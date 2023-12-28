from fila_base import FilaBase
from constantes import COD_PRIORITARIO
from typing import Union
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

Classes = Union[EstatisticaDetalhada, EstatisticaResumida]


class FilaPrioritaria(FilaBase):
    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{COD_PRIORITARIO}{self.codigo}'

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return (f'CLiente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')

    def estatistica(self, retorna_statistica: Classes) -> dict:

        return retorna_statistica.roda_estatistica(self.clientes_atendidos)
