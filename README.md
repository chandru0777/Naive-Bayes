## Email Spam Detector using Naive Bayes & Flask
# Overview
The Email Spam Detector is a machine learning web application that predicts whether an email is Spam or Not Spam.
It uses the Naive Bayes algorithm for classification, trained on a dataset of email messages.
The web interface is built using Flask with a professional and responsive UI for ease of use.

# Features
Spam/Not Spam Classification using Naive Bayes

Real-time Predictions through a simple web form

Professional, Responsive UI (HTML + CSS + Bootstrap)

CSV Dataset with 50 sample email records

Easily Extensible – add more data for better accuracy

# Technology Stack
Machine Learning

Python 3.x

Scikit-learn (Naive Bayes Model)

Pandas, NumPy

Web Development

Flask (Backend)

HTML, CSS, Bootstrap (Frontend)

# Project Structure
```
📁 Email-Spam-Detector
│── 📄 train.py          # Trains the Naive Bayes model & saves it
│── 📄 app.py            # Flask app for prediction
│── 📄 spam.csv          # Dataset (50 records)
│── 📄 templates/
│     └── index.html     # Frontend UI
│── 📄 static/
│     └── style.css      # Custom CSS
│── 📄 model.pkl         # Trained model
│── 📄 requirements.txt  # Dependencies
│── 📄 README.md         # Project Documentation
```
## Dataset
The dataset spam.csv contains 50 labeled email messages with the following columns:

message – The email text content

label – spam or ham (ham = not spam)

## Installation & Setup
# 1️ Clone the Repository
```
git clone https://github.com/yourusername/email-spam-detector.git
cd email-spam-detector
```
# 2️ Create Virtual Environment (Optional but Recommended)
```
python -m venv venv
source venv/bin/activate      # On Mac/Linux
venv\Scripts\activate         # On Windows
```
# 3️ Install Dependencies
```
pip install -r requirements.txt
```
# 4️ Train the Model
```
python train.py
```
# 5️ Run the Flask App
```
python app.py
```
# 6️ Open in Browser
```
Visit: http://127.0.0.1:5000
```
## Usage
Open the web application.

Enter an email message in the input box.

Click Predict to check if it's spam or not.

## Example Prediction
Email Message	Prediction
"Congratulations! You've won a free iPhone"	Spam
"Meeting at 3 PM today in conference room"	Not Spam

## Future Improvements
Use a larger dataset for better accuracy

Implement TF-IDF Vectorization for better feature extraction

Add Email Subject + Body Analysis

Deploy on Heroku or Render for public access

## Screenshots
![alt text](<Screenshot 2025-08-11 140533.png>)
![alt text](<Screenshot 2025-08-11 140626.png>)
![alt text](<Screenshot 2025-08-11 140641.png>)