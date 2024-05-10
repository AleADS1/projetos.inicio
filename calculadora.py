import tkinter as tk
from tkinter import ttk

# Função para adicionar um número ou operador na tela
def add_to_expression(value):
    current_expr = expression.get()
    new_expr = current_expr + str(value)
    expression.set(new_expr)

# Função para calcular a expressão na tela
def calculate():
    try:
        result = eval(expression.get())
        expression.set(result)
    except Exception as e:
        expression.set("Erro")
        print(e)

# Função para limpar a tela
def clear_expression():
    expression.set("")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora")

# Usando uma StringVar para gerenciar o conteúdo  
expression = tk.StringVar()

# Criando a interface
display = ttk.Entry(root, textvariable=expression, font=("Helvetica", 18), justify="right")
display.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Adicionando botões
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3), ('=', 4, 2),
    ('C', 4, 0)
]

for (text, row, col) in buttons:
    if text == '=':
        button = ttk.Button(root, text=text, command=calculate)
    elif text == 'C':
        button = ttk.Button(root, text=text, command=clear_expression)
    else:
        button = ttk.Button(root, text=text, command=lambda val=text: add_to_expression(val))
    button.grid(row=row, column=col, sticky="nsew", ipadx=10, ipady=10)

# Ajustando o tamanho dos botões
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    for j in range(4):
        root.grid_columnconfigure(j, weight=1)

# Iniciando o loop 
root.mainloop()
