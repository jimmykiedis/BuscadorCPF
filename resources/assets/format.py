def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# Função para formatar CPF no estilo "XXXXXXXXXYY"
def formatar_cpf2(cpf):
    return f"{cpf[:3]}{cpf[3:6]}{cpf[6:9]}{cpf[9:]}"
