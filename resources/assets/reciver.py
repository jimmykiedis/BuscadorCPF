from validator import *

class CatchData:
    def __init__(self, cpf_partial: str):
        # Armazena o CPF parcial, usando '*' para dígitos desconhecidos
        self.cpf_partial = cpf_partial

    def get_partial(self):
        return self.cpf_partial

    # Exemplo de método para adicionar um número conhecido
    def set_digit(self, position: int, digit: str):
        cpf_list = list(self.cpf_partial)
        cpf_list[position] = digit
        self.cpf_partial = ''.join(cpf_list)

if __name__ == "__main__":
    cpf_input = input("Digite o CPF parcial (use * para desconhecidos, ex: *6.267.***-*): ")
    cpf = CatchData(cpf_input)
    print("CPF recebido:", cpf.get_partial())

cpfs_possiveis = gerar_cpfs_validos()

# Função para formatar CPF no estilo "XXX.XXX.XXX-YY"
def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
# Função para formatar CPF no estilo "XXX.XXX.XXX-YY"

def formatar_cpf2(cpf):
    return f"{cpf[:3]}{cpf[3:6]}{cpf[6:9]}{cpf[9:]}"

# Salvar os CPFs formatados em um arquivo .txt
with open("possibilidades.txt", "w") as f:
    for cpf in cpfs_possiveis:
        f.write(formatar_cpf(cpf) + " or " + formatar_cpf2(cpf))

print("Os CPFs válidos foram salvos em 'possibilidades.txt'.")

# Exemplo de uso:
# cpf = CatchData("6.267.***-*")
# print(cpf.get_partial())