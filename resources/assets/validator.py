def calcular_digitos_verificadores(cpf9):
    def calc_digito(cpf_parcial, fator_inicial):
        soma = sum(int(d) * f for d, f in zip(cpf_parcial, range(fator_inicial, 1, -1)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    d1 = calc_digito(cpf9, 10)
    d2 = calc_digito(cpf9 + d1, 11)
    return d1 + d2

def gerar_cpfs_validos(meio="***"):
    resultados = []
    for i in range(1000):  # 000 a 999
        prefixo = f"{i:03d}"
        cpf_base = prefixo + meio
        dv = calcular_digitos_verificadores(cpf_base)
        cpf_completo = cpf_base + dv
        resultados.append(cpf_completo)
    return resultados

# Gerar todos os CPFs válidos
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