import tkinter as tk
from tkinter import ttk
import datetime as dt


lista_tipos = ["Galão", "Caixa", "Tubo", "Cilindro", "Unidade"]
lista_codigos = []

janela = tk.Tk()

#Criação da função

def inserir_codigo():
    desc = entry_description.get()
    tipo = combobox_selecionarTipo.get()
    qntd = entry_quantidade.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")
    codigo = len(lista_codigos) + 1
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((codigo_str, desc, tipo, qntd, data_criacao))
    entry_description.delete("")



janela.title("Cadastro de  Materiais")
janela.geometry("500x300")
janela.resizable(width=False, height=False)
janela.configure(background='#1C3144')

label_description = tk.Label(text='Descrição do Material', fg='#fff',bg='#1C3144', font=('Helvetica',10,'bold'))
label_description.place(relx= 0.1, rely= 0.05, relwidth=0.80, relheight=0.08)

entry_description = tk.Entry()
entry_description.place(relx = 0.1, rely = 0.2, relwidth=0.80, relheight=0.08)

label_tipo_unidade = tk.Label(text='Tipo de Unidade do Material', fg='black', font=('Helvetica',10,'bold'))
label_tipo_unidade.place(relx = 0.1, rely = 0.33, relwidth=0.38, relheight=0.08)

combobox_selecionarTipo = ttk.Combobox(values=lista_tipos)
combobox_selecionarTipo.place(relx = 0.50, rely = 0.33, relwidth=0.40, relheight=0.08)

label_quantidade = tk.Label(text='Quantidade da unidade do Material', fg='black', font=('Helvetica',10,'bold'))
label_quantidade.place(relx = 0.1, rely = 0.45, relwidth=0.47, relheight=0.08)

entry_quantidade = tk.Entry()
entry_quantidade.place(relx = 0.60, rely = 0.45, relwidth=0.10, relheight=0.08)

btn_criar_codigo = tk.Button(text='CRIAR CÓDIGO',fg='black', font=('Helvetica',10,'bold'), command=inserir_codigo)
btn_criar_codigo.place(relx = 0.35, rely = 0.60, relwidth=0.30, relheight=0.08)



janela.mainloop()

print(lista_codigos)