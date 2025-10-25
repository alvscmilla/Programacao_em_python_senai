e_commerce = {
    'tenis nike':600.60,
    'camiseta adidas': 250.0,
    'fone': 10.0,
}

print(e_commerce)

carrinho = []
valores = []

produto_1 = input('Digite o nome do produto: ')
produto_2 = input('Digite o nome do produto: ')

carrinho.append(produto_1)
carrinho.append(produto_2)
print(carrinho)

valores.append(e_commerce[produto_1])
valores.append(e_commerce[produto_2])

print('R$', valores)
somar = sum(valores)
print('R$', somar)