from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymongo
myclient= pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["tg_DAta"]
mycol1 = mydb["Provincia"]
mycol2 = mydb["Canton"]
mycol3 = mydb["Parroquia"]
mycol4 = mydb["Colegio"]
collist = mydb.list_collection_names()
def metodoProvincia(tree):
    for row in mycol1.find():
        tree.insert('',END,text=row["_id"],values=row["Sec"])

def metodoCanton(tree):
    for documento in mycol2.find():
        tree.insert('',END,text=documento["_id"],values=documento["Sec"])
def metodoParroquia(tree):
    for documento in mycol3.find():
        tree.insert('',END,text=documento["_id"],values=documento["Sec"])
def metodoColegio(tree):
    for documento in mycol4.find():
        tree.insert('',END,text=documento["_id"],values=documento["Sec"])
    
def guardar(texto1,texto2,texto3,texto4,texto5,texto6):
    mydict = { "Sec": texto1, "Campo ": texto2,"Descripcion de campo ":texto3,"Tipo de dato":texto4,"Tamaño":texto5,"Indice(Clave)":texto6}
    ingresoDato= mycol2.insert_one(mydict)
root=Tk()
root.title("Base de datos MIES")
root.geometry('1080x500')
root.config(cursor="pencil")

#Caja de texto para subir los documentos mencionados
titulo=Label(root,text="Sec: ")
titulo.place(x=30,y=250)
texto1=Entry(root)
texto1.place(x=190,y=250)
titulo=Label(root,text="Campo: ")
titulo.place(x=30,y=290)
texto2=Entry(root)
texto2.place(x=190,y=290)
titulo=Label(root,text="Descripcion de campo: ")
titulo.place(x=30,y=330)
texto3=Entry(root)
texto3.place(x=190,y=330)
titulo=Label(root,text="Tipo de dato: ")
titulo.place(x=400,y=250)
texto4=Entry(root)
texto4.place(x=500,y=250)
titulo=Label(root,text="Tamaño: ")
titulo.place(x=400,y=290)
texto5=Entry(root)
texto5.place(x=500,y=290)
titulo=Label(root,text="Indice(Clave): ")
titulo.place(x=400,y=330)
texto6=Entry(root)
texto6.place(x=500,y=330)


tree=ttk.Treeview(height=10, columns=('#0','#1','#2','#3','#4','#5'))
tree.place(x=100, y=10)
tree.column('#0',width=250)
tree.heading('#0', text="ID", anchor=CENTER)
tree.column('#1', width=35)
tree.heading('#1', text="Sec", anchor=CENTER)
tree.column('#2', width=45)
tree.heading('#2', text="Campo", anchor=CENTER)
tree.heading('#3', text="Descripcion del campo", anchor=CENTER)
tree.column('#3', width=200)
tree.heading('#4', text="Tipo de dato", anchor=CENTER)     
tree.heading('#5', text="Tamaño", anchor=CENTER)
tree.column('#5', width=50)
tree.heading('#6', text="Clave", anchor=CENTER)
tree.column('#6', width=50)
#Botones de las diferentes tablas
boton1=Button(root,text="Provincia",command=lambda:metodoProvincia(tree))
boton1.place(x=0,y=10)
boton1=Button(root,text="Canton   ",command=lambda:metodoCanton(tree))
boton1.place(x=0,y=50)
boton1=Button(root,text="Parroquia",command=lambda:metodoParroquia(tree))
boton1.place(x=0,y=90)
boton1=Button(root,text="Colegio  ",command=lambda:metodoColegio(tree))
boton1.place(x=0,y=130)

boton2=Button(root,text="Guardar",command=lambda:guardar(texto1.get(),texto2.get(),texto3.get(),texto4.get(),texto5.get(),texto6.get()))
boton2.place(x=100,y=400)
boton2=Button(root,text="Eliminar",command=lambda:guardar(texto1.get(),texto2.get(),texto3.get(),texto4.get(),texto5.get(),texto6.get()))
boton2.place(x=300,y=400)
boton2=Button(root,text="Crear",command=lambda:guardar(texto1.get(),texto2.get(),texto3.get(),texto4.get(),texto5.get(),texto6.get()))
boton2.place(x=500,y=400)
root.mainloop()



