from typing import Union


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: list[str]) -> dict:
        estatistica: dict[str, Union[list[str], str, int]] = {}

        estatistica['dia'] = self.dia
        estatistica['agencia'] = self.agencia
        estatistica['clientes_atendidos'] = clientes_atendidos
        estatistica['qtde_clientes_atendidos'] = len(clientes_atendidos)

        return estatistica
