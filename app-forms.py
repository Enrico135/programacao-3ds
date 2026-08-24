import sqlite3
import re
from tkinter import Tk, Label, Entry, Button, messagebox, ttk

# --- FUNÇÕES DO BANCO DE DADOS ---

def inicializar_banco():
    """Cria o banco de dados e a tabela se não existirem."""
    conexao = sqlite3.connect("cadastro_clientes.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

def salvar_cliente():
    """Valida os campos e insere os dados no banco de dados."""
    nome = entry_nome.get().strip()
    email = entry_email.get().strip()
    telefone = entry_telefone.get().strip()

    # Validação 1: Campos Vazios
    if not nome or not email or not telefone:
        messagebox.showwarning("Aviso", "Todos os campos do formulário devem ser preenchidos!")
        return

    # Validação 2: Formato básico de e-mail (Opcional, mas melhora a qualidade do cadastro)
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showwarning("Aviso", "Por favor, insira um e-mail válido!")
        return

    try:
        conexao = sqlite3.connect("cadastro_clientes.db")
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)",
            (nome, email, telefone)
        )
        conexao.commit()
        conexao.close()
        
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        limpar_formulario()
        
    except sqlite3.Error as erro:
        messagebox.showerror("Erro", f"Erro ao acessar o banco de dados: {erro}")

def limpar_formulario():
    """Limpa todos os campos de entrada de texto."""
    entry_nome.delete(0, 'end')
    entry_email.delete(0, 'end')
    entry_telefone.delete(0, 'end')
    entry_nome.focus()  # Define o foco inicial de volta para o campo nome

# --- CONFIGURAÇÃO DA INTERFACE GRÁFICA (TKINTER) ---

# Inicializa o banco de dados antes de carregar a tela
inicializar_banco()

# Criação da janela principal
janela = Tk()
janela.title("Cadastro de Clientes")
janela.geometry("400x250")
janela.resizable(False, False)

# Configuração de estilo para os elementos ficarem mais modernos
estilo = ttk.Style()
estilo.configure("TLabel", font=("Arial", 10))
estilo.configure("TButton", font=("Arial", 10, "bold"))

# Margem e espaçamento dos componentes na janela
padding_options = {'padx': 15, 'pady': 5}

# Componentes do campo Nome
lbl_nome = ttk.Label(janela, text="Nome:")
lbl_nome.grid(row=0, column=0, sticky="w", **padding_options)
entry_nome = ttk.Entry(janela, width=35)
entry_nome.grid(row=0, column=1, **padding_options)

# Componentes do campo E-mail
lbl_email = ttk.Label(janela, text="E-mail:")
lbl_email.grid(row=1, column=0, sticky="w", **padding_options)
entry_email = ttk.Entry(janela, width=35)
entry_email.grid(row=1, column=1, **padding_options)

# Componentes do campo Telefone
lbl_telefone = ttk.Label(janela, text="Telefone:")
lbl_telefone.grid(row=2, column=0, sticky="w", **padding_options)
entry_telefone = ttk.Entry(janela, width=35)
entry_telefone.grid(row=2, column=1, **padding_options)

# Container para os botões ficarem alinhados lado a lado
frame_botoes = ttk.Frame(janela)
frame_botoes.grid(row=3, column=0, columnspan=2, pady=20)

# Botão Salvar
btn_salvar = ttk.Button(frame_botoes, text="Salvar", command=salvar_cliente)
btn_salvar.pack(side="left", padx=10)

# Botão Limpar
btn_limpar = ttk.Button(frame_botoes, text="Limpar", command=limpar_formulario)
btn_limpar.pack(side="right", padx=10)

# Inicia o loop da interface gráfica
janela.mainloop()
