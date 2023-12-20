from abc import ABC, abstractclassmethod

class ItemCardapio:
    def __init__(self, nome: str, preco: int):
        self._nome = nome
        self._preco = preco
    
    @abstractclassmethod
    def aplicar_desconto(self):
        pass