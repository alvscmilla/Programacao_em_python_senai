# # Sinais aritméticos
# # + - * / // % **
print("-----------------------SINAIS ARITMÉTICOS---------------------------------------------")
n1 = 10 
n2 = 20

print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)
print(n1 // n2)
print(n1 % n2)
print(n1** n2)

print("------------------------------TRUE OR FALSE----------------------------------------------------")
n1 = 10 
n2 = 2 
print(n1 > n2) #maior
print(n1 < n2) #menor
print (n1 >= n2) #maior ou igual
print(n1 <= n2) #menor ou igual
print(n1 != n2) #diferente
print(n1 == n2) #igual

print("-----------------------------------INPUT AND OUTPUT-----------------------------------------------------")
#print() = output --- saída
#input() = input --- entrada

name = input('Digite seu nome: ')

#o INPUT naturalmente gera um texto
n1 = input("Digite um número: ")
n2 = input("Digite outro número: ")
print(n1 + n2)

#para transformar em um dado = "int" or "float"
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
print(n1 + n2)

print("------------------------------------------CONCATENAÇÃO-----------------------------------------------------------")
#concatenação = juntar dados

name = input('Digite seu nome: ')
age = int(input('Digite sua idade: '))
endereco = input("Digite seu endereço: ")
curso = input("Curso: ")
salario = float(input("Digite seu salario: "))

print('-----------------------------------------')
#concatenar
print('Nome: ', name)
print('Idade: ', age)
print('Endereço: ', endereco)
print('Curso: ', curso)
print('Salario', salario)

# #maneiras de concatenar
# print('nome', name)
# print('nome' + ' ' +name) #não consegue concatenar usando int, precisa usar a virgula(,).
# print(f'Nome {name}')
# print('Nome {}'.format(name))
# print('Nome %s')


#maneiras de pular linha:
# print()
# f''' '''
# \n

# f'''  sdfsdfhsdlfsdf  {}''' cerquilha 
# print(f'''
# Nome {nome}
# Idade {idade}
# Endereço {endereco}
# Curso {curso}
# Salario {salario}          
# ''')
# \n
# print('Nome\n', nome, 'idade\n',idade)





