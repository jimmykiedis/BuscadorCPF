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
