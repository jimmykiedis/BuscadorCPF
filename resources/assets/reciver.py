from resources.assets.validator import gerar_cpfs_validos  # certifique-se que gerar_cpfs_validos está aqui
import os

# Diretório base (do script)
BASE_DIR = os.path.dirname(__file__)
SAIDA_POSSIBILIDADES = os.path.abspath(os.path.join(BASE_DIR, '..', '..', 'contents', 'archives', 'possibilidades.txt'))

class CatchData:
    def __init__(self, cpf_partial: str):
        self.cpf_partial = cpf_partial

    def get_partial(self):
        return self.cpf_partial

    def set_digit(self, position: int, digit: str):
        cpf_list = list(self.cpf_partial)
        cpf_list[position] = digit
        self.cpf_partial = ''.join(cpf_list)

# Função para formatar CPF no estilo "XXX.XXX.XXX-YY"
def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# Função para formatar CPF no estilo "XXXXXXXXXYY"
def formatar_cpf2(cpf):
    return f"{cpf[:3]}{cpf[3:6]}{cpf[6:9]}{cpf[9:]}"

if __name__ == "__main__":
    cpf_input = input("Digite o CPF parcial (use * para desconhecidos, ex: *6.267.***-*): ")
    cpf = CatchData(cpf_input)
    print("CPF recebido:", cpf.get_partial())

    cpfs_possiveis = gerar_cpfs_validos()  # usa o input se fizer sentido dentro dessa função

    with open(SAIDA_POSSIBILIDADES, "w", encoding="utf-8") as f:
        for cpf in cpfs_possiveis:
            f.write(f'"{formatar_cpf(cpf)}" OR "{formatar_cpf2(cpf)}"\n')

    print("✅ Os CPFs válidos foram salvos em 'possibilidades.txt'.")
