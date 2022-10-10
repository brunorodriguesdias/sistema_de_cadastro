from tkinter import *
from tkinter import ttk

root =Tk()
root.title('Sistema de cliente')
root.geometry('900x500')

usuario = Entry()
usuario.grid(row=0, column=0)
senha = Entry()
senha.grid(row=1, column=0)

Button(text='Login').grid(row=2, column=0)

root.mainloop()