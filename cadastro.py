import tkinter as tk
from tkinter import ttk

def submit_form():
    nome = nome_entry.get()
    descricao = descricao_entry.get()
    valor = valor_entry.get()
    disponivel = disponivel_var.get()
    
    # Aqui pode ser adicionado o código para salvar os dados do produto
    print(f"Nome: {nome}, Descrição: {descricao}, Valor: {valor}, Disponível: {disponivel}")

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro de Produtos")

# Nome do produto
tk.Label(root, text="Nome do Produto:").grid(row=0, column=0, padx=10, pady=5)
nome_entry = tk.Entry(root)
nome_entry.grid(row=0, column=1, padx=10, pady=5)

# Descrição do produto
tk.Label(root, text="Descrição do Produto:").grid(row=1, column=0, padx=10, pady=5)
descricao_entry = tk.Entry(root)
descricao_entry.grid(row=1, column=1, padx=10, pady=5)

# Valor do produto
tk.Label(root, text="Valor do Produto:").grid(row=2, column=0, padx=10, pady=5)
valor_entry = tk.Entry(root)
valor_entry.grid(row=2, column=1, padx=10, pady=5)

# Disponibilidade do produto
tk.Label(root, text="Disponível para Venda:").grid(row=3, column=0, padx=10, pady=5)
disponivel_var = tk.StringVar(value="Sim")
ttk.Radiobutton(root, text="Sim", variable=disponivel_var, value="Sim").grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)
ttk.Radiobutton(root, text="Não", variable=disponivel_var, value="Não").grid(row=3, column=2, padx=10, pady=5, sticky=tk.W)

# Botão de submissão
submit_button = tk.Button(root, text="Cadastrar Produto", command=submit_form)
submit_button.grid(row=4, column=0, columnspan=3, pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()