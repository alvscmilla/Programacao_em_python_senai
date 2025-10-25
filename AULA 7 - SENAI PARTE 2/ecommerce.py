print('\n---------------------------E-COMMERCE------------------------------------------')


#CARRINHO DA PESSOA 
carrinho = [] 
carrinho_total = []


#LISTA
lista_produtos = [' ','HD','SSD', 'MEMORIA RAM', 'IPHONE 17','COMPUTADOR']

valores_produtos = [0,450.0,530.99, 700.0, 9000.99, 5000.0]

#PERMITE OLHAR A LISTA DE PRODUTOS E CONCATENAR COM A LISTA DE VALORES
print(f'''
{lista_produtos[1]} R$ - {valores_produtos[1]}
{lista_produtos[2]} R$ - {valores_produtos[2]}
{lista_produtos[3]} R$ - {valores_produtos[3]}
{lista_produtos[4]} R$ - {valores_produtos[4]}
{lista_produtos[5]} R$ - {valores_produtos[5]}\n
CASO NÃO QUEIRA ADICIONAR UM ITEM AO CARRINHO, DIGITE 0
''')

#VARIÁVEIS QUE VÃO ESCOLHER O PRODUTO DA LISTA
produto_1 = int(input('ID DO PRODUTO: '))
produto_2 = int(input('ID DO PRODUTO: '))
produto_3 = int(input('ID DO PRODUTO: '))

#ADICIONA ITENS(EX:PRODUTO_1, QUE É A ID ESCOLHIDA) AO CARRINHO VAZIO
carrinho.append(lista_produtos[produto_1])
print("você inseriu no seu carrinho:  ", carrinho)
#ADICIONA O VALOR TOTAL DOS PRODUTOS AO TOTAL DO CARRINHO(VAZIO)
carrinho_total.append(valores_produtos[produto_1])
print('R$', sum(carrinho_total))

carrinho.append(lista_produtos[produto_2])
print("Você inseriu no seu carrinho: ", carrinho)
carrinho_total.append(valores_produtos[produto_2])
print('R$', sum(carrinho_total))

carrinho.append(lista_produtos[produto_3])
print("Você inseriu no seu carrinho: ", carrinho)
carrinho_total.append(valores_produtos[produto_3])
print('R$', sum(carrinho_total))


#TOTAL DO PEDIDO
print('---------------------------------------------------------\n')
print('Seu pedido ficou R$', sum(carrinho_total))
print('\n--------------------------------------------------------')


#LISTA PARA A FORMA DE PAGAMENTO
forma_pag = [' ', '1 - PIX', '2 - CARTÃO DE CRÉDITO', '3 - CARTÃO DE DÉBITO']
print(f'''
{forma_pag[1]}
{forma_pag[2]}
{forma_pag[3]}
''')

#ESCOLHER A FORMA DE PAGAMENTO  
pag = int(input("ESCOLHA A FORMA DE PAGAMENTO A PARTIR DO ID: "))
#MOSTRAR A FORMA DE PAGAMENTO 
print(f'''Sua forma de pagamento é: {forma_pag[pag]}

Obrigada, volte sempre!
\n------------------------------------------------------------------------
''')
