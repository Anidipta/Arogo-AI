# Arogo-AI: 🚛 Shipment Delay Prediction & 🖼️ Image Description Web Application  

Welcome to the **AI/ML Internship Submission** repository! This document provides a guide on how to run the **Shipment Delay Prediction** and **Image Description Web Application**.

---

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
   git clone https://github.com/username/image-description-webapp  
   cd image-description-webapp  
   ```

2. **Install Backend Dependencies**  
   ```bash  
   pip install -r requirements.txt  
   ```

3. **Start the API**  
   ```bash  
   uvicorn main:app --reload  
   ```

4. **Frontend Access**  
   - Open `index.html` in your browser to upload images and view generated descriptions.

### 📂 **Key Files**  
- **main.py**: Backend API for image description generation.  
- **index.html**: Frontend interface for image upload.  
- **model.py**: Model integration for image captioning.  

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
