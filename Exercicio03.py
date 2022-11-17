def criaMatriz(linhas, colunas):
    matriz = []

    for i in range(linhas):
        listaLinhas = []
        for j in range(colunas):
            listaLinhas.append(0)
            
        matriz.append(listaLinhas)

    return matriz

linhas = int(input('Quantas linhas deve ter a matriz? '))
colunas = int(input('Quantas colunas deve ter a matriz? '))

matriz = criaMatriz(linhas, colunas)

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = int(input('Digite um valor inteiro qualquer: '))

maior = matriz[0][0]
menor = matriz[0][0]
pares = 0
impares = 0

for i in range(0, linhas):
    for j in range (0, colunas):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
        
        if matriz[i][j] < menor:
            menor = matriz[i][j]

        if matriz[i][j] % 2 == 0:
            pares += 1
        else:
            impares += 1

print('Matriz original: ')
for linha in matriz:
    print(linha)

print(f'Quantidade de valores pares: {pares}')
print(f'Quantidade de valores ímpares: {impares}')
print(f'Maior valor da matriz: {maior}')
print(f'Menor valor da matriz: {menor}')