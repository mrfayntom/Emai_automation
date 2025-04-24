# make sure you are running in different cell, well you can run all in one cell but it look messy + if any error cause then take so much time to find so best is go with different cell

# cell 1:
from google.colab import drive
drive.mount('/content/drive')

import json

with open('/content/drive/MyDrive/Dataset-email/unique_emails.json','r',encoding='utf-8') as f: # change it with your path
 d=json.load(f)

x=[i["subject"]+" "+i["body"] for i in d]
y=[i["label"] for i in d]


#cell 2:
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, stratify=y, random_state=42)

tfidf = TfidfVectorizer(max_features=3000, stop_words='english')
train_x_vec = tfidf.fit_transform(train_x)
test_x_vec = tfidf.transform(test_x)

model = LogisticRegression(C=0.5, penalty='l2', class_weight='balanced', max_iter=1000)
model.fit(train_x_vec, train_y)

preds = model.predict(test_x_vec)

print(classification_report(test_y, preds))


#cell 3:
import joblib

joblib.dump(model, "/content/drive/MyDrive/email_classifier.pkl")
joblib.dump(tfidf, "/content/drive/MyDrive/email_vectorizer.pkl")
print("Model and vectorizer saved.")
