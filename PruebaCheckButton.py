from tkinter import *

root=Tk()

root.title("Ejemplo")

playa=IntVar()
montaña=IntVar()
turismoRural=IntVar()

def opcionesViaje():

	opcioneEscogida=""

	if(playa.get()==1):
		opcioneEscogida+=" playa"

	if(montaña.get()==1):
		opcioneEscogida+=" montaña"

	if(turismoRural.get()==1):
		opcioneEscogida+=" turismo rural"

	textoFinal.config(text=opcioneEscogida)


foto=PhotoImage(file="avion.png")
Label(root, image=foto).pack()


frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()


Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montaña, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Turismo rural", variable=turismoRural, onvalue=1, offvalue=0, command=opcionesViaje).pack()
textoFinal=Label(frame)
textoFinal.pack()



root.mainloop()