# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()


# o que a estrutura(sintaticamente)? para que serve(contexto)? 
# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/
# 1 - cita a estrutura de código
# 2 - contextualiza 




largura, altura = 400, 400     #duas variáveis: largura e altura
tela = pygame.display.set_mode((largura, altura))       #display do jogo, usando o tamanho e largura para definir
pygame.display.set_caption("Labirinto")                 #nome


#cores pré definida 
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

#array para definir os "quadradinhos" do labirinto.  Utilizando coluna e tabela: 1,0,0,0,0,0,1.
tamanho_celula = 40
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#ajuda
x, y = 1 * tamanho_celula, 1 * tamanho_celula
velocidade = 40           #velocidade do bloco vermelho


#método encapsulado para "desenhar" o labirinto, moldando ele.
def desenhar_labirinto():
    for linha in range(len(labirinto)):       #lê a array, especificamente as linhas.
        for coluna in range(len(labirinto[linha])):    #lê a array novamente, dessa vez as colunas     
            cor = preto if labirinto[linha][coluna] == 1 else branco     #pinta de preto, se a coluna e labirinto for igual à 1. Senão, pinta de branco. 
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))     #chama a função "draw" e "rect" do import 'pygame', 

#executando o código, para abrir a tela dele e fechar
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False



#funcionamento do jogo, utilizando o teclado
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y

#pintar de branco
    tela.fill(branco)

#chama o método para desenhar a "bolinha vermelha"
    desenhar_labirinto()
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

#atualizar??
    pygame.display.flip()

#ajuda
    pygame.time.Clock().tick(10)

#ajuda
pygame.quit()
