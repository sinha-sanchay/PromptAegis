# Prompt_Injection — Student Project

Clean, self-contained instructions and notes for the code and data contained in this folder.

This repository contains the code, data, and notebooks used for a prompt-injection detection project.
The repo includes three notebooks developed in order (Notebook 1 → Notebook 2 → Notebook 3), a small Python package `injex/`, and saved model artifacts.

**Quick summary**
- Notebooks: Exploratory baseline (TF-IDF), advanced ensemble + thresholding, transformer fine-tuning.
- Data: CSV files under `dataset/` (Sanchay, Muskan, train/test splits, and produced `final_cleaned_dataset.csv`).
- Model: Large transformer saved under `injex/transformer/model/` and tracked with Git LFS on `main`.
- Branches: `main` (includes LFS-tracked model), `code-only` (does not include the large model; recommended for contributors).

Getting started (local, Windows)
-------------------------------
1. Clone the repo (choose branch):

   - To get code and the model (requires git-lfs and may consume LFS quota):

     ```powershell
     git clone https://github.com/sinha-sanchay/PromptAegis.git
     cd PromptAegis
     git checkout main
     git lfs install
     git lfs pull --include="injex/transformer/model/model.safetensors"
     ```

   - To get code only (no large model):

     ```powershell
     git clone https://github.com/sinha-sanchay/PromptAegis.git
     cd PromptAegis
     git checkout code-only
     ```

2. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

3. Run notebooks in order:

- `Notebooks/1_lightweight_model_tfidf_logistic.ipynb` — baseline (fast).
- `Notebooks/2_advanced_ml_ensemble_threshold.ipynb` — ensemble + threshold tuning (heavier).
- `Notebooks/3_roberta_transformer.ipynb` — XLM-R transformer fine-tune and external evaluation (Colab paths need updating for local runs).

Notes about paths
-----------------
- Notebooks were originally developed for Google Colab. Replace `/content/project/Prompt_Injection/...` with local paths like `dataset/...` before running locally.
- The transformer notebook saves/loads models from `injex/transformer/model/` — if you use `code-only` branch, that folder may be present but the large `model.safetensors` file is not tracked on that branch.

Model & storage
----------------
- The transformer model file `injex/transformer/model/model.safetensors` is tracked via Git LFS on `main`.
- GitHub enforces file-size limits — LFS is used to host the large object, but pushing it consumes the repository owner's LFS quota.
- If you do not want to use Git LFS, download the model from an external storage location and place it at `injex/transformer/model/model.safetensors`.

Evaluation results (transformer)
-------------------------------
These are the reported numbers from the transformer evaluation (external/test split):

- Class 0 (safe): precision 0.99, recall 0.96, f1-score 0.97 (support 600)
- Class 1 (attack): precision 0.97, recall 0.99, f1-score 0.98 (support 651)
- Accuracy: 0.98 (1251 samples)

Small developer notes
---------------------
- `.venv/` is ignored by default (do not commit virtual environments).
- `code-only` branch: created to simplify contributions without LFS downloads.
- If you need the model and cannot use Git LFS, I can provide a download script or upload location.

How I set this up (for maintainers)
-----------------------------------
- I migrated the large model into Git LFS and force-pushed rewritten refs so that the LFS pointer is present in history.
- I pushed a `code-only` branch (the local copy of the model remains on disk, but the branch does not track it). This keeps the remote `main` usable for model consumers while providing a lightweight branch for contributors.

If you want changes
-------------------
- I can add a small `scripts/fetch_model.sh` (or `fetch_model.ps1`) to automate `git lfs pull` for the model.
- I can add exact commands or CI instructions for contributors. Tell me which you'd like.

---
Student-style notes: short, clear, and focused on reproducibility. Let me know if you'd like a one-page quick-run cheat sheet added at the top.
