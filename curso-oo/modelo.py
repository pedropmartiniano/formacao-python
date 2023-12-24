class Programa:
    def __init__(self, nome, ano) -> None:
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao) -> None:
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{super().__str__()} - {self.duracao} min'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas) -> None:
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{super().__str__()} - {self.temporadas} temps'

class Playlist(list):
    def __init__(self, nome, programas) -> None:
        self.nome = nome
        self._programas = programas

    def __iter__(self):
        return iter(self._programas)

    def __contains__(self, programa):
        return programa in self._programas
    
    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)
    
    @property
    def listagem(self):
        return self._programas
    
    

vingadores = Filme('Guerra infinita', 2018, 160)
atlanta = Serie('Atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
tmep.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

print(atlanta in playlist_fim_de_semana)

print(playlist_fim_de_semana[0])

for programa in playlist_fim_de_semana:
    print(programa)
