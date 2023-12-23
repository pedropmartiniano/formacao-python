import os

restaurantes = [
    {'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False}, 
    {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
    {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]

def exibir_nome_do_programa():
    print('Sabor Express\n')

def exibir_opcoes():
    print('1. cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('opcao inválida!')
    voltar_ao_menu()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs:
    - Nome do restaurante(str)
    - Categoria(str)

    Output:
    - Adiciona um novo restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'O restaurante: {nome_restaurante}, foi cadastrado com sucesso!\n')
    voltar_ao_menu()


def listas_restaurantes():
    exibir_subtitulo('Listando os Restaurantes')
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nm_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nm_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu()

def estado_restaurante():
    exibir_subtitulo('Alternando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if(nome_restaurante == restaurante['nome']):
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    else:
        print(mensagem)


    voltar_ao_menu()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listas_restaurantes()
        elif opcao_escolhida == 3:
            estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def escolher_opcao_match():
    opcao_escolhida = int(input('Escolha uma opção: '))

    match opcao_escolhida:
        case 1:
            print('Cadastrar restaurante')
        case 2:
            print('Listar restaurantes')
        case 3:
            print('Ativando restaurante')
        case 4:
            finalizar_app()
        case _:
            print('Opção inválida!')

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()

