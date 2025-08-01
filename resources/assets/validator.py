import itertools

def calcular_digitos_verificadores(cpf9):
    def calc_digito(cpf_parcial, fator_inicial):
        soma = sum(int(d) * f for d, f in zip(cpf_parcial, range(fator_inicial, 1, -1)))
        resto = soma % 11
        return '0' if resto < 2 else str(11 - resto)

    d1 = calc_digito(cpf9, 10)
    d2 = calc_digito(cpf9 + d1, 11)
    return d1 + d2

def validar_cpf(cpf11):
    if len(cpf11) != 11 or not cpf11.isdigit():
        return False
    cpf9 = cpf11[:9]
    dig_verif = cpf11[9:]
    return calcular_digitos_verificadores(cpf9) == dig_verif

def gerar_cpfs_validos(cpf_parcial):
    cpf_parcial = cpf_parcial.replace(".", "").replace("-", "")
    if len(cpf_parcial) != 11:
        raise ValueError("CPF parcial deve ter 11 caracteres (dígitos ou '*').")

    if "*" not in cpf_parcial:
        # Sem curinga, valida direto e retorna só se válido
        if validar_cpf(cpf_parcial):
            return [cpf_parcial]
        else:
            return []

    indices = [i for i, c in enumerate(cpf_parcial) if c == "*"]
    possibilidades = itertools.product("0123456789", repeat=len(indices))

    cpfs_possiveis = []
    for p in possibilidades:
        cpf_lista = list(cpf_parcial)
        for i, val in zip(indices, p):
            cpf_lista[i] = val
        cpf_tentativa = "".join(cpf_lista)
        cpf9 = cpf_tentativa[:9]
        dv = calcular_digitos_verificadores(cpf9)
        cpf_completo = cpf9 + dv
        if cpf_completo == cpf_tentativa:
            cpfs_possiveis.append(cpf_completo)

    return cpfs_possiveis

# --- Teste rápido ---

