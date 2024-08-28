from tkinter import *

#iniciar tkinter
aplicacion = Tk()

#tamaño de la ventana
aplicacion.geometry("1020x630+0+0")

#evitar maximizar
aplicacion.resizable(0,0) #Ni en eje x ni y puede ampliar o reducir

#titulo de la venta
aplicacion.title("Mi restaurante - Sistema de facturacion")

#Color de fondo de la venta
aplicacion.config(bg="burlywood") #Hay una pagina en internet de los colores y nombres en tkinter


#Panel superior
panel_superior = Frame(aplicacion,bd=1,relief=FLAT)
panel_superior.pack(side=TOP)
#Titulo etiqueta
etiqueta_titulo = Label(panel_superior,text="Sistema de facturacion", fg="azure4",
                        font=("Dosis",58), bg="black",width=27)
etiqueta_titulo.grid(row=0,column=0)
#Evitar que la pantalla se cierre
aplicacion.mainloop()