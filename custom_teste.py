import customtkinter as ctk

# Configuração inicial
ctk.set_appearance_mode("light")  # "dark" se quiser
ctk.set_default_color_theme("blue")

# Janela principal
app = ctk.CTk()
app.title("Cadastro de Pacientes")
app.geometry("550x420")
app.resizable(False, False)

# =========================
# Frame principal (card)
# =========================
frame_main = ctk.CTkFrame(app, corner_radius=15)
frame_main.pack(padx=20, pady=20, fill="both", expand=True)

# Título
titulo = ctk.CTkLabel(
    frame_main,
    text="Cadastro de Pacientes",
    font=ctk.CTkFont(size=20, weight="bold")
)
titulo.pack(pady=(20, 10))

# =========================
# Patient Information
# =========================
frame_info = ctk.CTkFrame(frame_main, corner_radius=12)
frame_info.pack(padx=20, pady=10, fill="x")

label_info = ctk.CTkLabel(
    frame_info,
    text="Patient Information",
    font=ctk.CTkFont(size=14, weight="bold")
)
label_info.grid(row=0, column=0, columnspan=2, sticky="w", padx=15, pady=(10, 5))

# Nome
ctk.CTkLabel(frame_info, text="Nome").grid(row=1, column=0, sticky="w", padx=15)
entry_nome = ctk.CTkEntry(frame_info, width=220)
entry_nome.grid(row=2, column=0, padx=15, pady=(0, 10))

# Idade
ctk.CTkLabel(frame_info, text="Idade").grid(row=1, column=1, sticky="w", padx=15)
entry_idade = ctk.CTkEntry(frame_info, width=100)
entry_idade.grid(row=2, column=1, padx=15, pady=(0, 10))

# Peso
ctk.CTkLabel(frame_info, text="Peso (kg)").grid(row=3, column=0, sticky="w", padx=15)
entry_peso = ctk.CTkEntry(frame_info, width=220)
entry_peso.grid(row=4, column=0, padx=15, pady=(0, 10))

# Altura
ctk.CTkLabel(frame_info, text="Altura (m)").grid(row=3, column=1, sticky="w", padx=15)
entry_altura = ctk.CTkEntry(frame_info, width=100)
entry_altura.grid(row=4, column=1, padx=15, pady=(0, 10))

# =========================
# IMC (reservado)
# =========================
frame_imc = ctk.CTkFrame(frame_main, corner_radius=12)
frame_imc.pack(padx=20, pady=10, fill="x")

label_imc_titulo = ctk.CTkLabel(
    frame_imc,
    text="IMC",
    font=ctk.CTkFont(size=14, weight="bold")
)
label_imc_titulo.pack(anchor="w", padx=15, pady=(10, 5))

label_imc = ctk.CTkLabel(
    frame_imc,
    text="IMC será calculado automaticamente",
    text_color="gray"
)
label_imc.pack(anchor="w", padx=15, pady=(0, 10))

# =========================
# Botão
# =========================
botao_cadastrar = ctk.CTkButton(
    frame_main,
    text="Cadastrar Paciente",
    height=40,
    font=ctk.CTkFont(size=14, weight="bold")
)
botao_cadastrar.pack(pady=20)

app.mainloop()
