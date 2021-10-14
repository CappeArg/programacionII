from tkinter import ttk
from tkinter import *

class Ebook:
            def __init__(self,ventana):
                self.vent = ventana
                self.vent.title('E-Books Organizados!')
                
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
                
            #Tabla para visualizar los libros