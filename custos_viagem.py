class Veiculo:
    def custo_viagem(self, km):
        pass


class Carro(Veiculo):
    def custo_viagem(self, km):
        return km * 0.50


class Moto(Veiculo):
    def custo_viagem(self, km):
        return km * 0.30


class Caminhao(Veiculo):
    def custo_viagem(self, km):
        return km * 0.80


def custo_total(lista_veiculos):
    total = 0
    for veiculo in lista_veiculos:
        total += veiculo.custo_viagem(200)
    return total


veiculos = [Carro(), Moto(), Caminhao()]
print("Custo total da viagem:", custo_total(veiculos))
