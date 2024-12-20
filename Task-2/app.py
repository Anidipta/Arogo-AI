import streamlit as st
import requests
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance

# Streamlit UI
def main():
    st.title("🌟 Image Recognition App 🌟")

    # Sidebar customization
    st.sidebar.header("🔧 Customization")
    brightness_factor = st.sidebar.slider("Adjust Image Brightness", 0.5, 2.0, 1.0)

    # Upload image file
    uploaded_file = st.file_uploader("📂 Upload an image (jpg, jpeg, png)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        enhancer = ImageEnhance.Brightness(image)
        enhanced_image = enhancer.enhance(brightness_factor)

        st.image(enhanced_image, caption="📸 Uploaded Image", use_column_width=True)

        # Perform object detection on the uploaded image
        
        if st.button("🔍 Detect Objects"):
            if uploaded_file is not None:
                with st.spinner("Analyzing the image..."):
                    try:
                        # Send request to the Flask API
                        files = {"image": uploaded_file.getvalue()}
                        response = requests.post("http://127.0.0.1:5000/api/describe", files=files)

                        # Process the response
                        if response.status_code == 200:
                            result = response.json()
                            st.success("🎉 Detection Complete!")
                            st.write(f"**Description:** {result['description']}")
                        else:
                            st.error(f"Error: {response.status_code}, {response.json().get('error', 'Unknown error')}")

                    except Exception as e:
                        st.error(f"An error occurred: {e}")
            else:
                st.error("Please upload an image first.")

if __name__ == "__main__":
    main()
