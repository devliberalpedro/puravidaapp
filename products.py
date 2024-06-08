import json
from pathlib import Path

# Função para ler os produtos cadastrados
def read_products(assets_path):
    with open(f'{assets_path}/products.json', 'r', encoding='utf-8') as file:
        return json.load(file)

