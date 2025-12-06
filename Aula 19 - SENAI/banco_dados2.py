import sqlite3


conn  = sqlite3.connect('meu_banco.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS dados(
                
                nome TEXT,
                email TEXT,
                idade TEXT
                
               
               )''')
conn.commit()


nome  =  input('nome: ')
idade  =  input('idade: ')
email = input('e-mail:')


cursor.execute('INSERT INTO dados VALUES(?,?,?)', (nome, email,idade))
conn.commit()


cursor.execute('SELECT * FROM dados')
dados  =  cursor.fetchall()
print(dados)



conn.close()