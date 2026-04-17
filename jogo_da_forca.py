import os

palavra_secreta = "girafa".lower()
# Usando count para preparar a visualização inicial
letras_acertadas = "_" * len(palavra_secreta) 
tentativas_restantes = 6
letras_tentadas = ""

# Lista com os estágios do desenho (6 partes do corpo)
forca_visual = [
    "  +---+\n  |   |\n      |\n      |\n      |\n      |",      # 0 erros
    "  +---+\n  |   |\n  O   |\n      |\n      |\n      |",      # 1 erro: Cabeça
    "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |",      # 2 erros: Tronco
    "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |",      # 3 erros: Braço Esquerdo
    "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |",     # 4 erros: Braço Direito
    "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |",     # 5 erros: Perna Esquerda
    "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |"      # 6 erros: Perna Direita
]

while tentativas_restantes > 0 and "_" in letras_acertadas:
    # Mostra o desenho atual baseado no número de erros (6 - tentativas)
    erros = 6 - tentativas_restantes
    print(forca_visual[erros])
    print(f"\nPalavra: {' '.join(letras_acertadas)}")
    print(f"Letras já testadas: {letras_tentadas}")

    palpite = input("Digite uma letra: ").strip().lower()

    # Validação para não repetir letra ou digitar vazio
    if len(palpite) != 1 or not palpite.isalpha():
        print("Entrada inválida! Digite apenas uma letra.")
        continue
    
    if palpite in letras_tentadas:
        print(f"Você já tentou a letra '{palpite.upper()}'.")
        continue

    letras_tentadas += palpite + " "

    # Usando find() para verificar se a letra existe
    if palavra_secreta.find(palpite) != -1:
        print(f"Boa! A letra '{palpite.upper()}' existe.")
        
        # Atualizando a string de acertos
        nova_letras_acertadas = ""
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == palpite:
                nova_letras_acertadas += palpite
            else:
                nova_letras_acertadas += letras_acertadas[i]
        letras_acertadas = nova_letras_acertadas
    else:
        tentativas_restantes -= 1
        print(f"Erro! A letra '{palpite.upper()}' não existe.")

# Resultado Final
if "_" not in letras_acertadas:
    print(f"\nPARABÉNS! Você acertou: {palavra_secreta.upper()}")
else:
    print(forca_visual[6]) # Mostra a forca completa no erro final
    print(f"\nQUE PENA! Você foi enforcado. A palavra era: {palavra_secreta.upper()}")
