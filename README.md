
# PromptAegis

A modular AI framework for detecting and scoring prompt injection risks in GPT-based systems using ML and transformer models.

![License](https://img.shields.io/github/license/sinha-sanchay/PromptAegis)
![Python](https://img.shields.io/badge/Python-1.3%25-blue)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter%20Notebook-98.7%25-orange)

---

## Overview

PromptAegis provides a suite of Jupyter notebooks and Python modules for analyzing, detecting, and scoring prompt injection threats for GPT-based and LLM-powered systems. It progressively explores lightweight ML approaches, advanced ensemble methods, and state-of-the-art transformer models.

---

## Notebooks & Algorithms

The repo features a 3-stage methodological progression for prompt injection detection:

### 1. Lightweight Model (TF-IDF + Logistic Regression)
**Notebook:** [1_lightweight_model_tfidf_logistic.ipynb](https://github.com/sinha-sanchay/PromptAegis/blob/main/Notebooks/1_lightweight_model_tfidf_logistic.ipynb)

- **Feature Extraction:** TF-IDF (Term Frequency–Inverse Document Frequency) with n-grams.
- **Model:** Logistic Regression (with class balancing, probability outputs).
- **Purpose:** 
    - Fast text vectorization.
    - Simple, interpretable, and suitable for real-time scenarios.
- **Workflow:** Data cleaning, feature extraction, model training, evaluation, and scoring of prompt risk.

---

### 2. Advanced ML – Ensemble & Threshold Tuning
**Notebook:** [2_advanced_ml_ensemble_threshold.ipynb](https://github.com/sinha-sanchay/PromptAegis/blob/main/Notebooks/2_advanced_ml_ensemble_threshold.ipynb)

- **Algorithms:**
    - **Logistic Regression**
    - **Linear SVM (Support Vector Machines)**
    - **SGDClassifier** (Stochastic Gradient Descent, often with log-loss)
    - **Model Calibration:** Using `CalibratedClassifierCV` for better probability estimates
- **Feature Extraction:** Advanced TF-IDF (larger vocabulary, bi-grams).
- **Ensembling:** Combining multiple model predictions for robustness.
- **Threshold Adjustment:** Custom threshold tuning post-calibration to define cutoff for ALLOW/BLOCK decisions.
- **Purpose:** 
    - Improved accuracy and stability.
    - Better handles ambiguity via ensemble voting and calibrated probabilities.

---

### 3. Transformer-based Detection with RoBERTa
**Notebook:** [3_roberta_transformer.ipynb](https://github.com/sinha-sanchay/PromptAegis/blob/main/Notebooks/3_roberta_transformer.ipynb)

- **Model:** XLM-RoBERTa (fine-tuned for sequence classification)
- **Frameworks:** HuggingFace `transformers`, PyTorch
- **Dataset Handling:** Uses HuggingFace `datasets` along with thorough data cleaning and balancing.
- **Purpose:** 
    - Leverages cutting-edge transformer models for the highest accuracy and context sensitivity.
    - Suitable for complex, nuanced, or multilingual prompt risk detection.
- **Implementation Notes:** Notebook is pre-configured for Google Colab (with device/GPU detection and Colab-specific paths).

---

## Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook
- [Optional] Google Colab for transformer notebook

### Installation

Clone the repository and install requirements:

```bash
git clone https://github.com/sinha-sanchay/PromptAegis.git
cd PromptAegis
pip install -r requirements.txt
```

### Running the Notebooks

Open the desired notebook in Jupyter or upload to Google Colab as relevant:
```
cd Notebooks
jupyter notebook
```
- Begin with `1_lightweight_model_tfidf_logistic.ipynb` for the simplest and fastest model.
- Proceed to `2_advanced_ml_ensemble_threshold.ipynb` for improved accuracy with ensemble methods.
- Use `3_roberta_transformer.ipynb` for transformer-based state-of-the-art results.


## Contributing

Pull requests, issues, and suggestions are welcome! Please contribute code, notebooks, or improvements to existing algorithms.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## References

- scikit-learn: Logistic Regression, SVM, SGDClassifier, TF-IDF
- HuggingFace Transformers
- XLM-RoBERTa: Large pre-trained transformer for sequence classification tasks
- Datasets: Provided/curated prompt injection samples

---
