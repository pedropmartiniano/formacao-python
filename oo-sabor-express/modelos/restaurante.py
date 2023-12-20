from modelos.avaliacao import Avaliacao

class Restaurante():
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self._ativo}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome'.ljust(22)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'- {restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante._ativo}')

    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtde_notas = len(self._avaliacao)

        media = round(soma_notas / qtde_notas, 1)
        return media
