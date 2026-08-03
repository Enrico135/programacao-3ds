class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return (
            f"Livro: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Número de páginas: {self.paginas}"
        )


# Entrada de dados
titulo = input("Digite o título do livro: ")
autor = input("Digite o autor do livro: ")
paginas = int(input("Digite a quantidade de páginas: "))

# Criação do objeto
livro = Livro(titulo, autor, paginas)

# Saída de dados
print("\nDescrição do livro:")
print(livro)
