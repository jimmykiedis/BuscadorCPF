from googlesearch  import search 
import requests
from playsound import playsound
import time

API_KEY = "Sua_API_KEY_aqui"
ARQUIVO_ENTRADA = "possibilidades.txt"
ARQUIVO_SAIDA = "resultados_encontrados.txt"
SOM_ALERTA = "alerta.mp3"

VARIACOES = [
    "todas as variações de nome aqui separados por virgula",
]

def contem_variacao(texto):
    texto = texto.lower()
    return any(variacao in texto for variacao in VARIACOES)

def buscar_google(query):
    cx = "SEU_ID_DO_MECANISMO"  # Crie em https://programmablesearchengine.google.com/
    url = f"https://www.googleapis.com/customsearch/v1"
    
    params = {
        "q": query,
        "key": API_KEY,
        "cx": cx,
        "hl": "pt",
        "num": 10
    }

    response = requests.get(url, params=params)
    data = response.json()

    for item in data.get("items", []):
        titulo = item.get("title", "").lower()
        snippet = item.get("snippet", "").lower()
        if contem_variacao(titulo) or contem_variacao(snippet):
            return True
    return False


def main():
    with open(ARQUIVO_ENTRADA, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as saida:
        for i, linha in enumerate(linhas[:2000]):
            consulta = linha.strip()
            print(f"[{i+1}] Pesquisando: {consulta}...")

            try:
                achou = buscar_google(consulta)
                if achou:
                    msg = f"✅ [{i+1}] ACHOU: {consulta}\n"
                    print("    >> Encontrado!")
                    saida.write(msg)
                    try:
                        playsound(SOM_ALERTA)
                    except Exception as e:
                        print(f"    ⚠️ Erro ao tocar som: {e}")
                else:
                    print("    >> Nada encontrado.")
            except Exception as e:
                print(f"    ⚠️ ERRO na busca: {e}")

            time.sleep(2)  # evitar bloqueio da API

    print("\n📄 Todos os resultados positivos foram salvos em 'resultados_encontrados.txt'.")

if __name__ == "__main__":
    main()
