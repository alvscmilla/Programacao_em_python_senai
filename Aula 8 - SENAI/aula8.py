#condição simples

# idade = int(input('Qual a sua idade? '))

# if idade >= 18:
#     print("Pode dirigir")


# #condição composta 
# idade = int(input('Qual a sua idade? '))

# if idade >= 18:
#     print("Pode dirigir")
# else:                                       #else não tem condição (ex: idade >= 18)
#     print('Você não pode dirigir.')


# #condicional composta
# idade = int(input('Qual a sua idade? '))
# carteira = input('Possui carteira? ')

# if idade >= 18 and carteira == 'sim':
#     print("Maior de idade e pode dirigir")
# elif idade >= 18:
#     print('Pode dirigir, mas não tem carteira')
# else:                                       
#     print('Você não pode dirigir.')

estoque = {
    'frutas':{
        'uvas':
              {'quantidade':30,
               'preço':10.55,
               },
        'bananas':{
                'quantidade':20,
                'preço':15.25

        },
     
        },
    'eletronicos':{
        'fone':{
                'quantidade':10,
                'preço':500.55
        },
        'iphone':{
                'quantidade':5,
                'preço':17000
        }

    }
    
    }


carrinho =  []
total =  []

senha =  '123'
login = '@mi'

dig_senha =  input('Digite sua senha: ')
dig_login =  input('Digite seu login: ')

if dig_login == login and dig_senha == senha:
    print('Seja bem vindo(a))')
    pedir  =  input('Deseja fazer o pedido: sim ou não? ')
    if pedir == 'sim':
        print('estoque: escolha seu produto: ')
        secao = input('Digite a seção -  frutas ou eletrônicos: ')
        produto =  input(f'escolha o produto: {estoque[secao]} ')
        print('Produto:', estoque[secao][produto])
        carrinho.append(produto)
        total.append(estoque[secao][produto]['preço'])
        
        estoque[secao][produto]['quantidade'] - 1
        print(estoque)

        print('Carrinho', carrinho)
        print('R$', total)
        print('------------------------')
        formapag = print(['1 PIX', '2 - CC', '3 - CD'])
        pag =  int(input('Digite a forma de pagamento: '))
        print('FORMA DE PAGAMENTO', formapag[pag])

    else:
        print('Obrigada volte sempre')    
else:
    print('Algo foi digitado errado... tente novamente')    