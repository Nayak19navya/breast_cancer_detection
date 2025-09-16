# Breast Cancer Classification using DenseNet  

A web-based machine learning project for classifying breast cancer from ultrasound images using **DenseNet**.  
The system allows users to upload medical images through a web interface and get real-time predictions (benign / malignant/normal).  

---

## 🚀 Features
- Deep Learning model (**DenseNet**) trained on breast ultrasound images.  
- Frontend: **HTML, CSS, JavaScript**.  
- Backend: **Flask (Python)** for server-side processing.  
- Model evaluation using **accuracy, precision, recall, F1-score**.  
- Deployed with **Heroku (Procfile + setup.sh)**.  

---

## 📂 Project Structure
├── app.py  Main Flask application
├── img_classification.py  DenseNet model and inference logic
├── requirements.txt  Python dependencies
├── setup.sh  Setup script for deployment
├── Procfile  Process type declaration for Heroku
└── README.md  Project documentation
