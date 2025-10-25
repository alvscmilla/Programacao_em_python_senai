# inserir
lista  =  [] # LISTA VAZIA*** 

# append  -  inserir um dado
lista.append(10)

# extend  -  varios dados de uma vez
lista.extend([10,30,3010,30,30])

# (+=) -  inseri varios dados tb
lista +=(10,30,30,10,30,30)

# insert -  inserir na posição que você quiser
lista.insert(0,1500)

print(lista)


print(lista)
#remover

lista.remove(10)

#del - remove por indice
del lista[0]
print(lista)

#pop() - remove o último valor
lista.pop()
print(lista)

#pop(com indice) - remove o indice que voce deseja
lista.pop(2)
print(lista)


#verificar

#tamanho - len
print(len(lista))


#somar os números das listas (se for numeros)
print(sum(lista))


#max() - maior número da lista
maior = max(lista)
print(maior)

#min() - menor numero da lista
menor = min(lista)
print(menor)

#count() - quantidade de algum dado especifico dentro da lista
print(lista.count(30))

#sort() - ordenar do menor para o maior
lista.sort(reverse = True) # maior para o menor
lista.sort() #menor para o maior
print(lista)

#copy() - copia a lista
copia = lista.copy()
print(copia)

#clear() - limpa a lista
lista.clear()
print(lista)