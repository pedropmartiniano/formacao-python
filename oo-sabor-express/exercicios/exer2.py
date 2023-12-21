class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return f'{self._nome} | {self._idade} | {self._profissao}'

    def aniversario(self):
        self._idade += 1

    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá, sou {self._nome}! Trabalho como {self._profissao}'
        else:
            return f'Olá, sou {self._profissao}'
        
joao = Pessoa('João', 19, 'Carpinteiro')

joao.aniversario()

print(joao)

print(joao.saudacao)

print('(----------------)')

class ContaBancaria:
    cont_contas = 0
    def __init__(self, titular: str, saldo: int) -> None:
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
        ContaBancaria.cont_contas += 1

    def __str__(self) -> str:
        return f'Titular: {self._titular}, saldo: {self._saldo}'
    
    def ativar_conta(self) -> None:
        self._ativo = True

    @property
    def titular(self):
        return f'{self._titular}'
    
    @classmethod
    def qtde_contas(cls):
        return f'Quantidade de contas no banco: {cls.cont_contas}'
    

conta01 = ContaBancaria('João', 900)
conta02 = ContaBancaria('Pedro', 1000)

print(conta01)
print(conta02)

conta02.ativar_conta()

print(conta02._ativo)

print(ContaBancaria.qtde_contas())