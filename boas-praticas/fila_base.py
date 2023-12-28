from abc import ABCMeta, abstractmethod
from constantes import TAMANHO_FILA_MAX, TAMANHO_FILA_MIN


class FilaBase(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.codigo: int = 0
        self.fila: list[str] = []
        self.clientes_atendidos: list[str] = []
        self.senha_atual: str = ''

    def reseta_fila(self) -> None:
        if self.codigo >= TAMANHO_FILA_MAX:
            self.codigo = TAMANHO_FILA_MIN
        else:
            self.codigo += 1

    def inserir_cliente(self):
        self.fila.append(self.senha_atual)

    @abstractmethod
    def gera_senha_atual(self):
        ...

    def atualiza_fila(self):
        self.reseta_fila()
        self.gera_senha_atual()
        self.inserir_cliente()

    @abstractmethod
    def chama_cliente(self, caixa: int):
        ...
