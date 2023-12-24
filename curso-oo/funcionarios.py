class Funcionario:
    def __init__(self, nome) -> None:
        self.nome = nome

    def registra_horas(self):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

#  Os mixins são classes herdadas que não precisam ser instanciadas e contém preocupações comuns a diversas classes.
class Hipster: # Mixin (Serve para ter o compartilhamento de algum método apenas herdando essa classe, sem ter que escrever o método; classes assim não são para ser instanciadas)
    def __str__(self) -> str:
        return f'Hipster, {self.nome}'

class Junior(Alura, Hipster):
    pass

# Herança Multipla
class Pleno(Alura, Caelum, Hipster):
    pass

class Senior(Alura, Caelum, Hipster):
    pass


jose = Junior('José')

jose.busca_perguntas_sem_resposta() # Metodo da Alura
jose.registra_horas() # Metodo do Funcionario

print('----------------')

luan = Pleno('José')

luan.busca_perguntas_sem_resposta() # Metodo da Alura
luan.registra_horas() # Metodo do Funcionario
luan.busca_cursos_do_mes() # Metodo do Caelum
luan.mostrar_tarefas() # Sequência de chamada das classes: Pleno > Alura > Caelum > Funcionario (primeiro metodo que encontrar nessa sequência irá ser chamado, no caso será na classe "Alura" pois ela contém o método "mostrar_tarefas")

print('----------------')

pedro = Senior('Pedro')
print(pedro)