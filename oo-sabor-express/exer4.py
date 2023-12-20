class Banco:
    def __init__(self, nome: str, endereco: str) -> None:
        self._nome = nome
        self._endereco = endereco

class Agencia(Banco):
    def __init__(self, nome: str, endereco: str, numero: str) -> None:
        super().__init__(nome, endereco)
        self._numero = numero