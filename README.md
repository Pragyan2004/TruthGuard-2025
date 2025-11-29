# TruthGuard-2025

A complete end-to-end Fake News Detection system built using Machine Learning + Deep Learning + Flask API.
This repository contains full model training scripts, TF-IDF + Logistic Regression model, LSTM neural network model, visualization reports, and a web app with real-time prediction support.

---
# Project Structure

TruthGard-2025

│

├── app.py
     
│

├── templates/

│   ├── index.html

│   ├── detector.html

│   ├── analysis.html

│   ├── about.html

│   └── contact.html

│

├── static/

│   ├── css/

│   └── js/

│

├── Fake.csv 

├── True.csv 

│

├── logistic_regression_model.pkl

├── tfidf_vectorizer.pkl

├── lstm_model.h5

├── tokenizer.pkl

├── all_models.pkl

│

└── README.md

---
# Features

| Feature                          | Description                                                       |
| -------------------------------- | ----------------------------------------------------------------- |
| 🔍 Real-time News Classification | Detect whether news is *Real* or *Fake* instantly                 |
| 🧠 Multiple Models               | Logistic Regression, Naive Bayes, SVM, LSTM                       |
| 📊 Advanced NLP                  | Lemmatization, Tokenization, Stop-word removal                    |
| 📁 Supports API requests         | `/predict` for single & `/batch_predict` for multiple text inputs |
| 🖥 Flask Web App                 | Beautiful UI – Home, Detector, Dashboard, Contact pages           |
| 📈 Visualizations                | Training metrics, confusion matrix, model comparison              |
| 💾 Model Saving                  | Pickle + TensorFlow SavedModel + Joblib bundling                  |

---

# Installation & Setup

### 1️⃣ Clone Repository
```
git clone https://github.com/your-username/fake-news-detection.git
cd fake-news-detection
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 3️⃣ Run Flask App
```
python app.py
```
```
Server will start at: http://127.0.0.1:5000
```

---

### Model Training & Evaluation

Models implemented:

| Model               | Vectorizer            | Type           | Performance                        |
| ------------------- | --------------------- | -------------- | ---------------------------------- |
| Logistic Regression | TF-IDF                | Traditional ML | ⭐ Best Accuracy                    |
| Naive Bayes         | TF-IDF                | Lightweight ML | Fast & Efficient                   |
| SVM                 | TF-IDF                | ML             | Strong margin-based classification |
| LSTM                | Tokenizer + Embedding | Deep Learning  | Sequential text understanding      |

---

# Screenshots

<img width="1220" height="720" alt="Screenshot 2025-11-29 120456" src="https://github.com/user-attachments/assets/d4289b80-7144-42e7-8edd-4c451b50a461" />

<img width="1221" height="760" alt="Screenshot 2025-11-29 120509" src="https://github.com/user-attachments/assets/43e258a9-7c6e-4b3b-80c6-bb14163d0264" />

<img width="1237" height="849" alt="Screenshot 2025-11-29 120521" src="https://github.com/user-attachments/assets/93c158f3-5b79-4c26-9f69-619a8e5bb648" />

<img width="1177" height="934" alt="Screenshot 2025-11-29 120533" src="https://github.com/user-attachments/assets/99a3d010-49da-4d1a-a846-2a7fef019d09" />

<img width="1194" height="889" alt="Screenshot 2025-11-29 120547" src="https://github.com/user-attachments/assets/a68c741b-1c19-4537-99cf-9fbd06607be0" />

<img width="1152" height="857" alt="Screenshot 2025-11-29 120558" src="https://github.com/user-attachments/assets/fd9a1bf4-7087-4c03-910a-8c6763bc8482" />

<img width="1207" height="943" alt="Screenshot 2025-11-29 120612" src="https://github.com/user-attachments/assets/307dd94a-831e-40fd-a22d-f092401c0e02" />

---

# Future Improvements

🔹 Add BERT / RoBERTa transformer model

🔹 Chrome browser extension for instant detection

🔹 Deploy on AWS / Render / Railway

🔹 Real-time scraping + news credibility score
