from abc import ABC, abstractclassmethod

class Veiculo:
    def __init__(self, marca: str, modelo: str) -> None:
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self) -> str:
        return f"{self._marca} | {self._modelo} | {'Ligado' if self._ligado else 'Desligado'}"
    
    @abstractclassmethod
    def ligar(self):
        self._ligado = True

    
class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, portas: int) -> None:
        super().__init__(marca, modelo)
        self._portas = portas

    def __str__(self) -> str:
        return f"{super().__str__()} | {self._portas}"

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, tipo: str) -> None:
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self) -> str:
        return f"{super().__str__()} | {self._tipo}"
    


carro = Carro('Volks', 'Jetta GLI', 4)
moto = Moto('BMW', 'R800', 'Esportiva')

carro.ligar()

print(carro)
print(moto)