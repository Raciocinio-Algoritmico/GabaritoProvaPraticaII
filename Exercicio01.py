def criaLista(tamanho):
    return [0] * tamanho

tamanho = int(input('Qual tamanho você deseja criar a lista? '))
lista = criaLista(tamanho)

for i in range(len(lista)):
    lista[i] = int(input('Digite um valor inteiro qualquer: '))

print(f'Valores na ordem digitada: {lista}')
print(f'Valores na ordem inversa: {list(reversed(lista))}')
print(f'Valores em ordem crescente: {sorted(lista)}')
print(f'A soma dos valores é {sum(lista)}')
print(f'O maior valor é {max(lista)}')
print(f'O menor valor é {min(lista)}')