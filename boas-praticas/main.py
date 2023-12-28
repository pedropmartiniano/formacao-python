from fila_normal import FilaNormal

fila_teste = FilaNormal()

fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()

print(fila_teste.chama_cliente(5))
print(fila_teste.chama_cliente(7))

print('-----------------------')

from fila_prioritaria import FilaPrioritaria

fila_teste_2 = FilaPrioritaria()

fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()

print(fila_teste_2.chama_cliente(10))
print(fila_teste_2.chama_cliente(1))

print('-----------------------')

from fabrica_fila import FabricaFila
from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida

teste_fabrica = FabricaFila.pega_fila('prioritaria')

teste_fabrica.atualiza_fila()

print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.estatistica(EstatisticaDetalhada('28/12/2023', 120)))
