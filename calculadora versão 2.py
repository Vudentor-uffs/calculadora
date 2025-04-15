while True:  # Loop para reiniciar o programa
    soma = 0
    nota = 1
    quantidade = 0
	#o pai vai fazer um comentário
    total_notas = int(input("\n\033[039mDigite o total de avaliações/notas: \033[36m"))
    if total_notas > 0:
        mda = float(input("\033[039mDigite qual é a média mínima da sua instituição: \033[36m"))
        if mda > 0.0 and total_notas > 0:
            while quantidade < total_notas:  # Loop até digitar todas as notas
                valor = float(input(f"\n\033[039mDigite a \033[36m{nota}ª\033[039m nota: \033[36m"))
                soma += valor
                quantidade += 1
                nota += 1

            media = soma / total_notas
            print(f"\n\033[039mTotal da soma:\033[36m{soma:.2f}\033[039m")
            print("Quantidade de valores digitados:","\033[36m",total_notas,"\033[039m")
            print(f"Média total: \033[36m{media:.2f}\033[039m")

            if media >= mda:
                print("\033[32mParabéns, você passou!\033[039m")
            else:
                print("\033[031mInfelizmente, você está reprovado!\033[039m")

            confirm = input("Deseja continuar? \033[32mS\033[039m|\033[031mN\033[039m:\033[36m ").strip().lower()
            if confirm != 's':
                break
        else:
            print("\033[031mDados inválidos! A média e o número de notas devem ser maiores que zero.\n\033[36mReiniciando programa...\n")
    else:
            print("\033[031mDados inválidos! A média e o número de notas devem ser maiores que zero.\n\033[36mReiniciando programa...\n")
