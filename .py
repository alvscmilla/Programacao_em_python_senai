import tkinter as tk #as tk como tkinter>tk 


#FUNÇÃO para 
def mostar_():
    texto  =   input_.get()
    mostrar_texto.config(text=texto)   




janela = tk.Tk()  #criar janela
janela.geometry('1440x1024') #tamanho
janela.configure(bg = '#962828') #cor


#sempre vem dois text, dois input, dois button
#janela = onde aparece
#text = o texto que aparece na tela
#fg = cor
#font = fonte da letra
#bg = fundo
texto = tk.Label(janela, text='SEU TEXTO AQUI', fg = 'white', font = ('Montserrat', 32), bg ='#480987' )
texto.pack(pady=75)
#pack = posicionar as coisas
#pady = posicionar na VERTICAL


#input para DIGITAR
input_ = tk.Entry(janela,font = ('Montserrat', 32) )
input_.pack(pady=40)

#BOTÃO PARA enviar, com texto CLIQUE
btn =  tk.Button(janela, text='CLIQUE', bg = 'black', fg = 'white' , font = ('Montserrat', 25), command=mostar_)
btn.pack(pady=40)
 
#AVISANDO PREVIAMENTE QUE IRÁ MOSTRAR UM TEXTO APÓS O CLIQUE
mostrar_texto =  tk.Label(janela, text = 'aqui vai mostrar um texto', bg ='#480987', fg = 'white', font = ('Montserrat', 25))
mostrar_texto.pack(pady=30)




janela.mainloop()  #tela, tudo vem ANTES do loop para aparecer.

#auto-py-exe para ver no console