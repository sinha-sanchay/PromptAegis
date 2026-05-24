import re

# ============================================================
# TEXT PREPROCESSING
# ============================================================

def preprocess(text):

    text = str(text)

    # lowercase
    text = text.lower()

    # normalize spaces
    text = re.sub(r"\s+", " ", text)

    # strip spaces
    text = text.strip()

    return text