# MANIPULAÇÃO DE DIRETÓRIOS
import os
import shutil

# Exercício 1: Criar e ler um Arquivo

# with open('arquivvo', 'w') as novo_arquivo:           #CRIAR ARQUIVO
#     os.mkdir('arquivo_')
    


# with open('arquivvo', 'r') as arquivo:
#     conteúdo = arquivo.read()                               #LER ARQUIVO
#     print(conteúdo)


# Exemplo 2: Cria um Diretório

# with open('q','w') as arq:        #CRIEI A PASTA 'NOVO_ARQUIVO'
#     os.mkdir('novo_arquivo')

# with open('q','w') as arq:
#     os.mkdir('exemplo')           #CRIEI A PASTA 'EXEMPLO'


# Exercício 3: Renomear um Diretório

# os.rename('exemplo', 'novo_exemplo')    #SAIU DE EXEMPLO PARA NOVO EXEMPLO


# Exercício 4:  Listar Arquivos em um Diretório

# with os.scandir('novo_arquivo') as entrada:     #VAI NO DIRETORIO/PASTA "NOVO_ARQUIVO" E ENCONTRA OS ARQUIVOS, LISTANDO ELES NO TERMINAL 
#     for arquivo in entrada:
#         if arquivo.is_file():
#             print(f'Arquivos encontrados: {arquivo.name}')



# Exercício 5:  Copiar Arquivos em um Diretório


# shutil.copytree('novo_arquivo','pasta')


# Exercício 6:  Remover

# shutil.rmtree('arquivo_')         #REMOVI A PASTA 'ARQUIVO_'