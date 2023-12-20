from exer3 import Livro

livro_novo = Livro('teste', 'opa', 2001)

livro_novo.emprestar()

print(livro_novo)

print(Livro.verificar_disponibilidade(2001))