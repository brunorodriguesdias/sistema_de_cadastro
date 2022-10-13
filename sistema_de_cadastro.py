from tkinter import *
import tkinter as tk
import tela_cadastro


_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black'
_tabfg2 = 'black'
_tabbg1 = 'grey75'
_tabbg2 = 'grey89'
_bgmode = 'light'

class Tela_login():
    def __init__(self, top=None):
        top = tk.Tk()
        top.geometry("600x450+329+123")
        top.minsize(120, 1)
        top.maxsize(3290, 1061)
        top.resizable(1,  1)
        top.title("Login")
        top.configure(background="#dbf3fd")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.top = top

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.183, rely=0.222, relheight=0.433, relwidth=0.658)
        self.Frame1.configure(relief='raised')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="raised")
        self.Frame1.configure(background="#ebfdfe")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.usuario = tk.Entry(self.Frame1)
        self.usuario.place(relx=0.304, rely=0.308, height=20, relwidth=0.415)
        self.usuario.configure(background="white")
        self.usuario.configure(disabledforeground="#a3a3a3")
        self.usuario.configure(font="TkFixedFont")
        self.usuario.configure(foreground="#000000")
        self.usuario.configure(highlightbackground="#d9d9d9")
        self.usuario.configure(highlightcolor="black")
        self.usuario.configure(insertbackground="black")
        self.usuario.configure(selectbackground="#c4c4c4")
        self.usuario.configure(selectforeground="black")

        self.senha = tk.Entry(self.Frame1, show='*')
        self.senha.place(relx=0.304, rely=0.615, height=20, relwidth=0.415)
        self.senha.configure(background="white")
        self.senha.configure(disabledforeground="#a3a3a3")
        self.senha.configure(font="TkFixedFont")
        self.senha.configure(foreground="#000000")
        self.senha.configure(highlightbackground="#d9d9d9")
        self.senha.configure(highlightcolor="black")
        self.senha.configure(insertbackground="black")
        self.senha.configure(selectbackground="#c4c4c4")
        self.senha.configure(selectforeground="black")

        self.label_bem_vindo = tk.Label(self.Frame1)
        self.label_bem_vindo.place(relx=0.38, rely=0.051, height=21, width=114)
        self.label_bem_vindo.configure(activebackground="#f9f9f9")
        self.label_bem_vindo.configure(anchor='w')
        self.label_bem_vindo.configure(background="#ebfdfe")
        self.label_bem_vindo.configure(compound='left')
        self.label_bem_vindo.configure(disabledforeground="#a3a3a3")
        self.label_bem_vindo.configure(font="-family {SimSun} -size 15")
        self.label_bem_vindo.configure(foreground="#000000")
        self.label_bem_vindo.configure(highlightbackground="#d9d9d9")
        self.label_bem_vindo.configure(highlightcolor="black")
        self.label_bem_vindo.configure(text='''Bem vindo''')

        self.label_usuario = tk.Label(self.Frame1)
        self.label_usuario.place(relx=0.101, rely=0.308, height=21, width=64)
        self.label_usuario.configure(activebackground="#f9f9f9")
        self.label_usuario.configure(anchor='w')
        self.label_usuario.configure(background="#ebfdfe")
        self.label_usuario.configure(compound='left')
        self.label_usuario.configure(disabledforeground="#a3a3a3")
        self.label_usuario.configure(font="-family {SimSun} -size 12")
        self.label_usuario.configure(foreground="#000000")
        self.label_usuario.configure(highlightbackground="#d9d9d9")
        self.label_usuario.configure(highlightcolor="black")
        self.label_usuario.configure(text='''Usuario:''')

        self.label_senha = tk.Label(self.Frame1)
        self.label_senha.place(relx=0.127, rely=0.615, height=21, width=54)
        self.label_senha.configure(activebackground="#f9f9f9")
        self.label_senha.configure(anchor='w')
        self.label_senha.configure(background="#ebfdfe")
        self.label_senha.configure(compound='left')
        self.label_senha.configure(disabledforeground="#a3a3a3")
        self.label_senha.configure(font="-family {SimSun} -size 12")
        self.label_senha.configure(foreground="#000000")
        self.label_senha.configure(highlightbackground="#d9d9d9")
        self.label_senha.configure(highlightcolor="black")
        self.label_senha.configure(text='''Senha:''')

        self.button_login = tk.Button(self.Frame1, command=self.verifica_cadastro)
        self.button_login.place(relx=0.405, rely=0.769, height=24, width=87)
        self.button_login.configure(activebackground="beige")
        self.button_login.configure(activeforeground="black")
        self.button_login.configure(background="#dbf3fd")
        self.button_login.configure(compound='left')
        self.button_login.configure(disabledforeground="#a3a3a3")
        self.button_login.configure(font="-family {SimSun} -size 12")
        self.button_login.configure(foreground="#000000")
        self.button_login.configure(highlightbackground="#d9d9d9")
        self.button_login.configure(highlightcolor="black")
        self.button_login.configure(pady="0")
        self.button_login.configure(text='''Login''')
        top.mainloop()
    def verifica_cadastro(self):
        usuario_correto = 'admin'
        senha_correta = '1234'

        if (self.usuario.get() == usuario_correto and self.senha.get() == senha_correta):
            print('Usuario logado')
            self.top.destroy()
            self.sistema_cadastro()
        else:
           print('Dados incorretos')

    def sistema_cadastro(self):
        tela_cadastro.cadastro()

Tela_login()