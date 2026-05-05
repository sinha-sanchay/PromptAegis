from .preprocessing import preprocess
from .predictor import get_score
from .decision_engine import decide

def inspect(text):
    clean_text = preprocess(text)
    score = get_score(clean_text)
    decision = decide(score)

    return {
        "text": text,
        "score": float(score),
        "decision": decision
    }