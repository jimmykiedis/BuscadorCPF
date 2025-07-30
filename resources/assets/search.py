from googlesearch  import search 
import requests
from playsound import playsound
import time
import csv
import os

# Diretório base (do script)
BASE_DIR = os.path.dirname(__file__)

# Caminhos dos arquivos
ENTRADAS_POSSIVEIS = os.path.abspath(os.path.join(BASE_DIR, '..', '..', 'contents', 'archives', 'possibilidades.txt'))
SAIDAS_RESULTANTES = os.path.abspath(os.path.join(BASE_DIR, '..', '..', 'contents', 'archives', 'resultados_encontrados.txt'))
ALERTA_SONORO = os.path.abspath(os.path.join(BASE_DIR, '..', '..', 'contents', 'archives', 'alerta.mp3'))
ENTRADAS_VARIACOES = os.path.abspath(os.path.join(BASE_DIR, '..', '..', 'contents', 'archives', 'variations.csv'))
ENTRADA_CHAVES = os.path.abspath(os.path.join(BASE_DIR, '..', '..', 'contents', 'archives', 'keys.csv'))

def carregar_chaves():
    chaves = []
    cx = ""
    with open(ENTRADA_CHAVES, "r", encoding="utf-8") as f:
        leitor = csv.reader(f)
        linhas = list(leitor)

        if linhas:
            cx = linhas[0][1].strip()  # A primeira linha deve conter o ID do mecanismo

        for linha in linhas[1:]:  # Começa da segunda linha
            if len(linha) >= 3:
                chave = linha[1].strip()
                usos = int(linha[2].strip())
                chaves.append({"chave": chave, "usos": usos})

    return cx, chaves

def salvar_chaves(cx, chaves):
    with open(ENTRADA_CHAVES, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f)
        escritor.writerow(["cx", cx, ""])  # Primeira linha com o mecanismo
        for i, item in enumerate(chaves):
            escritor.writerow([chr(97 + i), item["chave"], item["usos"]])

def carregar_variacoes():
    variacoes = []
    with open(ENTRADAS_VARIACOES, "r", encoding="utf-8") as f:
        leitor = csv.reader(f)
        for linha in leitor:
            for item in linha:
                item = item.strip().lower()
                if item:
                    variacoes.append(item)
    return variacoes

VARIACOES = carregar_variacoes()

def contem_variacao(texto):
    texto = texto.lower()
    return any(variacao in texto for variacao in VARIACOES)

def buscar_google(query, chaves, cx):
    for chave in chaves:
        if chave["usos"] <= 0:
            continue

        params = {
            "q": query,
            "key": chave["chave"],
            "cx": cx,
            "hl": "pt",
            "num": 10
        }

        try:
            response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)
            data = response.json()
            chave["usos"] -= 1

            for item in data.get("items", []):
                titulo = item.get("title", "").lower()
                snippet = item.get("snippet", "").lower()
                if contem_variacao(titulo) or contem_variacao(snippet):
                    return True
            return False
        except Exception as e:
            print(f"    ⚠️ Erro ao usar a chave {chave['chave'][:5]}... tentando a próxima. Erro: {e}")
            continue

    raise Exception("❌ Todas as chaves estão inválidas ou esgotadas.")

def main():
    cx, chaves = carregar_chaves()

    with open(ENTRADAS_POSSIVEIS, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    with open(SAIDAS_RESULTANTES, "w", encoding="utf-8") as saida:
        for i, linha in enumerate(linhas[:2000]):
            consulta = linha.strip()
            print(f"[{i+1}] Pesquisando: {consulta}...")

            try:
                achou = buscar_google(consulta, chaves, cx)
                if achou:
                    msg = f"✅ [{i+1}] ACHOU: {consulta}\n"
                    print("    >> Encontrado!")
                    saida.write(msg)
                    try:
                        playsound(ALERTA_SONORO)
                    except Exception as e:
                        print(f"    ⚠️ Erro ao tocar som: {e}")
                else:
                    print("    >> Nada encontrado.")
            except Exception as e:
                print(f"    ⚠️ ERRO na busca: {e}")

            time.sleep(2)

    salvar_chaves(cx, chaves)
    print("\n📄 Todos os resultados positivos foram salvos em 'resultados_encontrados.txt'.")

if __name__ == "__main__":
    main()
