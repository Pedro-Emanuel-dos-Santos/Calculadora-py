# Função para realizar a operação de adição
def adicao(a, b):
    return a + b

# Função para realizar a operação de subtração
def subtracao(a, b):
    return a - b

# Função para realizar a operação de multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a operação de divisão
def divisao(a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    return a / b

# Função principal
def calculadora():
    while True:
        print("Opções:")
        print("Digite '1' para adição")
        print("Digite '2' para subtração")
        print("Digite '3' para multiplicação")
        print("Digite '4' para divisão")
        print("Digite '5' para sair")

        escolha = input("Digite a opção desejada: ")

        if escolha == '5':
            print("Calculadora encerrada.")
            break

        if escolha not in ('1', '2', '3', '4'):
            print("Opção inválida. Tente novamente.")
            continue

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado:", adicao(num1, num2))
        elif escolha == '2':
            print("Resultado:", subtracao(num1, num2))
        elif escolha == '3':
            print("Resultado:", multiplicacao(num1, num2))
        elif escolha == '4':
            print("Resultado:", divisao(num1, num2))

# Chamar a função principal da calculadora
calculadora()
