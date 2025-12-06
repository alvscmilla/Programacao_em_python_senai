import sqlite3

conn = sqlite3.connect('database.db') #open archive 
cursor = conn.cursor() #chama cursor

cursor.execute('''CREATE TABLE IF NOT EXISTS dados(
               
               nome TEXT,
               email TEXT,
               idade idade TEXT 
               )''')
conn.commit() #save, atualizar



nome = input('nome: ')
email = input('e-mail: ')
idade = input('idade: ')



#inserir dados nas tabelas: NOME, EMAIL, IDADE
cursor.execute('INSERT INTO dados VALUES(?,?,?)',(nome, email, idade))
conn.commit()


#SELECIONAR TUDO 
cursor.execute('SELECT * FROM dados')
dados = cursor.fetchall() #traz os daddos do banco
print(dados)

conn.close()