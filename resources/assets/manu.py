import os
import pandas as pd

# Caminho absoluto baseado na posição do script
base_dir = os.path.dirname(__file__)
csv_path = os.path.join(base_dir, '..', '..', 'resources', 'contents', 'archives', 'chaves.csv')
csv_path = os.path.abspath(csv_path)  # Normaliza o caminho

# Leitura do CSV
df = pd.read_csv(csv_path)

# Iteração pelas linhas do DataFrame
for _, row in df.iterrows():
    tipo = str(row['Tipo']).strip()  # Certifique-se de que as colunas estão corretas
    chave = str(row['Chave']).strip()
    qtd = int(row['Qtd'])

    print(f"Tipo: {tipo} | Chave: {chave} | Qtd: {qtd}")
