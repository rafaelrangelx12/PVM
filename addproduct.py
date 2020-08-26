from tkinter import*
from tkinter import messagebox

class Productos:
    def ventanaprincipal(self):
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
            res="Esto se toma de la caja de texto : "+txt.get()
            lbl.configure(text=res)
        def cl_Msg():
            messagebox.showinfo('Sistema', 'Aquí va el texto del mensaje')

        #Botones
        btn= Button(window, text="Aceptar", command=clicked)
        btn.grid (column=1, row=3)

        window.mainloop()