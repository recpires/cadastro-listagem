import tkinter as tk
from tkinter import ttk, simpledialog

class ProductListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Listagem de Produtos")

        self.products = []

        self.tree = ttk.Treeview(root, columns=('Nome', 'Valor'), show='headings')
        self.tree.heading('Nome', text='Nome')
        self.tree.heading('Valor', text='Valor')
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.add_button = tk.Button(root, text="Cadastrar Novo Produto", command=self.add_product)
        self.add_button.pack(pady=10)

    def add_product(self):
        name = simpledialog.askstring("Input", "Nome do Produto:")
        value = simpledialog.askfloat("Input", "Valor do Produto:")

        if name and value is not None:
            self.products.append((name, value))
            self.products.sort(key=lambda x: x[1])
            self.update_treeview()

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for product in self.products:
            self.tree.insert('', tk.END, values=product)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProductListApp(root)
    root.mainloop()