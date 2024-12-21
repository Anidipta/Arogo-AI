import os
import sqlite3
import numpy as np
from flask import Flask, render_template, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import Model
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.layers import GlobalAveragePooling2D
from pickle import load
from tensorflow.keras.optimizers import SGD

# Flask app initialization
app = Flask(__name__)

data_db_path = "data.db"

# Database initialization
def init_db():
    conn = sqlite3.connect(data_db_path)
    cursor = conn.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_name TEXT NOT NULL,
            caption TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

class utils:
    @staticmethod
    def get_image_features(img_abs_path):
        # Load ResNet50 model with ImageNet weights, without the top classification layer
        base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
        
        # Add Global Average Pooling to convert the feature map to a vector
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        
        # Create the feature extraction model
        model = Model(inputs=base_model.input, outputs=x)
        
        # Load and preprocess the image
        img = load_img(img_abs_path, target_size=(224, 224))
        img = img_to_array(img)
        img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
        img = preprocess_input(img)
        
        # Get the features from the image
        features = model.predict(img)
        return features

    @staticmethod
    def load_pretrained_data(model_path, tokenizer_path):
        # Load the pre-trained captioning model and tokenizer
        model = load_model(model_path, compile=False)  # Load model without compiling
        # Update optimizer if needed
        optimizer = SGD(learning_rate=0.01)  # Replace `lr` with `learning_rate`
        model.compile(optimizer=optimizer, loss='categorical_crossentropy')

        tk = load(open(tokenizer_path, 'rb'))  # Load tokenizer from pickle file
        return model, tk, 22  # 22 is the maximum length of the caption sequence

    @staticmethod
    def get_word_from_idx(idx, tokenizer):
        # Get word from index using tokenizer's word_index
        idx_to_word = {val: key for key, val in tokenizer.word_index.items()}
        return idx_to_word.get(idx, None)

    @staticmethod
    def generate_caption(model_path, image_path, tokenizer_path):
        # Start sequence for caption generation
        ip_seq = 'startseq'
        model, tk, max_length = utils.load_pretrained_data(model_path, tokenizer_path)

        # Get image features
        features = utils.get_image_features(image_path)

        for idx in range(max_length):
            seq = tk.texts_to_sequences([ip_seq])[0]
            seq = pad_sequences([seq], maxlen=max_length, padding='post')
            
            # Predict the next word in the sequence
            new_word_distribution = model.predict([features, seq], verbose=0)
            new_word_idx = np.argmax(new_word_distribution)
            new_word = utils.get_word_from_idx(new_word_idx, tk)

            # Append the word if it's not the 'endseq'
            if new_word and new_word != 'endseq':
                ip_seq += " " + new_word
            else:
                break

        # Return the caption by removing the start and end sequences
        return " ".join([i for i in ip_seq.split(' ') if i not in ['startseq', 'endseq']])

model_path = 'model_20_.h5'
tokenizer_path = 'tokenizer_vt2.pkl'

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        image = request.files['image']

        if image:
            img_name = image.filename
            img_path = os.path.join("./", img_name)
            image.save(img_path)

            # Generate caption for the uploaded image
            caption = utils.generate_caption(model_path, img_path, tokenizer_path)

            # Save the image name and caption to the database
            conn = sqlite3.connect(data_db_path)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO uploads (image_name, caption) VALUES (?, ?)', (img_name, caption))
            conn.commit()
            conn.close()

            # Delete the image file after processing
            os.remove(img_path)

            return jsonify({'image_path': img_path, 'caption': caption})

    return jsonify({'error': 'No image uploaded'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
