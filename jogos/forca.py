def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False
    
    letras = '_ ' * len(palavra_secreta)
    arr_letra = letras.split(' ')
    arr_letra.pop()

    tentativas = len(palavra_secreta) * 2

    while(not enforcou and not acertou):
        print('Jogando...')

        print(f'Tentativas restantes: {tentativas}')

        print(arr_letra)
        chute = input('Qual letra deseja chutar? ').strip().lower()

        for i, letra in enumerate(palavra_secreta):
            if(chute == letra):
                arr_letra[i] = letra
                print('Acertou uma letra!!!')

        if not '_' in arr_letra:
            acertou = True
        
        tentativas -= 1

        if(tentativas == 0):
            enforcou = True
        

        
    if(acertou):
        print('Parabéns, você ganhou!')
    else:
        print('Você perdeu.')

    print(f'A palavra era {palavra_secreta}')
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()