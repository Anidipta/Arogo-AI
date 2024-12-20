from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow_hub as hub 
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os

app = Flask(__name__)
CORS(app)

# Load pre-trained model from TensorFlow Hub
model_url = "https://tfhub.dev/google/imagenet/mobilenet_v2_140_224/classification/4"
model = hub.load(model_url)
IMAGE_SHAPE = (224, 224)

# Load ImageNet class labels
with open('Task-2/imagenet_labels.txt', 'r') as f:
    labels = [line.strip() for line in f.readlines()]


def process_image(image_data):
    # Convert bytes to PIL Image
    image = Image.open(io.BytesIO(image_data))
    
    # Preprocess image: resize, convert to numpy array, and normalize
    image = image.resize(IMAGE_SHAPE)
    image = np.array(image) / 255.0  # Normalize the image to [0, 1]
    
    # Convert to float32
    image = image.astype(np.float32)
    
    # Expand dimensions for batch size
    image = tf.expand_dims(image, 0)  # Shape should be (1, 224, 224, 3)
    
    # Get predictions from the model
    predictions = model(image)
    
    # Get predicted class and confidence
    predicted_class = tf.argmax(predictions[0])
    confidence = tf.nn.softmax(predictions[0])[predicted_class]
    print(f"Predicted Class: {predicted_class}, Confidence: {confidence}")
    
    return {
        'class': labels[predicted_class],
        'confidence': float(confidence) * 100
    }
    
@app.route('/api/describe', methods=['POST'])
def describe_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    try:
        image_file = request.files['image']
        image_data = image_file.read()
        result = process_image(image_data)
        
        return jsonify({
            'description': f"This image appears to be a {result['class'].lower()} " \
                         f"(confidence: {result['confidence']:.2f}%)"
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)