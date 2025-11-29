from flask import Flask, render_template, request, jsonify
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """
    Preprocess text by:
    1. Converting to lowercase
    2. Removing special characters and digits
    3. Tokenizing
    4. Removing stopwords
    5. Lemmatizing
    """
    if isinstance(text, str):
        text = text.lower()
        
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        tokens = word_tokenize(text)
        
        tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
        
        return ' '.join(tokens)
    else:
        return ''

try:
    with open('logistic_regression_model.pkl', 'rb') as f:
        lr_model = pickle.load(f)
    
    with open('tfidf_vectorizer.pkl', 'rb') as f:
        tfidf_vectorizer = pickle.load(f)
    
    print("Models loaded successfully!")
except Exception as e:
    print(f"Error loading models: {e}")
    lr_model = None
    tfidf_vectorizer = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detector')
def detector():
    return render_template('detector.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            text = data.get('text', '')
            model_type = data.get('model_type', 'logistic')
            
            if not text.strip():
                return jsonify({
                    'error': 'Please enter some text to analyze.'
                })
            
            cleaned_text = preprocess_text(text)
            
            if model_type == 'logistic' and lr_model and tfidf_vectorizer:
                
                text_tfidf = tfidf_vectorizer.transform([cleaned_text])
                
                prediction = lr_model.predict(text_tfidf)[0]
                probability = lr_model.predict_proba(text_tfidf)[0]
                
                result = {
                    'prediction': 'Real News' if prediction == 1 else 'Fake News',
                    'confidence': float(max(probability)),
                    'fake_probability': float(probability[0]),
                    'real_probability': float(probability[1]),
                    'model_used': 'Logistic Regression',
                    'status': 'success'
                }
            else:
                result = {
                    'error': 'Selected model is not available. Using default model.',
                    'status': 'error'
                }
            
            return jsonify(result)
            
        except Exception as e:
            return jsonify({
                'error': f'Prediction error: {str(e)}',
                'status': 'error'
            })

@app.route('/batch_predict', methods=['POST'])
def batch_predict():
    if request.method == 'POST':
        try:
            data = request.get_json()
            texts = data.get('texts', [])
            
            if not texts:
                return jsonify({
                    'error': 'No texts provided for analysis.'
                })
            
            results = []
            for text in texts:
                cleaned_text = preprocess_text(text)
                text_tfidf = tfidf_vectorizer.transform([cleaned_text])
                prediction = lr_model.predict(text_tfidf)[0]
                probability = lr_model.predict_proba(text_tfidf)[0]
                
                results.append({
                    'text': text[:100] + '...' if len(text) > 100 else text,
                    'prediction': 'Real News' if prediction == 1 else 'Fake News',
                    'confidence': float(max(probability)),
                    'fake_probability': float(probability[0]),
                    'real_probability': float(probability[1])
                })
            
            return jsonify({
                'results': results,
                'total_analyzed': len(results),
                'fake_count': len([r for r in results if r['prediction'] == 'Fake News']),
                'real_count': len([r for r in results if r['prediction'] == 'Real News']),
                'status': 'success'
            })
            
        except Exception as e:
            return jsonify({
                'error': f'Batch prediction error: {str(e)}',
                'status': 'error'
            })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)