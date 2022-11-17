import random

dado = [1, 2, 3, 4, 5, 6]
jogador1 = []
jogador2 = []

contador = 0

while (True):
    print('1. Jogar')
    print('2. Sair')

    entrada = int(input("Digite uma opção: "))

    if entrada == 1:
        rnd = random.choice(dado)
        if contador % 2 == 0:
            print(f'Player 1 tirou {rnd}')
            jogador1.append(rnd)
        else:
            print(f'Player 2 tirou {rnd}')
            jogador2.append(rnd)
    else:
        print('Resultados: ')
        print(f'Jogadas do Player 1: {jogador1}')
        print(f'Jogadas do Player 2: {jogador2}')
        print(f'Soma dos valores do Player 1: {sum(jogador1)}')
        print(f'Soma dos valores do Player 2: {sum(jogador2)}')
        
        if sum(jogador1) > sum(jogador2):
            print('Player 1 é o vencedor')
            print('Obrigada por jogar!')
            break
        elif sum(jogador1) < sum(jogador2):
            print('Player 2 é o vencedor')
            print('Obrigada por jogar!')
            break
        else:
            print('Empate')
            print('Obrigada por jogar!')
            break

    contador += 1