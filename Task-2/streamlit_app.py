import streamlit as st
import requests
from io import BytesIO
from PIL import Image

# Configure the page layout and theme
st.set_page_config(
    page_title="Image Processor",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Main background and text colors */
    .stApp {
        background: linear-gradient(to bottom right, #000000, #1a1a1a);
        color: #ffffff;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(90deg, #00c6fb 0%, #005bea 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    /* Upload section styling */
    .upload-section {
        background: rgba(255, 255, 255, 0.05);
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid rgba(0, 198, 251, 0.2);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(90deg, #00c6fb 0%, #005bea 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        border-radius: 5px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 198, 251, 0.3);
    }
    
    /* Response section styling */
    .response-section {
        background: rgba(255, 255, 255, 0.05);
        padding: 1.5rem;
        border-radius: 10px;
        margin-top: 2rem;
        border: 1px solid rgba(0, 198, 251, 0.2);
    }
    
    /* Image display styling */
    .uploaded-image {
        border: 2px solid rgba(0, 198, 251, 0.3);
        border-radius: 10px;
        padding: 0.5rem;
    }
    
    /* Status message styling */
    .success-message {
        color: #00ff9f;
        padding: 1rem;
        border-radius: 5px;
        background: rgba(0, 255, 159, 0.1);
    }
    
    .error-message {
        color: #ff4d4d;
        padding: 1rem;
        border-radius: 5px;
        background: rgba(255, 77, 77, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Define the URL of your Flask API
url = "http://127.0.0.1:5000/upload"

# Custom header
st.markdown('<div class="main-header"><h1>🖼️ Image Processing Portal</h1></div>', unsafe_allow_html=True)

# Create two columns for layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### Upload Your Image")
    st.markdown("Select an image file to process (JPG, JPEG, or PNG)")
    
    # Allow user to upload an image
    image_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
    st.markdown('</div>', unsafe_allow_html=True)

# Process and display the image
if image_file is not None:
    with col2:
        st.markdown("### Preview")
        # Display the uploaded image
        image = Image.open(image_file)
        # Get original dimensions
        width, height = image.size
        # Calculate new dimensions (45% of original)
        new_width = int(width * 0.45)
        new_height = int(height * 0.45)
        # Resize image
        resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        st.image(resized_image, caption="Uploaded Image", use_column_width=False)
        st.markdown('</div>', unsafe_allow_html=True)

    # Convert image to binary format
    image_bytes = BytesIO()
    image.save(image_bytes, format='JPEG')
    image_bytes.seek(0)

    # Send the image to the Flask server
    files = {"image": image_bytes}
    
    st.markdown("### Processing Results")
    
    try:
        with st.spinner('Processing image...'):
            response = requests.post(url, files=files)
            
        if response.status_code == 200:
            st.markdown('<div class="success-message">', unsafe_allow_html=True)
            st.markdown(f"✅ Success! Status Code: {response.status_code}")
            st.markdown('</div>', unsafe_allow_html=True)
            
            try:
                response_json = response.json()
                st.json(response_json)
            except requests.exceptions.JSONDecodeError:
                st.code(response.text)
                
        else:
            st.markdown('<div class="error-message">', unsafe_allow_html=True)
            st.markdown(f"⚠️ Error! Status Code: {response.status_code}")
            st.markdown('</div>', unsafe_allow_html=True)
            st.code(response.text)
            
    except requests.exceptions.RequestException as e:
        st.markdown('<div class="error-message">', unsafe_allow_html=True)
        st.markdown(f"⚠️ Connection Error: {str(e)}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)