from typing import Union


class EstatisticaResumida:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: list[str]) -> dict:
        estatistica: dict[str, Union[list[str], str, int]] = {}

        estatistica[f'{self.agencia}-{self.dia}'] = len(clientes_atendidos)

        return estatistica
