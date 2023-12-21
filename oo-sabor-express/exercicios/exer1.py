class Carro:
    def __init__(self, modelo: str, cor: str, ano: int):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

corolla = Carro('Corolla', 'preto', '2009')

class Restaurante:
    def __init__(self, nome: str, categoria: str, cidade: str):
        self.nome = nome
        self.categoria = categoria
        self.cidade = cidade
        self.ativo = False

    def __str__(self):
        return f'{self.nome} | {self.categoria | {self.ativo}}'

plaza = Restaurante('Plaza', 'Gourmet','São Paulo')