
#Import Time sleep = demorar 2 segundos para o número ir de 1 a 10
# import time

#FINITO 
# for x in range(1,11):
#     print(x)
#     time.sleep(2)


# #TABUADA
# mult = int(input('Multiplicador: '))
# for numero in range(11):
#     calculo = numero * mult
#     print(mult, 'x', numero, '=', calculo)


# #ECOMMERCE
# carrinho = []
# for n in range(3):
#     produto = input('produto: ')
#     carrinho.append(produto)
#     print(carrinho)


# #INFINITO (em sua essência) e FINITO
# while True: #infinito
#     print('infinito')

# contador = 3 #finito
# while contador >= 3:
#     print(contador)
#     contador = contador + 1


# carrinho = []

# desej = input('Deseja comprar? s/n    ')

# while desej == 'sim':
#     p = input("produto:")
#     print(carrinho)
#     desej = input('Deseja comprar? s/n')



#ecommerce & estrutura de dados com loop
ecommerce = {
     
        'celulares':{
             'SAMSUNG':1500.66,
             'IPHONE':3000.0
        },

        'roupas':{
            'camiseta':150.0,
            'calça':250.0

        },
        'acesorios':{
            'relogio':500.0,
            'anel':90.0
        }


}



carrinho = []
valores = [] #criar a lista de valores
deseja = input('deseja comprar? s / n?')
while deseja == 'sim':
    secao = input('SECAO - CELULARES ROUPAS ACESSORIOS')
    p1 = input(F'Produto: {ecommerce[secao]}')
    carrinho.append(p1)
    valores.append(ecommerce[secao][p1])
    print(carrinho)
    total = sum(valores)
    print('R$',total)
    deseja = input('Deseja comprar? s / n?')
else:
    print('Obrigada volte sempre!')   