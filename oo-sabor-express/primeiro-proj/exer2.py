numeros = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]

for num in numeros:
    print(num)

soma = 0
for i in range(10):
    if i % 2 != 0:
        soma += i

print(soma)

for i in range(10, 0, -1):
    print(i)

num = int(input('Digite um número: '))

for i in range(0, 11):
    print(f'{num} x {i}: {num * i}')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0
for num in lista:
    try:
        soma += num
    except:
        print('Não é um número')

print(f'soma dos valores da lista: {soma}')

try:
    media = soma/len(lista)
    print(f'média dos valores da lista: {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possivel fazer a média')

credenciais_clientes = {
    'alice123': {'username': 'alice123', 'password': 'alic3P@ssw0rd', 'status': 'active'},
    'bob456': {'username': 'bob456', 'password': 'b0bP@ssword!', 'status': 'inactive'},
    'charlie789': {'username': 'charlie789', 'password': 'Ch@rlieP@ss9', 'status': 'active'}
}

print(credenciais_clientes['bob456']['status'])