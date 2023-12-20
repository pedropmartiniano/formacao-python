from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

praca = Restaurante('Praça', 'Gourmet')
suco = Bebida('Suco de Melancia', 5.0, 'G')
pao = Prato('Paozinho', 2.0, 'O melhor pão da cidade')
chocolate = Sobremesa('Chocolate', 4.0, 'Ao leite', '30g')


praca.add_cardapio(suco)
praca.add_cardapio(pao)
praca.add_cardapio(chocolate)

suco.aplicar_desconto()
pao.aplicar_desconto()
chocolate.aplicar_desconto()

def main():
    praca.exibir_cardapio

if __name__ == '__main__':
    main()