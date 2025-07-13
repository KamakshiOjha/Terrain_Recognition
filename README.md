# 🌍 Terrain Recognition using CNN

This project focuses on **terrain classification** using a Convolutional Neural Network (CNN). The model is trained to recognize four types of terrains — **Grassy**, **Marshy**, **Rocky**, and **Sandy** — using labeled image data. A simple Flask-based web app provides a user-friendly interface to interact with the model.

---

## 🚀 How to Run

To run this project locally, follow these steps:

1. Clone the repository using:

   `https://github.com/KamakshiOjha/Terrain_Recognition.git`  
   `cd terrain_classifier`

2. Make sure Python 3 is installed on your machine. Install all required dependencies by running:  
   
   `pip install -r requirements.txt`

3. After installing the dependencies, start the web server with:  
   
   `python3 app.py`

4. Once the server is running, open your browser and go to:  
   
   `http://127.0.0.1:5000`

You will see a web UI where you can upload an image and get terrain predictions in real-time.

---

## 📊 Dataset

- **Source**: [Kaggle - Terrain Recognition Dataset](https://www.kaggle.com/datasets/atharv1610/terrain-recognition)

The dataset is divided into three parts:
- **Training set**: 14,956 images  
- **Validation set**: 6,721 images  
- **Test set**: 6,769 images  
Each image has a shape of (224, 224, 3).

---

## 🧠 Model Performance (on Test Set)

The CNN model achieved high accuracy and balanced precision-recall values across all classes. Below are the metrics:
<img width="413" height="187" alt="Screenshot 2025-07-13 at 12 23 39 PM" src="https://github.com/user-attachments/assets/f20608a5-78ac-49b9-9548-0de92e437680" />

- **Overall Accuracy**: 97%  
- **Macro Average**: 97%  
- **Weighted Average**: 97%

---

## 🖼 UI Preview

Here are some snapshots of the web interface used to classify terrain images.

<p align="center">
  <img width="1357" height="678" alt="Screenshot 2025-07-13 at 12 13 41 PM" src="https://github.com/user-attachments/assets/79832f90-f0c2-41fb-921e-f73ab883e6a3" />
  <img width="594" height="588" alt="Screenshot 2025-07-13 at 12 14 46 PM" src="https://github.com/user-attachments/assets/86977970-f619-486b-9e00-3162617a4b7f" />
</p>

---

## 📌 Confusion Matrix

<p align="center">
  <img width="360" height="293" alt="Screenshot 2025-07-13 at 12 25 13 PM" src="https://github.com/user-attachments/assets/63b619ef-861b-4dac-9678-c4ef8943bf0a" />
</p>

---

## ✨ Features

- Real-time terrain classification from uploaded images
- CNN-based deep learning model with 97% accuracy
- Simple and intuitive web interface using Flask
- Easily extendable for more terrain classes or larger datasets


