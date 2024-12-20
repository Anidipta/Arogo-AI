# Arogo-AI: 🚛 Shipment Delay Prediction & 🖼️ Image Description Web Application  

Welcome to the **AI/ML Internship Submission** repository! This document outlines the approach, steps, and decisions taken to solve the given problems: **Shipment Delay Prediction** and **Image Description Web Application**.

---

## 🚛 **Problem 1: Shipment Delay Prediction**  

### 📋 **Objective**  
Build a classification model to predict shipment delays based on historical logistics data and deploy it as an API.

### 🛠️ **Steps**  

#### 1️⃣ **Data Preparation & Exploration**  
- 🧹 **Data Cleaning**  
  - Removed duplicates and handled missing values (imputed weather and traffic conditions).  
  - Standardized distance and date formats.  

- 📊 **EDA**  
  - Visualized relationships between features (e.g., traffic/weather vs. delays).  
  - Correlation matrix to identify significant predictors.  

#### 2️⃣ **Model Development**  
- ✨ **Algorithms Tried**  
  - Logistic Regression  
  - Random Forest  

- 🧪 **Performance Evaluation**  
  Metrics Used:  
  - **Accuracy**  
  - **Precision**  
  - **Recall**  
  - **F1 Score**  

| Model              | Accuracy | Precision | Recall | F1 Score |  
|---------------------|----------|-----------|--------|----------|  
| Logistic Regression | 82%      | 78%       | 80%    | 79%      |  
| Random Forest       | 88%      | 84%       | 87%    | 85%      |  

#### 3️⃣ **Deployment**  
- 🌐 Built a **FastAPI**-based REST API.  
- 📮 Endpoint `/predict-delay` accepts shipment details and returns prediction:  
  - `{"Delayed": "Yes"}` or `{"Delayed": "No"}`  

### 🔧 **Usage Instructions**  

#### 🚀 **Run Locally**  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/username/shipment-delay-prediction  
   cd shipment-delay-prediction  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Start the API:  
   ```bash  
   uvicorn main:app --reload  
   ```  
4. Test the API:  
   Use tools like Postman or CURL.  

#### 📂 **Files**  
- **main.py**: API logic.  
- **model.pkl**: Trained Random Forest model.  
- **EDA.ipynb**: EDA and data preparation.  

---

## 🖼️ **Problem 2: Image Description Web Application**  

### 📋 **Objective**  
Develop a web application where users upload images and receive descriptions of their content.

### 🛠️ **Steps**  

#### 1️⃣ **Backend**  
- 🧠 Integrated a **Hugging Face pre-trained model** for image captioning.  
- 🛠️ Built a **FastAPI** endpoint for image upload and description generation.  
- 🌥️ Deployed on **AWS** for reliability.  

#### 2️⃣ **Frontend**  
- 🎨 Designed a user-friendly web interface using HTML, CSS, and JS.  
- 📤 Added image upload functionality with a drag-and-drop feature.  
- 🖼️ Displayed generated descriptions elegantly.  

#### 3️⃣ **Deployment**  
- 🖥️ Hosted the backend on AWS and the frontend on GitHub Pages for easy access.  

### 🔧 **Usage Instructions**  

#### 🌐 **Access the App**  
1. Open the [web application link](https://your-deployment-link.com).  
2. Upload an image using the upload button or drag and drop.  
3. Wait for the magic 🪄—a description appears below!  

#### 🚀 **Run Locally**  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/username/image-description-webapp  
   cd image-description-webapp  
   ```  
2. Install backend dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  
3. Start the API:  
   ```bash  
   uvicorn main:app --reload  
   ```  
4. Open the `index.html` file in your browser.  

#### 📂 **Files**  
- **main.py**: Backend API logic.  
- **index.html**: Frontend interface.  
- **model.py**: Model integration logic.  

---

### 🏆 **Key Features**  
1. **Shipment Delay Prediction**:  
   - 🚚 Reliable predictions for logistics management.  
   - 💡 Easy-to-use API for real-time integration.  

2. **Image Description App**:  
   - 🖼️ Accurate and engaging descriptions.  
   - 🌍 Deployed on the cloud for seamless access.  

---  

### 🤝 **Contributors**  
- 👨‍💻 [Anidipta](https://github.com/Anidipta)  

📬 Feel free to reach out for queries or collaborations!  

---  

🌟 Happy Coding! 🚀  
