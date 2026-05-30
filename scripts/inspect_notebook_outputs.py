import json
from pathlib import Path

nb_path = Path('Notebooks/3_roberta_transformer.ipynb')
if not nb_path.exists():
    print('MISSING')
    raise SystemExit(2)

with nb_path.open('r', encoding='utf-8') as f:
    nb = json.load(f)

cells = nb.get('cells', [])
print(f'Total cells: {len(cells)}')

heavy = []
for i, cell in enumerate(cells, start=1):
    outs = cell.get('outputs', []) if cell.get('cell_type') == 'code' else []
    total = 0
    types = set()
    for o in outs:
        try:
            s = json.dumps(o, ensure_ascii=False)
        except Exception:
            s = str(o)
        b = s.encode('utf-8')
        total += len(b)
        if isinstance(o, dict) and 'data' in o:
            for k in o['data'].keys():
                types.add(k)
    print(f'CELL {i}: outputs={len(outs)} bytes={total} types={sorted(types)}')
    if total > 50_000 or any(t.startswith('image/') or t == 'application/pdf' for t in types):
        heavy.append((i, total, sorted(types)))

print('\nHEAVY CELLS:')
for h in heavy:
    print('CELL', h[0], 'bytes=', h[1], 'types=', h[2])

if not heavy:
    print('\nNo heavy cells detected (threshold 50KB).')
else:
    print(f'\nDetected {len(heavy)} heavy cells. Recommended: clear outputs and re-push.')
