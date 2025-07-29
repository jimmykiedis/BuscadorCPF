
print('Bem vindos ao sistema de busca de CPF no google!\n')
print('Nota: Esse programa usa a API do Google para buscar CPF, portanto adaquira as suas chaves no site deles.\n')

resposta = input("Você é usuário premium da plataforma do googlesearch? (sim/não): ").strip().lower()
match resposta:
    case "sim":
        print("Segue o curso normal do código...")
    case "não":
        print("Segue o fluxo da gambiarra")
    case _:
        print("❓ Resposta inválida. Por favor, digite 'sim' ou 'não'.")