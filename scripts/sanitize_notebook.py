import json
from pathlib import Path

nb_path = Path('Notebooks/3_roberta_transformer.ipynb')
if not nb_path.exists():
    print('MISSING')
    raise SystemExit(2)

with nb_path.open('r', encoding='utf-8') as f:
    nb = json.load(f)

# Remove colab/widget metadata at notebook level
for k in ['colab', 'widgets']:
    if k in nb.get('metadata', {}):
        nb['metadata'].pop(k, None)

# Sanitize cells: clear outputs and execution counts, keep metadata.id if present
for cell in nb.get('cells', []):
    if cell.get('cell_type') == 'code':
        cell['outputs'] = []
        cell['execution_count'] = None
    # remove known noisy metadata keys but preserve id
    meta = cell.get('metadata', {})
    for bad in ['collapsed', 'scrolled', 'run_control', 'colab']:
        if bad in meta:
            meta.pop(bad, None)
    cell['metadata'] = meta

with nb_path.open('w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Sanitized notebook: outputs cleared and Colab/widget metadata removed.')
