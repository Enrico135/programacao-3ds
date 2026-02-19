testecalc.py
# Funções para as operações básicas
def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

# Menu de operações
def menu():
    print("Selecione uma operação:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

# Função principal para executar a calculadora
def calculadora():
    while True:
        menu()
        escolha = input("Digite sua escolha (1/2/3/4) ou 'sair' para encerrar: ")

        if escolha == 'sair':
            print("Saindo da calculadora...")
            break

        if escolha not in ['1', '2', '3', '4']:
            print("Opção inválida, tente novamente.")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira números válidos.")
            continue

        if escolha == '1':
            print(f"{num1} + {num2} = {somar(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == '4':
            print(f"{num1} / {num2} = {dividir(num1, num2)}")

# Chama a função principal para rodar a calculadora
calculadora()
