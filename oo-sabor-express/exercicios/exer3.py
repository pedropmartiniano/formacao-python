class Livro:
    livros = []
    def __init__(self, titulo: str, autor: str, ano: int) -> None:
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self) -> str:
        return f"{self._titulo} | {self._autor} | {self._ano_publicacao} | {'Disponível' if self._disponivel else 'Indisponível'}"
    
    def emprestar(self) -> None:
        self._disponivel = False

    @classmethod
    def verificar_disponibilidade(cls, ano: int):
        # for livro in cls.livros:
        #     if ano == livro._ano_publicacao:
        #         livros_disponiveis.append(livro._titulo)

        livros_disponiveis = ([livro._titulo for livro in cls.livros if livro._ano_publicacao == ano and livro._disponivel])

        return livros_disponiveis


livro1 = Livro('A trança da vovó careca', 'Adam Sandler', 2000)
livro2 = Livro('A trança da vovó careca 2', 'Adam Sandler', 2000)
livro3 = Livro('A trança da vovó careca 3', 'Adam Sandler', 2000)
livro4 = Livro('A trança da vovó careca 4', 'Adam Sandler', 2001)

# print(livro1)

print(Livro.verificar_disponibilidade(2000))