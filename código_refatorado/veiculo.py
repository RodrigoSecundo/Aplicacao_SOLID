from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def calcular_preco(self, dias):
        pass

    @abstractmethod
    def tipo(self):
        pass

    @abstractmethod
    def marca(self):
        pass

class Carro(Veiculo):
    def __init__(self, marca):
        self._marca = marca

    def calcular_preco(self, dias):
        return dias * 100

    def tipo(self):
        return "Carro"

    def marca(self):
        return self._marca

class Moto(Veiculo):
    def __init__(self, marca):
        self._marca = marca

    def calcular_preco(self, dias):
        return dias * 50

    def tipo(self):
        return "Moto"

    def marca(self):
        return self._marca

class Caminhao(Veiculo):
    def __init__(self, marca):
        self._marca = marca

    def calcular_preco(self, dias):
        return dias * 200

    def tipo(self):
        return "Caminhão"

    def marca(self):
        return self._marca
