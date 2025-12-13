import tkinter as tk
from tkinter import ttk

# Janela principal
root = tk.Tk()
root.title("Cadastro de Pacientes")
root.geometry("520x380")
root.resizable(False, False)

# ===============================
# Patient Information
# ===============================
frame_paciente = ttk.LabelFrame(root, text="Patient Information", padding=15)
frame_paciente.pack(padx=20, pady=15, fill="x")

# Nome
ttk.Label(frame_paciente, text="Nome").grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry_nome = ttk.Entry(frame_paciente, width=25)
entry_nome.grid(row=1, column=0, padx=5, pady=5)

# Idade
ttk.Label(frame_paciente, text="Idade").grid(row=0, column=1, sticky="w", padx=5, pady=5)
spin_idade = ttk.Spinbox(frame_paciente, from_=0, to=120, width=10)
spin_idade.set(18)
spin_idade.grid(row=1, column=1, padx=5, pady=5)

# Peso
ttk.Label(frame_paciente, text="Peso (kg)").grid(row=2, column=0, sticky="w", padx=5, pady=5)
entry_peso = ttk.Entry(frame_paciente, width=25)
entry_peso.grid(row=3, column=0, padx=5, pady=5)

# Altura
ttk.Label(frame_paciente, text="Altura (m)").grid(row=2, column=1, sticky="w", padx=5, pady=5)
entry_altura = ttk.Entry(frame_paciente, width=10)
entry_altura.grid(row=3, column=1, padx=5, pady=5)

# ===============================
# IMC (reservado)
# ===============================
frame_imc = ttk.LabelFrame(root, text="IMC", padding=15)
frame_imc.pack(padx=20, pady=10, fill="x")

label_imc = ttk.Label(
    frame_imc,
    text="IMC será calculado automaticamente",
    foreground="gray"
)
label_imc.pack(anchor="w")

# ===============================
# Botão
# ===============================
botao_cadastrar = ttk.Button(root, text="Cadastrar Paciente")
botao_cadastrar.pack(pady=20)

root.mainloop()
