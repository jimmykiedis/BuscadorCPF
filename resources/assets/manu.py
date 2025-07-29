import os
import pandas as pd

# Caminho absoluto baseado na posição do script
base_dir = os.path.dirname(__file__)
xlsx_path = os.path.join(base_dir, '..', '..', 'resources', 'contents', 'archives', 'chaves.xlsx')
xlsx_path = os.path.abspath(xlsx_path)  # Normaliza o caminho

# Leitura do Excel
df = pd.read_excel(xlsx_path)

for _, row in df.iterrows():
    tipo = str(row['Tipo']).strip()
    chave = str(row['Chave']).strip()
    qtd = int(row['Qtd'])

    print(f"Tipo: {tipo} | Chave: {chave} | Qtd: {qtd}")
