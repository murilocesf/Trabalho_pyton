print("Bem vindo ao catálogo automotivo!")

lista_veiculos = []
lista_ano = []
lista_motor = []

while True:
    print("\nMenu:")
    print("1. Adicionar veículo")
    print("2. Visualizar catálogo")
    print("3. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        veiculo = input("Insira o veículo: ")
        lista_veiculos.append(veiculo)

        ano = int(input("Insira o ano do veículo: "))
        lista_ano.append(ano)

        motor = float(input("Insira o valor do motor do veículo: "))
        lista_motor.append(motor)

    elif opcao == 2:
        print("\nCatálogo de Veículos:")
        for i in range(len(lista_veiculos)):
            print(f"Veículo: {lista_veiculos[i]}, Ano: {lista_ano[i]}, Motor: {lista_motor[i]}")

    elif opcao == 3:
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")