import pymysql
from tkinter import *
from tkinter import messagebox
from menu import seleccion

class Login:

	def consulta(self, username, pwd):
		try:
			conexion = pymysql.connect(host='localhost',
										user = 'root', 
										password = '', 
										db = 'spv')
			try:
				with conexion.cursor() as cursor:
					consulta = "SELECT * FROM usuarios WHERE username = %s AND pwd = %s;"
					cursor.execute(consulta, [username, pwd])
					cuenta = cursor.fetchone()
					if cuenta:
						#Aqui pasara a otra ventana
						msj = [2, "Bienvenido al sistema"]
						return msj
					else:
						msj = [0, "Error al ingresar, verifica tus credenciales"]
						return msj
				conexion.commit()
			finally:
				conexion.close()
		except(pymysql.err.OperationalError, pymysql.err.IntegrityError) as e:
			msj = [1, "Ocurrio un error al conectar " +e]
			return msj
		finally:
			print("Ok")


MiLogin = Login()
MiMenu = seleccion()

LoginTK = Tk()
LoginTK.title("Login del sistema.")
LoginTK.geometry("350x200")

lbl1 = Label(LoginTK, text = "Usuario:")
lbl1.grid(column = 0, row = 0)
lbl2 = Label(LoginTK, text = "Contraseña:")
lbl2.grid(column = 0, row = 1)

txtusuario = Entry(LoginTK, width = 30)
txtusuario.grid(column = 1, row = 0)
txtpwd = Entry(LoginTK, show = "*", width = 30)
txtpwd.grid(column = 1, row = 1)

def clicklog():
	usuario = txtusuario.get()
	pwd = txtpwd.get()
	response = MiLogin.consulta(usuario, pwd)
	if(response[0] == 0):
		messagebox.showerror('Error en el sistema.', response[1])
	elif(response[0] == 1):
		messagebox.showerror("Error en el sistema.", response[1])
	elif(response[0] == 2):
		messagebox.showinfo("Sistema.", response[1])
		LoginTK.destroy()
		MiMenu.menu(usuario)

btnlog = Button(LoginTK, text = "Iniciar sesion.", command = clicklog)
btnlog.grid(column = 0, row = 2)

LoginTK.mainloop()