# A CLÍNICA "SAÚDE & BEM-ESTAR" ENFRENTA DIFICULDADES EM GERENCIAR O CADASTRO DE SEUS PACIENTES E CALCULAR O IMC (ÍNDICE DE MASSA CORPORAL) DURANTE AS CONSULTAS. OS DADOS SÃO REGISTRADOS MANUALMENTE, O QUE PODE LEVAR A ERROS E DIFICULDADE NA CONSULTA DOS DADOS. ALÉM DISSO, O CÁLCULO DO IMC É FEITO DE MANEIRA ARCAICA, SEM SER AUTOMATIZADO.

#------------------PROPOSTA--------------------
# Criar um sistema de cadastro de pacientes que permita registrar dados como nome, idade, peso e altura. O sistema calculará automaticamente o IMC de cada paciente com base nos dados fornecidos. Além disso, será possível consultar, editar ou excluir os registros dos pacientes.





import tkinter as tk
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk 


# ======
#  IMC
# ======

# def imc():
#     peso = entry_peso.get()
#     altura = entry_altura.get()
#     imc_valor = peso / (altura ** 2)
#     return imc_valor
# imc()


# ===========
#  DATABASE
# ===========

def conectar():
    return sqlite3.connect('cadastrohospitalar_database.db')

def tabela_():
    conn = conectar()
    c = conn.cursor()
    c.execute(''' CREATE TABLE IF NOT EXISTS pacientes(
              
              NOME TEXT,
              IDADE INTEGER,
              ALTURA REAL,
              PESO REAL,
              IMC REAL

              )
    ''')
    conn.commit()
    conn.close()

tabela_()

# =========
#   CRUD
# =========


# CREATE

def inserir_usuario():
    nome  = entry_nome.get()
    idade = entry_idade.get()
    altura = float(entry_altura.get())
    peso = float(entry_peso.get())
    imc = peso / (altura**2)
    label_imc.configure(text =f'{round(imc,2)}')
    if nome and idade and altura and peso:
        conn =  conectar()
        c =  conn.cursor()
        c.execute('INSERT INTO pacientes(NOME,IDADE,ALTURA,PESO, IMC) VALUES(?,?,?,?,?)', (nome, idade, altura, peso, imc))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADOS INSERIDOS COM SUCESSO')
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'DADOS NÃO INSERIDOS')    

# READ

def mostrar_usuario():
    for row in tree.get_children():
        tree.delete(row)
    conn =  conectar()
    c = conn.cursor()
    c.execute('SELECT * FROM pacientes')
    paciente = c.fetchall()
    for pacientes in paciente:
        tree.insert("", 'end', values=(pacientes[0], pacientes[1],pacientes[2],pacientes[3],pacientes[4]))       
    conn.close()

# UPDATE
def atualizar():
    selecao =  tree.selection()
    if selecao:
        user_name =  tree.item(selecao)['values'][0]
        novo_nome = entry_nome.get()
        novo_idade = entry_idade.get()
        novo_altura = entry_altura.get()
        novo_peso = entry_peso.get()


        if novo_nome and novo_idade and novo_altura and novo_peso:
            conn =  conectar()
            c =  conn.cursor()
            c.execute('UPDATE pacientes  SET NOME = ?, IDADE = ?, ALTURA = ?, PESO = ?   WHERE NOME = ?', (novo_nome, novo_idade, novo_altura, novo_peso,user_name))
            conn.commit()
            conn.close()
            messagebox.showinfo('', 'DADOS ATUALIZADOS')
            mostrar_usuario()
        else:
            messagebox.showerror('ERRO', 'OCORREU UM ERRO!')
    else:
        messagebox.showwarning('', 'OCORREU UM ERRO DESCONHECIDO')    

# DELETE

def deletar():

    selecao =  tree.selection()
    if selecao:
        user_name =  tree.item(selecao)['values'][0]
        conn = conectar()
        c = conn.cursor()
        c.execute('DELETE FROM pacientes WHERE NOME = ?', (user_name,))
        conn.commit()
        conn.close()
        messagebox.showinfo('', 'DADOS DELETADOS')
        mostrar_usuario()
    else:
        messagebox.showerror('ERRO', 'OCORREU UM ERRO')    



# =====================
#   INTERFACE GRÁFICA
# =====================

root =  tk.Tk()
root.geometry("1050x680")
icone = 'hospital.ico'
root.title('CADASTRO DE PACIENTES')
root.iconbitmap(icone)


fr1 = tk.Frame(root)
fr1.grid(columnspan=3, pady=20)



# NOME
label_nome = ctk.CTkLabel(fr1, text="NOME").grid(row=1, column=0, padx=15)
entry_nome = ctk.CTkEntry(fr1, width=220)
entry_nome.grid(row=2, column=0, padx=15, pady=(0, 10))


# IDADE
label_idade = ctk.CTkLabel(fr1, text="IDADE").grid(row=1, column=1, padx=15)
entry_idade = ctk.CTkEntry(fr1, width=100)
entry_idade.grid(row=2, column=1, padx=15, pady=(0, 10))


# ALTURA
label_altura = ctk.CTkLabel(fr1, text="ALTURA").grid(row=3, column=0, padx=15)
entry_altura = ctk.CTkEntry(fr1, width=220)
entry_altura.grid(row=4, column=0, padx=15, pady=(0, 10))


# PESO
label_peso = ctk.CTkLabel(fr1, text="PESO").grid(row=3, column=1, padx=15)
entry_peso = ctk.CTkEntry(fr1, width=100)
entry_peso.grid(row=4, column=1, padx=15, pady=(0, 10))


# ======
#  IMC
# ======

fr4 = tk.Frame(root)
fr4.grid(columnspan=3, pady=20)


frame_imc = ctk.CTkFrame(fr4)
frame_imc.pack(padx=20, pady=10)
label_imc_titulo = ctk.CTkLabel(frame_imc, text="IMC", font=ctk.CTkFont(size=14, weight="bold"))

label_imc_titulo.pack(padx=15)
label_imc = ctk.CTkLabel(frame_imc, text="IMC CALCULADO AUTOMATICAMENTE", text_color="gray")
label_imc.pack(padx=15)

# ============
#    BUTTON
# ============

fr2 = tk.Frame(root)
fr2.grid(columnspan=3, pady=20)


btn_salvar = ctk.CTkButton(fr2, text='SALVAR', font=('arial', 12), command= inserir_usuario)
btn_salvar.grid(row=4, column=0, pady = 5, padx=5)

btn_atualizar = ctk.CTkButton(fr2, text='ATUALIZAR', font=('arial', 12), command=atualizar)
btn_atualizar.grid(row=4, column=1, pady = 5, padx=5)

btn_deletar = ctk.CTkButton(fr2, text='DELETAR', font=('arial', 12), command=deletar)
btn_deletar.grid(row=4, column=2, pady = 5, padx=5)

fr3 = tk.Frame(root)
fr3.grid(columnspan=3, pady=20, padx=22)


columns = ('NOME', 'IDADE', 'ALTURA', 'PESO', 'IMC')
tree = ttk.Treeview(fr3, columns=columns, show='headings')
tree.grid(row=6,column=0)

root.mainloop()