import tkinter as tk
import sqlite3
import pandas as pd




#conexao = sqlite3.connect('banco_clientes.db')

#cursor = conexao.cursor()

#cursor.execute("""CREATE TABLE clientes (
#    nome text,
#    sobrenome text,
#    email text,
#    telefone text
#    )
#""")

#conexao.commit()

#conexao.close()

def cadastrar_clientes():
    conexao = sqlite3.connect('banco_clientes.db')

    cursor = conexao.cursor()

    cursor.execute("INSERT INTO clientes VALUES (:nome, :sobrenome, :email, :telefone)",
            {
            'nome':nome_entry.get(),
            'sobrenome':sobrenome_entry.get(),
            'email':email_entry.get(),
            'telefone':telefone_entry.get()
            }
            )

    conexao.commit()

    conexao.close()

    nome_entry.delete(0, 'end')
    sobrenome_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    telefone_entry.delete(0, 'end')


def export_clientes():
    conexao = sqlite3.connect('banco_clientes.db')

    cursor = conexao.cursor()

    cursor.execute("SELECT *, oid FROM clientes")
    clientes_cadastrados = cursor.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['nome', 'sobrenome', 'email', 'telefone', 'Id_banco'])
    clientes_cadastrados.to_excel('banco_clientes.xlsx')
    conexao.commit()

    conexao.close()



janela = tk.Tk()
janela.title('Ferramenta de Cadastro de Cliente')
janela.geometry('500x300')
janela.configure(background='#272D2D')

#Labels
nome_label = tk.Label(janela, text="Nome", fg='#fff', bg='#272D2D', font=('Helvetica',10, 'bold'))
nome_label.place(relx = 0.1, rely= 0.08, relwidth=0.15, relheight=0.1)

nome_entry = tk.Entry(janela, bg='#fff')
nome_entry.place(relx= 0.25, rely= 0.10, relwidth=0.60, relheight=0.07)

sobrenome_label = tk.Label(janela, text="Sobrenome", fg='#fff', bg='#272D2D', font=('Helvetica',10, 'bold'))
sobrenome_label.place(relx = 0.07, rely= 0.20, relwidth=0.15, relheight=0.1)

sobrenome_entry = tk.Entry(janela, bg='#fff')
sobrenome_entry.place(relx= 0.25, rely= 0.22, relwidth=0.60, relheight=0.07)

email_label = tk.Label(janela, text="Email", fg='#fff', bg='#272D2D', font=('Helvetica',10, 'bold'))
email_label.place(relx = 0.1, rely= 0.33, relwidth=0.15, relheight=0.1)

email_entry = tk.Entry(janela, bg='#fff')
email_entry.place(relx= 0.25, rely= 0.34, relwidth=0.60, relheight=0.07)

telefone_label = tk.Label(janela, text="Telefone", fg='#fff', bg='#272D2D', font=('Helvetica',10, 'bold'))
telefone_label.place(relx = 0.08, rely= 0.44, relwidth=0.15, relheight=0.1)

telefone_entry = tk.Entry(janela, bg='#fff')
telefone_entry.place(relx= 0.25, rely= 0.46, relwidth=0.60, relheight=0.07)

#Botao
botao_cadastrar = tk.Button(janela, text='Cadastrar' ,bg='#e24', fg='white', activebackground='#e24', activeforeground='#fff', font=('Helvetica',10, 'bold'), command=cadastrar_clientes)
botao_cadastrar.place(relx= 0.30, rely= 0.6, relwidth=0.45, relheight=0.1)

botao_exportar = tk.Button(janela, text='Exportar para Exel' ,bg='#23CE6B', fg='white', activebackground='#23CE6B', activeforeground='#fff', font=('Helvetica',10, 'bold'), command=export_clientes)
botao_exportar.place(relx= 0.35, rely= 0.73, relwidth=0.35, relheight=0.1)



janela.mainloop()