pessoas = {
    'Pedro': {
        'nome': 'Pedro',
        'idade': 19,
        'cidade': 'Franca'
    },
    'João': {
        'nome': 'João',
        'idade': 20,
        'cidade': 'Franca'
    },
    'Mariah': {
        'nome': 'Mariah',
        'idade': 16,
        'cidade': 'Franca'
    }
}

pessoas['João']['idade'] = 21

pessoas['Pedro']['profissao'] = 'Dev 😎'

pessoas.pop('João')

print('Existe' if pessoas.get('Pedro') else 'Não existe')

print('-----------------------')

def cont_palavras(frase: str):
    palavras = frase.split(' ')
    frequencia = {}
    for palavra in palavras:
        if frequencia.get(palavra):
            frequencia[palavra] += 1  
        else: 
            frequencia[palavra] = 1

    print(frequencia)

cont_palavras('teste de frase frase')