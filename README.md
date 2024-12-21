## 🚛 **Problem 1: Shipment Delay Prediction**  

### 📋 **Objective**  
Build a model to predict shipment delays based on historical data and deploy it as an API.

### 🛠️ **How to Run Task 1**  

1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/Anidipta/Arogo-AI.git 
   cd Arogo-AI/Task-1 
   ```

2. **Install Dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```

3. **Start the API**  
   ```bash  
   python flask_api.py 
   ```

4. **Start the Streamlit Web App**  
     ```bash
     streamlit run app.py
     ```

### 📂 **Key Files**  
- **flask_api.py**: API logic for shipment delay prediction.  
- **best_automl_classifier.pkl**: Trained ExtraTreesClassifier model for delay prediction.  
- **Model_Training.ipynb**: Exploratory data analysis (EDA) and data prep.  

---

## 🖼️ **Problem 2: Image Description Web Application**  

### 📋 **Objective**  
Build a web app where users upload images and receive descriptions of the content.

### 🛠️ **How to Run Task 2**  

1. **Clone the Repository**  
   ```bash  
   git clone https://github.com/Anidipta/Arogo-AI.git  
   cd Arogo-AI/Task-2 
   ```

2. **Install Backend Dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```

3. **Start the API**  
   ```bash  
   python flask_api.py 
   ```

4. **Start the Streamlit Web App**  
     ```bash
     streamlit run streamlit_app.py
     ```

### 📂 **Key Files**  
- **streamlit_app.py**: This file contains the frontend interface for your Streamlit application, allowing users to upload images. It interacts with the backend API for image processing and displays the results.
- **flask_api.py**: This file serves as the backend of your project, integrating the model for image captioning. It handles requests from the frontend and processes images for predictions.
- **data.db**: Likely the database file used for storing relevant data for the project.
- **model_20_.h5**: The trained model file, possibly the machine learning model for image captioning or another task.
- **tokenizer_vt2.pkl**: A pickle file for the tokenizer, likely used for processing text data related to image captions or NLP tasks.

---

### 🏆 **Key Features**  

1. **Shipment Delay Prediction**:  
   - 🚚 Predict shipment delays.  
   - 🌐 API integration for logistics.  

2. **Image Description Web App**:  
   - 🖼️ Generate descriptions for images.  
   - 🌍 Hosted on AWS for easy access.  

---

### 🤝 **Contributors**  
- 👨‍💻 [Anidipta](https://github.com/Anidipta)  

📬 Reach out for queries or collaborations!  

---  

🌟 Happy Coding! 🚀
