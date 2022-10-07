#Este proyecto me permitira llevar uan relación de los libros 
#que tengo que leer y saber en cualquier momento los libros
#que tengo pendientes por leer.

from this import s
from tkinter import *
from tkinter import messagebox

libros = []

def añadir():
    t = titulo.get()
    a = autor.get()
    e = editorial.get()
    np = Ndepaginas.get()
    f1 = fechalimite.get()
    libros.append(t+"$"+a+"$"+e+"$"+str(np)+"$ "+f1)
    escribirLibro()
    messagebox.showinfo("Guardado","El libro que tiene que leer ha sido guardado")
    titulo.set("")
    autor.set("")
    editorial.set("")
    Ndepaginas.set("")
    fechalimite.set("")
    consultar()

def escribirLibro():
    archivo=open("biblioteca.txt","w")
    libros.sort()
    for elemento in libros:
        archivo.write(elemento+"n")
    archivo.close()


def eliminarLibro():
    eliminado=eliminarlibro.get()
    removido=False
    for elemento in libros:
        arreglo = elemento.split("$")
    if eliminarlibro.get()==arreglo[0]:
        respuesta=messagebox.askyesno("Eliminar libro",
                         "Desea eliminar el libro con el titulo\n"+eliminado)
        if respuesta:
            libros.remove(elemento)
            removido = True
            escribirLibro()
            consultar()
            respuesta=""
    if removido: 
        messagebox.showinfo("Eliminar", "se ha eliminado el titulo\n"+eliminado)


def salir():
    sa=messagebox.askyesno("Salir","¿Deseas finalizar?") 
    if sa==True:
        quit()


def iniciarArchivo():
    archivo = open("biblioteca.txt","a")      
    archivo.close()


def cargar():
    archivo=open("biblioteca.txt","r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1]=='\n':
                linea=linea[:-1]
            libros.append(linea)
            linea=archivo.readline()
        archivo.close()

def consultar():
    r=Text(ventana,width=80,height=15) 
    libros.sort()
    valores=[]
    r.insert(INSERT,"\tTitulo del libro\n")
    r.insert(INSERT,"--------------------------------------------------------------------------------\
--------------------------\n")

    for elemento in libros:
        arreglo=elemento.split("$")
        valores.append(arreglo[0])
        r.insert(INSERT,"k"+arreglo[0]+"\n Autor:"+arreglo[1]+
                "tEditorial:"[2]+"\tN° de páginas:"+arreglo[3]+
                "\Fecha limite:"+arreglo[4]+"\n")
        r.insert(INSERT,"---------------------------\
-------------------------------------------\n")
    spinTitulo=Spinbox(ventana, value=(valores),
                       textvariable=eliminarlibro,width=50).place(x=110,y=450)
    r.place(x=30,y=195) 
    if libros==[]:

     r.config(state=DISABLED)


ventana = Tk()
titulo = StringVar()
autor = StringVar()
editorial = StringVar()
Ndepaginas = IntVar()
fechalimite = StringVar()
eliminarlibro = StringVar()    
colorFondo = "#006"
colorLetra = "#FFF"
iniciarArchivo()
cargar()
consultar()
ventana.title("Relación de los libros que tengo que leer")
ventana.geometry("700x500")
ventana.configure(background = colorFondo)
etiquetaTitulo = Label(ventana, text="Relación de libros\
         que tengo que leer",bg = colorFondo,fg = colorLetra).place(x=250, y=10)

eTitulo = Label(ventana, text="Titulo: ", bg = colorFondo\
                   ,fg = colorLetra).place(x=30,y=40)
cTitulo = Entry(ventana, textvariable=titulo,width=70).place(x=80 ,y=40)
eAutor = Label(ventana, text="Autor: ", bg = colorFondo,\
                  fg = colorLetra).place(x=30,y=70)
cAutor = Entry(ventana, textvariable=autor).place(x=120 ,y=70)                  
eEditorial = Label(ventana, text="Editorial: ",\
                     bg = colorFondo,fg = colorLetra).place(x=30,y=100)
cEditorial = Entry(ventana, textvariable=editorial).place(x=120, y=100)
eNpaginas = Label(ventana, text="N° de páginas: ",\
                  bg=colorFondo, fg=colorLetra). place (x=30, y=130) 

cNpaginas = Entry(ventana, textvariable=Ndepaginas).place(x=120,y=130)                  
botonAnadir= Button (ventana, text="Añadir libro",\
             command=añadir, bg="#009", fg="white") .place (x=580,y=38)

cFechaLimite=Entry (ventana, textvariable=fechalimite)\
.place (x=120,y=160)

eFechaLimite = Label(ventana, text="Fecha limite: ",\
               bg = colorFondo,fg = colorLetra).place(x=30,y=160)

spinTitulo=Label (ventana, text="Titulo leido:",\
    bg= colorFondo, fg= colorLetra) .place (x=20,y=450) 

botonLeido = Button (ventana,text="Libro ya leido",\
                     command=eliminarLibro, bg="#009",fg= "white").place (x=550,y=448)

imgbtn=PhotoImage (file="saliir.png")

sal =Button (ventana, image=imgbtn, command=salir) .place (x=300, y=60)

ventana.mainloop()




