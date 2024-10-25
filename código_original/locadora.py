class Locadora:
    def __init__(self):
        self.veiculos = []

    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)

    def calcular_preco(self, tipo, dias):
        if tipo == "carro":
            return dias * 100
        elif tipo == "moto":
            return dias * 50
        elif tipo == "caminhao":
            return dias * 200
        else:
            raise ValueError("Tipo de veículo desconhecido")

    def gerar_relatorio(self):
        for veiculo in self.veiculos:
            print(f"Veículo: {veiculo['tipo']}, Marca: {veiculo['marca']}")

