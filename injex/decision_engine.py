import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "model")

def get_threshold():
    with open(os.path.join(MODEL_DIR, "threshold.json")) as f:
        return json.load(f)["threshold"]

def decide(score):
    threshold = get_threshold()
    return "BLOCK" if score >= threshold else "ALLOW"