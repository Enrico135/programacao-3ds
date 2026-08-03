class Animal:
    def __init__(self, nome):
        self.nome = nome

    def dados(self):
        return f"Animal: {self.nome}"


class Cachorro(Animal):
    def dados(self):
        return f"Cachorro: {self.nome}"


class Gato(Animal):
    def dados(self):
        return f"Gato: {self.nome}"


tipo = input("Digite o tipo (cachorro/gato): ").lower()
nome = input("Nome do animal: ")

if tipo == "cachorro":
    animal = Cachorro(nome)
else:
    animal = Gato(nome)

print("\nCadastro realizado!")
print(animal.dados())
