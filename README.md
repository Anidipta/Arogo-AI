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
- **app.py**: Frontend streamlit web app.
- **flask_api.py**: API logic for shipment delay prediction.  
- **best_automl_classifier.pkl**: Trained ExtraTreesClassifier model for delay prediction.  
- **Model_Training.ipynb**: Exploratory data analysis (EDA) and data prep.  


### Our App

![Task-1 App](Task-1%20App.png)


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
- **streamlit_app.py**: Frontend interface for streamlit web app.
- **flask_api.py**: Backend integrating the model for image captioning
- **data.db**: Database file used for storing the images and their responses.
- **model_20_.h5**: The pre-trained model for image description.
- **tokenizer_vt2.pkl**: Tokenizer, for processing text data related to image.

---

### 🤝 **Contributor**  
- 👨‍💻 [Anidipta](https://github.com/Anidipta)  
