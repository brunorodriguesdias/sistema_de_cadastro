from tkinter import *
import tkinter as tk


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

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
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

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.304, rely=0.308, height=20, relwidth=0.415)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry2 = tk.Entry(self.Frame1, show='*')
        self.Entry2.place(relx=0.304, rely=0.615, height=20, relwidth=0.415)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="black")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(selectbackground="#c4c4c4")
        self.Entry2.configure(selectforeground="black")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.38, rely=0.051, height=21, width=114)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#ebfdfe")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {SimSun} -size 15")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Bem vindo''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.101, rely=0.308, height=21, width=64)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(anchor='w')
        self.Label2.configure(background="#ebfdfe")
        self.Label2.configure(compound='left')
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {SimSun} -size 12")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Usuario:''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.127, rely=0.615, height=21, width=54)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(anchor='w')
        self.Label3.configure(background="#ebfdfe")
        self.Label3.configure(compound='left')
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {SimSun} -size 12")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Senha:''')

        self.Button2 = tk.Button(self.Frame1, command=self.verifica_cadastro)
        self.Button2.place(relx=0.405, rely=0.769, height=24, width=87)
        self.Button2.configure(activebackground="beige")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#dbf3fd")
        self.Button2.configure(compound='left')
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {SimSun} -size 12")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Login''')
        top.mainloop()
    def verifica_cadastro(self):
        usuario_correto = 'admin'
        senha_correta = '1234'

        if (self.Entry1.get() == 'admin' and self.Entry2.get() == '1234'):
            print('Usuario logado')
            self.top.destroy()
            self.sistema_cadastro()
        else:
           print('Dados incorretos')

    def sistema_cadastro(self):
        root = tk.Tk()
        root.title('Sistema de cadastro')
        root.mainloop()

Toplevel1()