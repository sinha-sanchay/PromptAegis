import os
import json

# ============================================================
# LOAD THRESHOLD
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(__file__)
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "model"
)

# ============================================================
# LOAD THRESHOLD
# ============================================================

def get_threshold():

    with open(
        os.path.join(MODEL_DIR, "threshold.json")
    ) as f:

        return json.load(f)["threshold"]

# ============================================================
# FINAL DECISION
# ============================================================

def decide(score):

    threshold = get_threshold()

    # strong attack
    if score >= threshold:
        return "BLOCK"

    # suspicious
    elif score >= 0.40:
        return "REVIEW"

    # safe
    else:
        return "ALLOW"