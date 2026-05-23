import json

from .preprocessing import preprocess
from .predictor import get_score
from .decision_engine import decide

# ============================================================
# MAIN INSPECTION FUNCTION
# ============================================================

def inspect(text):

    # preprocess input
    clean_text = preprocess(text)

    # get hybrid scores
    scores = get_score(clean_text)

    # final score
    final_score = scores["final_score"]

    # final decision
    decision = decide(final_score)

    # final response
    result = {
        "text": text,

        "ensemble_score":
            scores["ensemble_score"],

        "transformer_score":
            scores["transformer_score"],

        "final_score":
            scores["final_score"],

        "decision": decision
    }

    # pretty json output
    # pretty json output
    print(
        json.dumps(
            result,
            indent=4
        )
    )

    return ""