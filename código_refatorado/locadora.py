class Locadora:
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def gerar_relatorio(self):
        for veiculo in self.veiculos:
            print(f"Veículo: {veiculo.tipo()}, Marca: {veiculo.marca()}")

class CalculoPrecoAluguel:
    def calcular_preco(self, veiculo, dias):
        return veiculo.calcular_preco(dias)
