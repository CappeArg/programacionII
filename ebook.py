from tkinter import ttk
from tkinter import *

class Ebook:
            #creamos una propiedad con la base de datos
            bd_nombre= 'BD.db'
            
            def __init__(self,ventana):
                self.vent = ventana
                self.vent.title('E-Books Organizados!')
                self.vent.iconbitmap("book-bookmark-icon_34486.ico")

                
                
            #creamos un contenedor
                contenedor = LabelFrame(self.vent, text= 'Guarda un nuevo e-book!!')
                contenedor.grid(row=0, column=0, columnspan=3, pady=30)

            
            #creamos un input para titulo    
                Label(contenedor, text= 'Título').grid(row=1, column=0, pady=5)
                self.titulo= Entry(contenedor)
                self.titulo.focus()
                self.titulo.grid(row=1, column=1)
            #creamos otro input para el autor
                Label(contenedor, text='Autor/a').grid(row=2,column=0, pady=5)
                self.autor=Entry(contenedor)
                self.autor.grid(row=2,column=1)                
            #creamos un combobox editable para el genero
                Label(contenedor, text='Género').grid(row=1,column=3, pady=5)
                self.genero=ttk.Combobox(contenedor,values=["Novela",
                                         "Poesía",
                                         "Libro de Estudio",
                                         "Cuentos",
                                         "Libro de Habilidades!"])
                self.genero.grid(row=1,column=4, pady=5)                
            #creamos  input para la descripción
                Label(contenedor, text='Descripción').grid(row=2,column=3, pady=5)
                self.descripcion=Entry(contenedor)
                self.descripcion.grid(row=2,column=4)                
            
            #creamos otro input para el link de descarga
                Label(contenedor, text='Descarga').grid(row=3,column=3, pady=5)
                self.descarga=Entry(contenedor)
                self.descarga.grid(row=3,column=4, pady=5)                
                
            #Finalmente agregamos el botón para guardar el libro
                ttk.Button(contenedor, text="Guardar Libro!").grid(row=4, column=3, pady=10)
                
            #Creamos un texto para visualizar la confirmación de operaciones (guardado de nuevos registros,eliminación, etc)
            
                self.mensaje = Label(text="Mensaje de información", fg='blue')
                self.mensaje.grid(row=5, column=2, columnspan=2, sticky= W + E)
                
            #Tabla para visualizar los libros
                self.arbol = ttk.Treeview(ventana,height=10, columns=("#1", "#2", "#3","#4"), selectmode="extended")
                self.arbol.grid(row=6, column=2, columnspan=1)
                self.arbol.heading('#0',text="TITULO")
                self.arbol.heading('#1', text="AUTOR")
                self.arbol.heading('#2', text="GENERO")
                self.arbol.heading('#3', text="DESCARGA")
                self.arbol.heading('#4', text="DESCRIPCION")
               

                
            #Botones de Baja y Modificación
                ttk.Button(text="Borrar").grid(row=7, column=3,pady=10,padx=10)
                ttk.Button(text="Editar").grid(row=7, column=4,pady=10,padx=10)