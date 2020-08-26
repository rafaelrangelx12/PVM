from tkinter import*
from tkinter import messagebox
import pymysql

class Productos:
	def ventanaprincipal(self, usuario):
		window= Tk()
		window.geometry('350x200')
		window.configure(bg="#49A")
		window.title ("Registro De Productos")

		#Etiquetas
		lbl=Label (window, text="Nombre: ")
		lbl.grid(column=0, row=0,)
		lbl1=Label (window, text="Existencia:  ")
		lbl1.grid(column=0, row=1)
		lbl2=Label (window, text="Precio:  ")
		lbl2.grid(column=0, row=2)

		#Cuadros de Texto 
		txt=Entry (window, width=20)
		txt.grid (column=1, row=0)
		txt1=Entry (window, width=20)
		txt1.grid (column=1, row=1)
		txt2=Entry (window, width=20)
		txt2.grid (column=1, row=2)

		#Metodos
		def clicked():
			nombre = txt.get()
			existencia = txt1.get()
			price = txt2.get()

			MiProducto = Productos()
			response = MiProducto.consulta(nombre, existencia, price)
			if(response[0] == 1):
				messagebox.showerror("Error", response[1])
			elif(response[0] == 2):
				messagebox.showinfo("Sistema", response[1])
				window.destroy()
				
		def clickvolver():
			window.destroy()

		#Botones
		btn= Button(window, text="Guardar", command=clicked)
		btn.grid (column=1, row=3)
		btnvolver = Button(window, text = "Volver a la ventana anterior", command = clickvolver)
		btnvolver.grid(column = 2, row = 3)

		window.mainloop()
		
	def consulta(self, nombre, stock, dinero):
		try:
			conexion = pymysql.connect(host='localhost',
									user = 'root', 
									password = '', 
									db = 'spv')
			try:
				with conexion.cursor() as cursor:
					consulta = "INSERT INTO productos(nombre, existencias, precio) VALUES(%s, %s, %s);"

					cursor.execute(consulta, (nombre, stock, dinero))
				conexion.commit()
			finally:
				conexion.close()
		except(pymysql.err.OperationalError, pymysql.err.IntegrityError) as e:
			msj = [1, "Ocurrio un error al conectar " +e]
			return msj
		finally:
			msj = [2, "Exito al guardar el registro"]
			return msj