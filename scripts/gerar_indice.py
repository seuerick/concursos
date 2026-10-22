#!/usr/bin/env python3
"""Gera data.json com a estrutura do acervo (usado pelo GitHub Actions e localmente)."""
import json
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IGNORED = {
    '.git', '.github', 'node_modules', 'index.html', '.gitignore',
    'agent.py', 'ANALISE_PADRAO_TI_TCE_TCU.md', 'data.json', '.nojekyll', 'scripts',
}


def build(path):
    entries = []
    try:
        items = sorted(os.listdir(path), key=str.lower)
    except OSError:
        return entries
    for name in items:
        if name in IGNORED:
            continue
        full = os.path.join(path, name)
        if os.path.isdir(full):
            children = build(full)
            entries.append({'name': name, 'type': 'dir', 'children': children})
        else:
            entries.append({'name': name, 'type': 'file', 'size': os.path.getsize(full)})
    return entries


def main():
    tree = build(ROOT)
    data = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'tree': tree,
    }
    out = os.path.join(ROOT, 'data.json')
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'data.json gerado: {len(tree)} itens na raiz')


if __name__ == '__main__':
    sys.exit(main())
