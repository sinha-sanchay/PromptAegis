import os
import joblib

from injex.transformer.transformer_detector import (
    transformer_detect
)

# ============================================================
# LOAD ML MODELS
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "model"
)

vectorizer = joblib.load(
    os.path.join(MODEL_DIR, "vectorizer.pkl")
)

lr = joblib.load(
    os.path.join(MODEL_DIR, "lr.pkl")
)

svm = joblib.load(
    os.path.join(MODEL_DIR, "svm.pkl")
)

sgd = joblib.load(
    os.path.join(MODEL_DIR, "sgd.pkl")
)

# ============================================================
# ENSEMBLE SCORE
# ============================================================

def ensemble_score(vec):

    lr_score = lr.predict_proba(vec)[:, 1]

    svm_score = svm.predict_proba(vec)[:, 1]

    sgd_score = sgd.predict_proba(vec)[:, 1]

    return (
        lr_score +
        svm_score +
        sgd_score
    ) / 3

# ============================================================
# HYBRID SCORING
# ============================================================

def get_score(text):

    # ensemble score
    vec = vectorizer.transform([text])

    ensemble = ensemble_score(vec)[0]

    # transformer score
    transformer = transformer_detect(text)

    # weighted hybrid score
    final_score = (
        0.4 * ensemble +
        0.6 * transformer
    )

    return {
        "ensemble_score":
            round(float(ensemble), 4),

        "transformer_score":
            round(float(transformer), 4),

        "final_score":
            round(float(final_score), 4)
    }