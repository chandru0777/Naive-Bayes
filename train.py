import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load dataset
df = pd.read_csv("emails.csv")

# Features and labels
X = df['message']
y = df['label']

# Vectorization
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Save model & vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved successfully!")
