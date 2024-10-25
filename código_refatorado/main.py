from locadora import Locadora, CalculoPrecoAluguel
from veiculo import Carro, Moto, Caminhao

locadora = Locadora()
locadora.adicionar_veiculo(Carro("Ford"))
locadora.adicionar_veiculo(Moto("Honda"))
locadora.adicionar_veiculo(Caminhao("Mercedes"))

preco_calculador = CalculoPrecoAluguel()

# Cálculo de preço
for veiculo in locadora.veiculos:
    preco = preco_calculador.calcular_preco(veiculo, dias=3)
    print(f"Aluguel de 3 dias do {veiculo.tipo()} ({veiculo.marca()}): R${preco}")

# Geração de relatório
locadora.gerar_relatorio()
