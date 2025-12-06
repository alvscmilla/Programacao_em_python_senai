# CRIE UM BANCO DE DADOS PARA UMA AGENCIA DE MARKETING 

# PRECISA  CADASTRAR OS LEADS DA AGENCIA:

# DADOS: 

# NOME 

# IDADE

# EMAIL 

# ENDEREÇO

# TRABALHO

# GRADUÇÃO

import sqlite3

conn = sqlite3.connect('marketing_database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS dados(
               nome TEXT,
               idade TEXT,
               email TEXT,
               endereco TEXT,
               trabalho TEXT,
               graduacao TEXT                
            )''')
conn.commit()

nome = input('Nome: ')
idade = input('Idade: ')
email = input('E-mail: ')
endereco = input('Endereço: ')
trabalho = input('Trabalho: ')
graduacao = input('Graduação: ')

cursor.execute('INSERT INTO dados VALUES(?,?,?,?,?,?)',(nome, idade, email, endereco, trabalho, graduacao))
conn.commit()

cursor.execute('SELECT * FROM dados')
dados = cursor.fetchall()
print(dados)

conn.close