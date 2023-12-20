from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome: str, preco: int, tipo: str, tamanho: str):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho

    def __str__(self) -> str:
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15)