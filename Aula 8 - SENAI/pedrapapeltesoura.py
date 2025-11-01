import random 

#números aleatórios de 1 até 10.
# n = random.randint(1,10)
# print(n)

ppt_maquina = ['🪨','✂️','📄']
ppt_jogador = ['🪨','✂️','📄']

#o random escolhe um dos emojis aleatoriamente
aleatorio = random.choice(ppt_maquina)
escolha = int(input('''
0 - 🪨
1 - ✂️
2 - 📄  
ESCOLHA: '''))

#se computador escolher o mesmo que o jogador = empate
if aleatorio == ppt_jogador[escolha]:
    print('EMPATE!')
    print('Maquina escolheu: ', aleatorio)
    print('Você escolheu: ', ppt_jogador[escolha])

#se computador escolher papel e jogador pedra = computador ganhou
elif aleatorio == '📄' and ppt_jogador[escolha] == '🪨':
    print('O computador ganhou! ')
    print('A maquina escolheu: ', aleatorio)
    print('Você escolheu: ', ppt_jogador[escolha])

#se computador escolher pedra e jogador tesooura = computador ganhou
elif aleatorio == '🪨' and ppt_jogador[escolha] == '✂️':
    print('O computador ganhou! ')
    print('A maquina escolheu: ', aleatorio)
    print('Você escolheu: ', ppt_jogador[escolha])

#se computador escolher tesoura e jogador pedra = computador ganhou
elif aleatorio == '✂️' and ppt_jogador[escolha] == '📄':
     print('O computador ganhou! ')
     print('A maquina escolheu: ', aleatorio)
     print('Você escolheu: ', ppt_jogador[escolha])


# jogador: papel e computador: pedra = jogador ganha
elif  ppt_jogador[escolha] == '🧻'  and  aleatorio == '🪨':
    print('Você ganhou!')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha])    

# jogador: pedra e computador: tesoura = jogador ganha
elif ppt_jogador[escolha] == '🪨'  and   aleatorio == '✂️':
    print('Você ganhou!')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha]) 

# jogador: tesoura e computador: papel = jogador ganha
elif ppt_jogador[escolha] == '✂️'  and   aleatorio  == '🧻':
    print('Você ganhou!')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha]) 
