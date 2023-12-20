from modelos.restaurante import Restaurante

praca = Restaurante('Praça', 'Gourmet')

praca.receber_avaliacao('Gui', 10)
praca.receber_avaliacao('Lais', 8)
praca.receber_avaliacao('Emy', 5)

Restaurante.listar_restaurantes()

def main():
    pass

if __name__ == '__main__':
    main()