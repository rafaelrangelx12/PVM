from tkinter import *
from tkinter import messagebox
from addproduct import Productos

class seleccion:
	def menu(self, usuario):
		MenuTk = Tk()
		MenuTk.title("Menu principal.")
		MenuTk.geometry("350x200")

		lbl = Label(MenuTk, text = "Bienvenido: " + usuario)
		lbl.grid(column = 0, row = 0)

		def clickadd():
			MisProductos = Productos()
			MisProductos.ventanaprincipal(usuario)

		def clicklist():
			messagebox.showwarning("Inaccesible", "Sistema aun en desarrollo")

		btnadd = Button(MenuTk, text = "Añadir producto.", command = clickadd)
		btnadd.grid(column = 0, row = 1)
		btnlist = Button(MenuTk, text = "Lista de productos.", command = clicklist)
		btnlist.grid(column = 1, row = 1)

		MenuTk.mainloop()
