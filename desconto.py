# Solicita o preço do produto
preco = float(input("Digite o preço do produto: R$ "))

# Solicita o código de desconto
codigo_desconto = input("Digite o código de desconto (A, B ou C): ").upper()

# Aplica o desconto com base no código fornecido
if codigo_desconto == 'A':
    # Desconto de 10%
    desconto = preco * 0.10
elif codigo_desconto == 'B':
    # Desconto de 15%
    desconto = preco * 0.15
elif codigo_desconto == 'C':
    # Desconto de 20%
    desconto = preco * 0.20
else:
    # Caso o código não seja válido
    print("Código de desconto inválido!")
    desconto = 0

# Calcula o preço final
preco_final = preco - desconto

# Exibe o preço final
if desconto > 0:
    print(f"Preço original: R$ {preco:.2f}")
    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")
