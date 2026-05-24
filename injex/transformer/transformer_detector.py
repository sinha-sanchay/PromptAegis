# ============================================================
# TRANSFORMER DETECTOR
# ============================================================

import os
import torch

from transformers import (
    XLMRobertaTokenizer,
    XLMRobertaForSequenceClassification
)

# ============================================================
# MODEL PATH
# ============================================================

BASE_DIR = os.path.dirname(__file__)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model"
)

# ============================================================
# DEVICE
# ============================================================

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

# ============================================================
# LOAD TOKENIZER
# ============================================================

tokenizer = XLMRobertaTokenizer.from_pretrained(
    MODEL_PATH
)

# ============================================================
# LOAD MODEL
# ============================================================

model = XLMRobertaForSequenceClassification.from_pretrained(
    MODEL_PATH
)

model.to(device)

model.eval()

# ============================================================
# TRANSFORMER DETECTION FUNCTION
# ============================================================

def transformer_detect(text):

    # tokenize input
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    # move to device
    inputs = {
        k: v.to(device)
        for k, v in inputs.items()
    }

    # inference
    with torch.no_grad():

        outputs = model(**inputs)

        probs = torch.softmax(
            outputs.logits,
            dim=1
        )

        score = probs[0][1].item()

    return round(score, 4)