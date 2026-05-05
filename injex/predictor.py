import os
import joblib

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")

vectorizer = joblib.load(os.path.join(MODEL_DIR, "vectorizer.pkl"))
lr = joblib.load(os.path.join(MODEL_DIR, "lr.pkl"))
svm = joblib.load(os.path.join(MODEL_DIR, "svm.pkl"))
sgd = joblib.load(os.path.join(MODEL_DIR, "sgd.pkl"))

def ensemble_score(vec):
    lr_score = lr.predict_proba(vec)[:,1]
    svm_score = svm.predict_proba(vec)[:,1]
    sgd_score = sgd.predict_proba(vec)[:,1]
    
    return (lr_score + svm_score + sgd_score) / 3

def get_score(text):
    vec = vectorizer.transform([text])
    return ensemble_score(vec)[0]