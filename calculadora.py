
def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação desejada (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"Resultado: {num1 + num2}")
        elif escolha == '2':
            print(f"Resultado: {num1 - num2}")
        elif escolha == '3':
            print(f"Resultado: {num1 * num2}")
        elif escolha == '4':
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Erro: Divisão por zero não é permitida.")
    else:
        print("Opção inválida. Tente novamente.")

calculadora()