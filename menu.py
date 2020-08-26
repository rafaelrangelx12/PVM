from tkinter import *
from tkinter import messagebox

class seleccion:
	def menu(self, usuario):
		MenuTk = Tk()
		MenuTk.title("Menu principal.")
		MenuTk.geometry("350x200")

		lbl = Label(MenuTk, text = "Bienvenido: " + usuario)
		lbl.grid(column = 0, row = 0)

		btnadd = Button(MenuTk, text = "Añadir producto.")
		btnadd.grid(column = 0, row = 1)
		btnlist = Button(MenuTk, text = "Lista de productos.")
		btnlist.grid(column = 1, row = 1)

		MenuTk.mainloop()
