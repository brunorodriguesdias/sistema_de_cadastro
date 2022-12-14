from tkinter import *
import tkinter as tk
import tela_cadastro
import mysql.connector

banco = mysql.connector.connect(host='localhost', user='root', passwd='', database='clientes')
cursor = banco.cursor()

def tela_consulta():

    _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
    _fgcolor = '#000000'  # X11 color: 'black'
    _compcolor = 'gray40'  # X11 color: #666666
    _ana1color = '#c3c3c3'  # Closest X11 color: 'gray76'
    _ana2color = 'beige'  # X11 color: #f5f5dc
    _tabfg1 = 'black'
    _tabfg2 = 'black'
    _tabbg1 = 'grey75'
    _tabbg2 = 'grey89'
    _bgmode = 'light'


    class Tela_consulta_cliente:
        def __init__(self, top=None):
            top = tk.Tk()
            top.geometry("600x450+348+126")
            top.minsize(120, 1)
            top.maxsize(3290, 1061)
            top.resizable(1, 1)
            top.title("Consulta clientes")
            top.configure(background="#dbf3fd")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="black")
            self.top = top

            self.label_retorno_nome = tk.Label(self.top)
            self.label_retorno_nome.place(relx=0.067, rely=0.156, height=21, width=44)
            self.label_retorno_nome.configure(activebackground="#f9f9f9")
            self.label_retorno_nome.configure(anchor='w')
            self.label_retorno_nome.configure(background="#dbf3fd")
            self.label_retorno_nome.configure(compound='left')
            self.label_retorno_nome.configure(disabledforeground="#a3a3a3")
            self.label_retorno_nome.configure(font="-family {SimSun} -size 12")
            self.label_retorno_nome.configure(foreground="#000000")
            self.label_retorno_nome.configure(highlightbackground="#d9d9d9")
            self.label_retorno_nome.configure(highlightcolor="black")
            self.label_retorno_nome.configure(text='''Nome:''')

            self.label_retorno_nome_1 = tk.Label(self.top)
            self.label_retorno_nome_1.place(relx=0.067, rely=0.222, height=21, width=44)
            self.label_retorno_nome_1.configure(activebackground="#f9f9f9")
            self.label_retorno_nome_1.configure(anchor='w')
            self.label_retorno_nome_1.configure(background="#dbf3fd")
            self.label_retorno_nome_1.configure(compound='left')
            self.label_retorno_nome_1.configure(disabledforeground="#a3a3a3")
            self.label_retorno_nome_1.configure(font="-family {SimSun} -size 12")
            self.label_retorno_nome_1.configure(foreground="#000000")
            self.label_retorno_nome_1.configure(highlightbackground="#d9d9d9")
            self.label_retorno_nome_1.configure(highlightcolor="black")
            self.label_retorno_nome_1.configure(text='''CPF:''')

            self.label_retorno_nome_1_1 = tk.Label(self.top)
            self.label_retorno_nome_1_1.place(relx=0.067, rely=0.289, height=21, width=94)
            self.label_retorno_nome_1_1.configure(activebackground="#f9f9f9")
            self.label_retorno_nome_1_1.configure(anchor='w')
            self.label_retorno_nome_1_1.configure(background="#dbf3fd")
            self.label_retorno_nome_1_1.configure(compound='left')
            self.label_retorno_nome_1_1.configure(disabledforeground="#a3a3a3")
            self.label_retorno_nome_1_1.configure(font="-family {SimSun} -size 12")
            self.label_retorno_nome_1_1.configure(foreground="#000000")
            self.label_retorno_nome_1_1.configure(highlightbackground="#d9d9d9")
            self.label_retorno_nome_1_1.configure(highlightcolor="black")
            self.label_retorno_nome_1_1.configure(text='''Nascimento:''')

            self.label_retorno_nome_1_1_1 = tk.Label(self.top)
            self.label_retorno_nome_1_1_1.place(relx=0.067, rely=0.356, height=21, width=84)
            self.label_retorno_nome_1_1_1.configure(activebackground="#f9f9f9")
            self.label_retorno_nome_1_1_1.configure(anchor='w')
            self.label_retorno_nome_1_1_1.configure(background="#dbf3fd")
            self.label_retorno_nome_1_1_1.configure(compound='left')
            self.label_retorno_nome_1_1_1.configure(disabledforeground="#a3a3a3")
            self.label_retorno_nome_1_1_1.configure(font="-family {SimSun} -size 12")
            self.label_retorno_nome_1_1_1.configure(foreground="#000000")
            self.label_retorno_nome_1_1_1.configure(highlightbackground="#d9d9d9")
            self.label_retorno_nome_1_1_1.configure(highlightcolor="black")
            self.label_retorno_nome_1_1_1.configure(text='''Telefone:''')

            self.label_retorno_nome_1_1_1_1 = tk.Label(self.top)
            self.label_retorno_nome_1_1_1_1.place(relx=0.067, rely=0.422, height=21, width=64)
            self.label_retorno_nome_1_1_1_1.configure(activebackground="#f9f9f9")
            self.label_retorno_nome_1_1_1_1.configure(anchor='w')
            self.label_retorno_nome_1_1_1_1.configure(background="#dbf3fd")
            self.label_retorno_nome_1_1_1_1.configure(compound='left')
            self.label_retorno_nome_1_1_1_1.configure(disabledforeground="#a3a3a3")
            self.label_retorno_nome_1_1_1_1.configure(font="-family {SimSun} -size 12")
            self.label_retorno_nome_1_1_1_1.configure(foreground="#000000")
            self.label_retorno_nome_1_1_1_1.configure(highlightbackground="#d9d9d9")
            self.label_retorno_nome_1_1_1_1.configure(highlightcolor="black")
            self.label_retorno_nome_1_1_1_1.configure(text='''E-mail:''')

            self.label_titulo_cep = tk.Label(self.top)
            self.label_titulo_cep.place(relx=0.067, rely=0.489, height=21, width=44)
            self.label_titulo_cep.configure(activebackground="#f9f9f9")
            self.label_titulo_cep.configure(anchor='w')
            self.label_titulo_cep.configure(background="#dbf3fd")
            self.label_titulo_cep.configure(compound='left')
            self.label_titulo_cep.configure(disabledforeground="#a3a3a3")
            self.label_titulo_cep.configure(font="-family {SimSun} -size 12")
            self.label_titulo_cep.configure(foreground="#000000")
            self.label_titulo_cep.configure(highlightbackground="#d9d9d9")
            self.label_titulo_cep.configure(highlightcolor="black")
            self.label_titulo_cep.configure(text='''CEP:''')

            self.label_titulo_cnpj = tk.Label(self.top)
            self.label_titulo_cnpj.place(relx=0.533, rely=0.244, height=21, width=44)
            self.label_titulo_cnpj.configure(activebackground="#f9f9f9")
            self.label_titulo_cnpj.configure(anchor='w')
            self.label_titulo_cnpj.configure(background="#dbf3fd")
            self.label_titulo_cnpj.configure(compound='left')
            self.label_titulo_cnpj.configure(disabledforeground="#a3a3a3")
            self.label_titulo_cnpj.configure(font="-family {SimSun} -size 12")
            self.label_titulo_cnpj.configure(foreground="#000000")
            self.label_titulo_cnpj.configure(highlightbackground="#d9d9d9")
            self.label_titulo_cnpj.configure(highlightcolor="black")
            self.label_titulo_cnpj.configure(text='''CNPJ:''')

            self.label_titulo_inscricao = tk.Label(self.top)
            self.label_titulo_inscricao.place(relx=0.533, rely=0.311, height=21, width=104)
            self.label_titulo_inscricao.configure(activebackground="#f9f9f9")
            self.label_titulo_inscricao.configure(anchor='w')
            self.label_titulo_inscricao.configure(background="#dbf3fd")
            self.label_titulo_inscricao.configure(compound='left')
            self.label_titulo_inscricao.configure(disabledforeground="#a3a3a3")
            self.label_titulo_inscricao.configure(font="-family {SimSun} -size 12")
            self.label_titulo_inscricao.configure(foreground="#000000")
            self.label_titulo_inscricao.configure(highlightbackground="#d9d9d9")
            self.label_titulo_inscricao.configure(highlightcolor="black")
            self.label_titulo_inscricao.configure(text='''Ins.Estadual:''')

            self.botao_nova_consulta = tk.Button(self.top)
            self.botao_nova_consulta.place(relx=0.067, rely=0.622, height=54, width=237)
            self.botao_nova_consulta.configure(activebackground="beige")
            self.botao_nova_consulta.configure(activeforeground="black")
            self.botao_nova_consulta.configure(background="#ebfdfe")
            self.botao_nova_consulta.configure(compound='left')
            self.botao_nova_consulta.configure(disabledforeground="#a3a3a3")
            self.botao_nova_consulta.configure(font="-family {SimSun} -size 10")
            self.botao_nova_consulta.configure(foreground="#000000")
            self.botao_nova_consulta.configure(highlightbackground="#d9d9d9")
            self.botao_nova_consulta.configure(highlightcolor="black")
            self.botao_nova_consulta.configure(pady="0")
            self.botao_nova_consulta.configure(text='''Nova consulta''')
            self.botao_nova_consulta.configure(command=self.nova_consulta)

            self.botao_retorna_para_cadastro = tk.Button(self.top)
            self.botao_retorna_para_cadastro.place(relx=0.533, rely=0.622, height=54, width=237)
            self.botao_retorna_para_cadastro.configure(activebackground="beige")
            self.botao_retorna_para_cadastro.configure(activeforeground="black")
            self.botao_retorna_para_cadastro.configure(background="#ebfdfe")
            self.botao_retorna_para_cadastro.configure(compound='left')
            self.botao_retorna_para_cadastro.configure(disabledforeground="#a3a3a3")
            self.botao_retorna_para_cadastro.configure(font="-family {SimSun} -size 10")
            self.botao_retorna_para_cadastro.configure(foreground="#000000")
            self.botao_retorna_para_cadastro.configure(highlightbackground="#d9d9d9")
            self.botao_retorna_para_cadastro.configure(highlightcolor="black")
            self.botao_retorna_para_cadastro.configure(pady="0")
            self.botao_retorna_para_cadastro.configure(text='''Retornar para cadastro''')
            self.botao_retorna_para_cadastro.configure(command=self.retorna_cadastro)

            self.botao_consulta = tk.Button(self.top)
            self.botao_consulta.place(relx=0.517, rely=0.067, height=24, width=147)
            self.botao_consulta.configure(activebackground="beige")
            self.botao_consulta.configure(activeforeground="black")
            self.botao_consulta.configure(background="#ebfdfe")
            self.botao_consulta.configure(compound='left')
            self.botao_consulta.configure(disabledforeground="#a3a3a3")
            self.botao_consulta.configure(font="-family {SimSun} -size 9")
            self.botao_consulta.configure(foreground="#000000")
            self.botao_consulta.configure(highlightbackground="#d9d9d9")
            self.botao_consulta.configure(highlightcolor="black")
            self.botao_consulta.configure(pady="0")
            self.botao_consulta.configure(text='''Consulta''')
            self.botao_consulta.configure(command=self.consulta_cadastro)

            self.label_cpf_cnpj = tk.Label(self.top)
            self.label_cpf_cnpj.place(relx=0.067, rely=0.067, height=21, width=174)
            self.label_cpf_cnpj.configure(activebackground="#f9f9f9")
            self.label_cpf_cnpj.configure(anchor='w')
            self.label_cpf_cnpj.configure(background="#dbf3fd")
            self.label_cpf_cnpj.configure(compound='left')
            self.label_cpf_cnpj.configure(disabledforeground="#a3a3a3")
            self.label_cpf_cnpj.configure(font="-family {SimSun} -size 12")
            self.label_cpf_cnpj.configure(foreground="#000000")
            self.label_cpf_cnpj.configure(highlightbackground="#d9d9d9")
            self.label_cpf_cnpj.configure(highlightcolor="black")
            self.label_cpf_cnpj.configure(text='''CPF/CNPJ:''')

            self.entry_cpf_cnpj = tk.Entry(self.top)
            self.entry_cpf_cnpj.place(relx=0.2, rely=0.067, height=20, relwidth=0.29)
            self.entry_cpf_cnpj.configure(background="white")
            self.entry_cpf_cnpj.configure(disabledforeground="#a3a3a3")
            self.entry_cpf_cnpj.configure(font="TkFixedFont")
            self.entry_cpf_cnpj.configure(foreground="#000000")
            self.entry_cpf_cnpj.configure(highlightbackground="#d9d9d9")
            self.entry_cpf_cnpj.configure(highlightcolor="black")
            self.entry_cpf_cnpj.configure(insertbackground="black")
            self.entry_cpf_cnpj.configure(selectbackground="#c4c4c4")
            self.entry_cpf_cnpj.configure(selectforeground="black")

            self.label_retorno_nome = tk.Label(self.top)
            self.label_retorno_nome.place(relx=0.15, rely=0.156, height=21, width =264)
            self.label_retorno_nome.configure(activebackground="#f9f9f9")
            self.label_retorno_nome.configure(anchor='w')
            self.label_retorno_nome.configure(background="#FFFFFF")
            self.label_retorno_nome.configure(compound='left')
            self.label_retorno_nome.configure(disabledforeground="#a3a3a3")
            self.label_retorno_nome.configure(foreground="#000000")
            self.label_retorno_nome.configure(highlightbackground="#d9d9d9")
            self.label_retorno_nome.configure(highlightcolor="black")
            self.label_retorno_nome.configure(relief="sunken")

            self.label_retorno_cpf = tk.Label(self.top)
            self.label_retorno_cpf.place(relx=0.133, rely=0.222, height=21, width =174)
            self.label_retorno_cpf.configure(activebackground="#f9f9f9")
            self.label_retorno_cpf.configure(anchor='w')
            self.label_retorno_cpf.configure(background="#FFFFFF")
            self.label_retorno_cpf.configure(compound='left')
            self.label_retorno_cpf.configure(disabledforeground="#a3a3a3")
            self.label_retorno_cpf.configure(foreground="#000000")
            self.label_retorno_cpf.configure(highlightbackground="#d9d9d9")
            self.label_retorno_cpf.configure(highlightcolor="black")
            self.label_retorno_cpf.configure(relief="sunken")

            self.label_retorno_nascimento = tk.Label(self.top)
            self.label_retorno_nascimento.place(relx=0.233, rely=0.289, height=21, width = 134)
            self.label_retorno_nascimento.configure(activebackground="#f9f9f9")
            self.label_retorno_nascimento.configure(anchor='w')
            self.label_retorno_nascimento.configure(background="#FFFFFF")
            self.label_retorno_nascimento.configure(compound='left')
            self.label_retorno_nascimento.configure(disabledforeground="#a3a3a3")
            self.label_retorno_nascimento.configure(foreground="#000000")
            self.label_retorno_nascimento.configure(highlightbackground="#d9d9d9")
            self.label_retorno_nascimento.configure(highlightcolor="black")
            self.label_retorno_nascimento.configure(relief="sunken")

            self.label_retorno_telefone = tk.Label(self.top)
            self.label_retorno_telefone.place(relx=0.2, rely=0.356, height=21, width = 144)
            self.label_retorno_telefone.configure(activebackground="#f9f9f9")
            self.label_retorno_telefone.configure(anchor='w')
            self.label_retorno_telefone.configure(background="#FFFFFF")
            self.label_retorno_telefone.configure(compound='left')
            self.label_retorno_telefone.configure(disabledforeground="#a3a3a3")
            self.label_retorno_telefone.configure(foreground="#000000")
            self.label_retorno_telefone.configure(highlightbackground="#d9d9d9")
            self.label_retorno_telefone.configure(highlightcolor="black")
            self.label_retorno_telefone.configure(relief="sunken")

            self.label_retorno_email = tk.Label(self.top)
            self.label_retorno_email.place(relx=0.167, rely=0.422, height=21, width = 214)
            self.label_retorno_email.configure(activebackground="#f9f9f9")
            self.label_retorno_email.configure(anchor='w')
            self.label_retorno_email.configure(background="#FFFFFF")
            self.label_retorno_email.configure(compound='left')
            self.label_retorno_email.configure(disabledforeground="#a3a3a3")
            self.label_retorno_email.configure(foreground="#000000")
            self.label_retorno_email.configure(highlightbackground="#d9d9d9")
            self.label_retorno_email.configure(highlightcolor="black")
            self.label_retorno_email.configure(relief="sunken")

            self.label_retorno_cep = tk.Label(self.top)
            self.label_retorno_cep.place(relx=0.133, rely=0.489, height=21, width = 134)
            self.label_retorno_cep.configure(activebackground="#f9f9f9")
            self.label_retorno_cep.configure(anchor='w')
            self.label_retorno_cep.configure(background="#FFFFFF")
            self.label_retorno_cep.configure(compound='left')
            self.label_retorno_cep.configure(disabledforeground="#a3a3a3")
            self.label_retorno_cep.configure(foreground="#000000")
            self.label_retorno_cep.configure(highlightbackground="#d9d9d9")
            self.label_retorno_cep.configure(highlightcolor="black")
            self.label_retorno_cep.configure(relief="sunken")

            self.label_retorno_cnpj = tk.Label(self.top)
            self.label_retorno_cnpj.place(relx=0.617, rely=0.244, height=21, width = 194)
            self.label_retorno_cnpj.configure(activebackground="#f9f9f9")
            self.label_retorno_cnpj.configure(anchor='w')
            self.label_retorno_cnpj.configure(background="#FFFFFF")
            self.label_retorno_cnpj.configure(compound='left')
            self.label_retorno_cnpj.configure(disabledforeground="#a3a3a3")
            self.label_retorno_cnpj.configure(foreground="#000000")
            self.label_retorno_cnpj.configure(highlightbackground="#d9d9d9")
            self.label_retorno_cnpj.configure(highlightcolor="black")
            self.label_retorno_cnpj.configure(relief="sunken")

            self.label_retorno_inscricao = tk.Label(self.top)
            self.label_retorno_inscricao.place(relx=0.717, rely=0.311, height=21, width = 154)
            self.label_retorno_inscricao.configure(activebackground="#f9f9f9")
            self.label_retorno_inscricao.configure(anchor='w')
            self.label_retorno_inscricao.configure(background="#FFFFFF")
            self.label_retorno_inscricao.configure(compound='left')
            self.label_retorno_inscricao.configure(disabledforeground="#a3a3a3")
            self.label_retorno_inscricao.configure(foreground="#000000")
            self.label_retorno_inscricao.configure(highlightbackground="#d9d9d9")
            self.label_retorno_inscricao.configure(highlightcolor="black")
            self.label_retorno_inscricao.configure(relief="sunken")

            top.mainloop()

        def retorna_cadastro(self):
            self.top.destroy()
            tela_cadastro.cadastro()
            
        def consulta_cadastro(self):
            chave_consulta = self.entry_cpf_cnpj.get()
            consulta = f"SELECT nome FROM cliente_fisicos WHERE cpf = {chave_consulta}"
            cursor.execute(consulta)
            nome = cursor.fetchone()
            self.label_retorno_nome.configure(text=nome)

            consulta = f"SELECT cpf FROM cliente_fisicos WHERE cpf = {chave_consulta}"
            cursor.execute(consulta)
            cpf = cursor.fetchone()
            self.label_retorno_cpf.configure(text=cpf)

            consulta = f"SELECT nascimento FROM cliente_fisicos WHERE cpf = {chave_consulta}"
            cursor.execute(consulta)
            nascimento = cursor.fetchone()
            self.label_retorno_nascimento.configure(text=nascimento)

            consulta = f"SELECT telefone FROM cliente_fisicos WHERE cpf = {chave_consulta}"
            cursor.execute(consulta)
            telefone = cursor.fetchone()
            self.label_retorno_telefone.configure(text=telefone)

            consulta = f"SELECT email FROM cliente_fisicos WHERE cpf = {chave_consulta}"
            cursor.execute(consulta)
            email = cursor.fetchone()
            self.label_retorno_email.configure(text=email)

            consulta = f"SELECT cep FROM cliente_fisicos WHERE cpf = {chave_consulta}"
            cursor.execute(consulta)
            cep = cursor.fetchone()
            self.label_retorno_cep.configure(text=cep)

            consulta = f"SELECT nome FROM cliente_juridicos WHERE cnpj = {chave_consulta}"
            cursor.execute(consulta)
            nome = cursor.fetchone()
            self.label_retorno_nome.configure(text=nome)

            consulta = f"SELECT nascimento FROM cliente_juridicos WHERE cnpj = {chave_consulta}"
            cursor.execute(consulta)
            nascimento = cursor.fetchone()
            self.label_retorno_nascimento.configure(text=nascimento)

            consulta = f"SELECT telefone FROM cliente_juridicos WHERE cnpj = {chave_consulta}"
            cursor.execute(consulta)
            telefone = cursor.fetchone()
            self.label_retorno_telefone.configure(text=telefone)

            consulta = f"SELECT email FROM cliente_juridicos WHERE cnpj = {chave_consulta}"
            cursor.execute(consulta)
            email = cursor.fetchone()
            self.label_retorno_email.configure(text=email)

            consulta = f"SELECT cep FROM cliente_juridicos WHERE cnpj = {chave_consulta}"
            cursor.execute(consulta)
            cep = cursor.fetchone()
            self.label_retorno_cep.configure(text=cep)

            consulta = f"SELECT cnpj FROM cliente_juridicos WHERE cnpj = {chave_consulta}"
            cursor.execute(consulta)
            cnpj = cursor.fetchone()
            self.label_retorno_cnpj.configure(text=cnpj)

            consulta = f"SELECT inscricao FROM cliente_juridicos WHERE cnpj = {chave_consulta}"
            cursor.execute(consulta)
            inscricao = cursor.fetchone()
            self.label_retorno_inscricao.configure(text=inscricao)

        def nova_consulta(self):
            self.entry_cpf_cnpj.delete(0, END)
            self.label_retorno_nome.configure(text='')
            self.label_retorno_cpf.configure(text='')
            self.label_retorno_nascimento.configure(text='')
            self.label_retorno_telefone.configure(text='')
            self.label_retorno_email.configure(text='')
            self.label_retorno_cep.configure(text='')
            self.label_retorno_cnpj.configure(text='')
            self.label_retorno_inscricao.configure(text='')


    Tela_consulta_cliente()
