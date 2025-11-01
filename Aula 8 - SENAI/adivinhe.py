import random

#sequencia de números aleatorios entre 1 a 10
numero = random.randrange(1,10)
escolha = int(input('Escolha um número de 1 à 10: '))

if numero == escolha:
    print('Você ganhou o jogo!')
    print('O número aleatório é: ', numero)
else:
    print('Você errou!')
    print('O número aleatório é: ', numero)