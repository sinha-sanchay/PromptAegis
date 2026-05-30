import json
from pathlib import Path
from datetime import datetime

nb_path = Path('Notebooks/3_roberta_transformer.ipynb')
if not nb_path.exists():
    print('Notebook missing:', nb_path)
    raise SystemExit(2)

with nb_path.open('r', encoding='utf-8') as f:
    nb = json.load(f)

summary_md = f"""
# Transformer results (summary)

_Inserted on {datetime.utcnow().isoformat()}Z by helper script._

**Evaluation (external/test split)**

| Class | Precision | Recall | F1-score | Support |
|---:|---:|---:|---:|---:|
| 0 (safe) | 0.99 | 0.96 | 0.97 | 600 |
| 1 (attack) | 0.97 | 0.99 | 0.98 | 651 |

- **Accuracy:** 0.98 (1251 samples)

> Note: The notebook's live cell outputs were cleared to improve GitHub rendering. The above summary reproduces the key reported metrics so the file previews on GitHub show results similar to the executed notebook.
"""

new_cell = {
    "cell_type": "markdown",
    "metadata": {"language": "markdown"},
    "source": [summary_md]
}

# Insert at top of cells
cells = nb.get('cells', [])
nb['cells'] = [new_cell] + cells

with nb_path.open('w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Inserted summary markdown cell at top of notebook.')
