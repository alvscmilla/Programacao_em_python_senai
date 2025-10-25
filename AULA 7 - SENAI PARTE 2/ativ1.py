# Exercício 0: Escreva um programa que use a função range() para gerar os números pares de 2 a 20 e, em seguida, imprima cada número.

lista = list(range(0, 21, 2))
print(lista)

#Exercício 1: Crie uma lista chamada numeros que contenha os números inteiros de 1 a 10 e imprima-a na tela.
print('---------------------------------------------------------------------------\n')
l = [1,2,3,4,5,6,7,8,9,10]
print(l)

print('\n------------------------------------------------------------------------')
# Exercício 2: Acesse e imprima o terceiro elemento da lista numeros.

print(f''' 
Terceiro número da lista:
{l[3]}\n''')

print('-------------------------------------------------------------------------------\n')
l.append(9)
print(l)

print('---------------------------------------------------------------------------------\n')
del l[5]
print(l)


print('-----------------------------------------------------------------------------\n')


#Exercício 5: Crie uma lista chamada carros contendo três nomes de carros diferentes. Em seguida, concatene essa lista com a lista numeros e imprima o resultado.

list_car = ['Honda','Subaru','Toyota']

l.extend(list_car)
print(l)