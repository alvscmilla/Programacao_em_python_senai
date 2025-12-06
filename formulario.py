# ATIVIDADE 2
# Crie um formulário em Tkinter
# Problema: Sistema de Cadastro de Clientes
# Você é um desenvolvedor de software e foi contratado por uma empresa de serviços para criar um sistema de cadastro de clientes. O sistema deve permitir que os clientes forneçam suas informações pessoais, como nome, idade, e-mail, endereço, celular...
# Atividade: Crie um formulário em Tkinter que contenha os seguintes campos: Nome Idade E-mail Endereço Celular
# Cep
# Cidade
# Cursos
# O formulário deve ter um botão de "Enviar" que, quando clicado, imprima as informações do cliente na console.
# Tamanho da tela = '1700x750’ 

import tkinter as tk

def mostrar():
    n = input_n.get()
    print(n)

    i = input_i.get()
    print(i)

    e = input_e.get()
    print(e)

    num = input_num.get()
    print(num)

    cep = input_cep.get()
    print(cep)

    city = input_city.get()
    print(city)

    curso = input_curso.get()
    print(curso)


janela = tk.Tk()
janela.geometry = ('1700x750')
janela.configure(bg = '#98c9a3')


#FRAMES
fr1 =  tk.Frame(janela, bg = '#98c9a3')
fr1.grid()



texto = tk.Label(fr1, text='SISTEMA DE CADASTRO DE CLIENTES ', fg = 'white', font = ('Montserrat', 20), bg ='#98c9a3' ).grid(row=0, column=0,padx= 600)

fr2 =  tk.Frame(janela, bg = '#98c9a3')
fr2.grid(columnspan=2)

#NOME
texto = tk.Label(fr2, text='Digite seu nome: ', fg = 'white', font = ('Montserrat', 15), bg ='#77bfa3' )
texto.grid(column= 0, row= 0, pady=30)
input_n = tk.Entry(fr2,font = ('Montserrat', 15) )
input_n.grid(column= 1, row= 0,pady=20)


#IDADE 
texto = tk.Label(fr2, text='Digite sua idade: ', fg = 'white', font = ('Montserrat', 15), bg ='#77bfa3' )
texto.grid(column= 0, row= 1       ,pady=30)
input_i = tk.Entry(fr2,font = ('Montserrat', 15) )
input_i.grid(column= 1 , row= 1,pady=20)

#EMAIL
texto = tk.Label(fr2, text='Digite seu e-mail: ', fg = 'white', font = ('Montserrat', 15), bg ='#77bfa3' )
texto.grid(column= 0  , row= 2  ,pady=30)
input_e = tk.Entry(fr2,font = ('Montserrat', 15) )
input_e.grid(column= 1 ,row= 2  ,pady=20)

#NÚMERO 
texto = tk.Label(fr2, text='Digite seu número: ', fg = 'white', font = ('Montserrat', 15), bg ='#77bfa3' )
texto.grid(column= 0,row= 3,pady=30)
input_num = tk.Entry(fr2,font = ('Montserrat', 15) )
input_num.grid(column= 1,row= 3,pady=20)

#CEP
texto = tk.Label(fr2, text='Digite seu CEP: ', fg = 'white', font = ('Montserrat', 15), bg ='#77bfa3' )
texto.grid(column= 0,row= 4,pady=30)
input_cep = tk.Entry(fr2,font = ('Montserrat', 15) )
input_cep.grid(column= 1,row= 4,pady=20)

#CIDADE     
texto = tk.Label(fr2, text='CIDADE: ', fg = 'white', font = ('Montserrat', 15), bg ='#77bfa3' )
texto.grid(column= 0,row= 5,pady=30)
input_city = tk.Entry(fr2,font = ('Montserrat', 15) )
input_city.grid(column= 1,row=5,pady=20)

#CURSO
texto = tk.Label(fr2, text='CURSO DESEJADO: ', fg = 'white', font = ('Montserrat', 15), bg ='#77bfa3' )
texto.grid(column= 0,row=6,pady=30)
input_curso = tk.Entry(fr2,font = ('Montserrat', 15) )
input_curso.grid(column=1, row=6,pady=20)


btn =  tk.Button(fr2, text='ENVIAR', bg = '#77bfa3', fg = 'white' , font = ('Montserrat', 25), command=mostrar)
btn.grid(pady=40)




janela.mainloop()