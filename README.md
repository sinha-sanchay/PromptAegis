# Prompt Injection Detection System

An advanced machine learning system for detecting prompt injection attacks using ensemble learning and threshold optimization.

## Overview

This project implements a sophisticated prompt injection detection system that combines multiple machine learning models to accurately classify prompts as either safe (ALLOW) or malicious (BLOCK).

## Features

- **Advanced Text Preprocessing**: Regex-based URL/email removal, special character normalization
- **Enhanced Feature Engineering**: TF-IDF with 10k features, trigrams, sublinear scaling
- **Stacking Ensemble**: 6+ base models with meta-learner for robust predictions
- **Hyperparameter Tuning**: GridSearchCV optimization for individual models
- **Threshold Optimization**: Multiple strategies (Max F1, Security-First, Balanced Accuracy)
- **Comprehensive Evaluation**: ROC-AUC, Precision-Recall curves, confusion matrices
- **Multi-Dataset Validation**: Internal test + external dataset evaluation

## Project Structure

```
Prompt_Injection/
├── dataset/                          # Training and test datasets
│   ├── Sanchay.csv                  # Dataset 1
│   ├── Muskan.csv                   # Dataset 2
│   ├── train_updated.csv            # Training data
│   ├── test_updated.csv             # External test data
│   ├── train.csv
│   └── test.csv
├── model/                            # Saved models and configs
│   ├── vectorizer.pkl               # TF-IDF vectorizer
│   ├── ensemble.pkl                 # Stacking ensemble
│   ├── lr.pkl, svm.pkl, etc.        # Base models
│   ├── threshold.json               # Optimal threshold
│   └── metrics.json                 # Performance metrics
├── Notebooks/                        # Jupyter notebooks
│   ├── 1_lightweight_model_tfidf_logistic.ipynb
│   └── 2_advanced_ml_ensemble_threshold.ipynb
├── injex/                            # Python package
│   ├── __init__.py
│   ├── core.py                      # Core prediction logic
│   ├── decision_engine.py           # Decision engine
│   ├── predictor.py                 # Predictor class
│   └── preprocessing.py             # Text preprocessing
├── setup.py                          # Package setup
└── README.md                         # This file
```

## Installation

### Requirements
- Python 3.8+
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
- joblib

### Setup

1. Clone the repository:
```bash
git clone https://github.com/sinha-sanchay/prompt-injection-detection.git
cd prompt-injection-detection
```

2. Create virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# or
source .venv/bin/activate  # On Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install package:
```bash
pip install -e .
```

## Usage

### Quick Prediction

```python
from injex.predictor import PromptPredictor

predictor = PromptPredictor()
label, score = predictor.predict("Your prompt here")
print(f"Prediction: {label}, Score: {score}")
```

### Detailed Prediction

```python
result = predictor.predict("Your prompt here", return_details=True)
print(f"Label: {result['label']}")
print(f"Score: {result['score']:.4f}")
print(f"Confidence: {result['confidence']:.4f}")
```

### Using Decision Engine

```python
from injex.decision_engine import DecisionEngine

engine = DecisionEngine()
decision = engine.evaluate_prompt("Your prompt here")
print(f"Decision: {decision}")
```

## Model Performance

### Validation Set
- Accuracy: ~97%+
- Precision: ~96%+
- Recall: ~96%+
- F1 Score: ~97%+
- ROC-AUC: ~99%+

### Test Set
- Similar performance metrics

### External Dataset
- Validated on separate dataset
- Strong generalization capability

## Training Pipeline

### 1. Data Loading & Preprocessing
- Load from multiple CSV sources
- Handle mixed label types
- Normalize to binary classification
- 70% train, 15% val, 15% test split

### 2. Feature Extraction
- TF-IDF vectorization
- 10,000 features with trigrams
- min_df=2, max_df=0.95 filtering
- Sublinear TF scaling

### 3. Model Training
- Logistic Regression (with GridSearchCV)
- Linear SVM (calibrated)
- SGD Classifier (calibrated)
- Ridge Classifier (calibrated)
- Complement Naive Bayes
- Random Forest (with SVD reduction)

### 4. Ensemble Creation
- Stacking ensemble with meta-learner
- 3-fold cross-validation
- Logistic Regression as final estimator

### 5. Threshold Optimization
- 91 candidate thresholds tested
- Multiple selection strategies
- Security-first approach (recall ≥ 0.95)

### 6. Evaluation
- ROC-AUC curves
- Precision-Recall curves
- Confusion matrices
- Multi-dataset validation

## Notebooks

### Notebook 1: Lightweight Model
`1_lightweight_model_tfidf_logistic.ipynb`
- Basic TF-IDF + Logistic Regression
- Quick baseline performance

### Notebook 2: Advanced Ensemble
`2_advanced_ml_ensemble_threshold.ipynb`
- Advanced preprocessing
- 6+ model ensemble
- Threshold optimization
- Comprehensive evaluation

## Configuration

### Model Threshold
Edit `model/threshold.json`:
```json
{
  "threshold": 0.45,
  "threshold_f1": 0.50,
  "threshold_balanced": 0.48,
  "min_recall_constraint": 0.95
}
```

### Feature Parameters
Edit preprocessing settings:
- max_features: 10000
- ngram_range: (1, 3)
- min_df: 2
- max_df: 0.95

## Performance Optimization

### Batch Prediction
```python
texts = ["prompt1", "prompt2", "prompt3"]
predictions = predictor.predict_batch(texts)
```

### Threshold Tuning
Adjust security vs. precision tradeoff:
- Higher threshold: More conservative (fewer false positives)
- Lower threshold: More aggressive (fewer false negatives)

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Training New Model
```bash
# Run Notebook 2 to retrain
jupyter notebook Notebooks/2_advanced_ml_ensemble_threshold.ipynb
```

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create Pull Request

## License

MIT License - See LICENSE file for details

## Authors

- Sanchay Sinha

## Acknowledgments

- Ensemble learning techniques
- Scikit-learn library
- Machine Learning best practices

## References

- [Prompt Injection Research](https://arxiv.org/abs/2301.12519)
- [Ensemble Methods](https://scikit-learn.org/stable/modules/ensemble.html)
- [Stacking Classifiers](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.StackingClassifier.html)

## Contact

For questions or issues, please open an issue on GitHub or contact the maintainers.

---

**Last Updated**: May 6, 2026
