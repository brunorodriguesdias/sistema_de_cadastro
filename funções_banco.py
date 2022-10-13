from tkinter import *
import tkinter as tk
import mysql.connector

banco = mysql.connector.connect(host='localhost', user='root',passwd='', database='lista_clientes')
cursor = banco.cursor()

insert_banco = 'INSERT into '