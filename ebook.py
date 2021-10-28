from tkinter import ttk
from tkinter import *
import sqlite3

class Ebook:
            #creamos una propiedad con la base de datos
            bd_nombre= 'BD.db'
            
            #conexión a la base de datos
            def ejecutaConsulta(self, consulta, parametros = ()):
                with sqlite3.connect(self.bd_nombre) as conexion:
                    fila = conexion.cursor()
                    resultado = fila.execute(consulta,parametros)
                    conexion.commit()
                return resultado
            
            #Traer los libros
            def getLibros(self):
                
                #limpiamos todos los elementos que podrían llegar a existir en la tabla (eliminamos)
                registros=self.arbol.get_children()
                for elemento in registros:
                    self.arbol.delete(elemento)
                
                #consulta de registros en la base de datos    
                consulta='SELECT * FROM ebooks ORDER BY titulo ASC'
                filas_BD=self.ejecutaConsulta(consulta)
                #recorremos las filas para poder mostrarlas y completar la tabla
                for fila in filas_BD:
                    self.arbol.insert('',END,text=fila[0],values=(fila[1],fila[2],fila[3],fila[5],fila[4]))
                    # print(fila)
                    
            #función para validar el agregado de libros sin campos
            def validacion(self):
                return len(self.titulo.get()) != 0 and len(self.autor.get()) and len(self.descarga.get()) != 0
                
                

            #función para agregar libro al sistema
            def agregarLibro(self):
                if self.validacion():
                    consulta='INSERT INTO ebooks VALUES (NULL, ?, ?, ?, ?, ?)'
                    parametros=(self.titulo.get(), self.autor.get(), self.genero.get(), self.descripcion.get(), self.descarga.get())
                    self.ejecutaConsulta(consulta,parametros)
                    
                    #agregamos mensaje confirmando el guardado del libro
                    self.mensaje['text']= 'Libro {} agregado correctamente'.format(self.titulo.get())
                    
                    #limpiamos el formulario para próximo ingreso
                    self.titulo.delete(0,END)
                    self.autor.delete(0,END)
                    self.genero.delete(0,END)
                    self.descripcion.delete(0,END)
                    self.descarga.delete(0,END)
                else:
                    self.mensaje['text']='El título, autor y link de descarga son obligatorios'
                self.getLibros()

            #Eliminar libros
            def eliminarLibro(self):
                self.mensaje['text'] = ''
                if self.arbol.item(self.arbol.selection())['text']:
                    consulta='DELETE FROM ebooks WHERE titulo = ?'
                    self.mensaje['text'] = ''
                    # print(self.arbol.item(self.arbol.selection())['values'])
                    id = self.arbol.item(self.arbol.selection())['text']
                    consulta = 'DELETE FROM ebooks WHERE id = ?'
                    self.ejecutaConsulta(consulta, (id, ))
                    self.mensaje['text'] = 'Libro eliminado correctamente'
                    self.getLibros()
                else:
                    self.mensaje['text'] = 'Por favor seleccione un registro'
                    return
                
            #editar un libro
            def editarLibro(self):    
                self.mensaje['text']=''
                if  self.arbol.item(self.arbol.selection())['text']:
                    #creamos una variable para recuperar los valores a editar de cada campo
                    indice=self.arbol.item(self.arbol.selection())['text']
                    tituloanterior=self.arbol.item(self.arbol.selection())['values'][0]
                    autoranterior=self.arbol.item(self.arbol.selection())['values'][1]
                    generoanterior=self.arbol.item(self.arbol.selection())['values'][2]
                    descripcionanterior=self.arbol.item(self.arbol.selection())['values'][4]
                    linkanterior=self.arbol.item(self.arbol.selection())['values'][3]
                    #creamos una ventana con toplevel para editar el contenido
                    self.ventanaedicion=Toplevel()
                    self.ventanaedicion.title='Editar datos del ebook!'
                    #campos en la nueva ventana (se indican uno para mostrar el contenido anterior y otro para el nuevo valor)
                    Label(self.ventanaedicion, text='Titulo Anterior: ').grid(row=0,column=1)
                    Entry(self.ventanaedicion, textvariable=StringVar(self.ventanaedicion, value=tituloanterior), state='readonly').grid(row=0, column=2)
                    Label(self.ventanaedicion, text='Titulo Nuevo: '). grid(row=1, column=1)
                    nuevotitulo= Entry(self.ventanaedicion)
                    nuevotitulo.grid(row=1, column=2)
                    Label(self.ventanaedicion, text='Autor Anterior: ').grid(row=2,column=1)
                    Entry(self.ventanaedicion, textvariable=StringVar(self.ventanaedicion, value=autoranterior), state='readonly').grid(row=2, column=2)
                    Label(self.ventanaedicion, text='Autor Nuevo: '). grid(row=3, column=1)
                    nuevoautor= Entry(self.ventanaedicion)
                    nuevoautor.grid(row=3, column=2)
                    Label(self.ventanaedicion, text='Genero Anterior: ').grid(row=4,column=1)
                    Entry(self.ventanaedicion, textvariable=StringVar(self.ventanaedicion, value=generoanterior), state='readonly').grid(row=4, column=2)
                    Label(self.ventanaedicion, text='Genero Nuevo: '). grid(row=5, column=1)
                    nuevogenero= Entry(self.ventanaedicion)
                    nuevogenero.grid(row=5, column=2)
                    Label(self.ventanaedicion, text='Descripción Anterior: ').grid(row=6,column=1)
                    Entry(self.ventanaedicion, textvariable=StringVar(self.ventanaedicion, value=descripcionanterior), state='readonly').grid(row=6, column=2)
                    Label(self.ventanaedicion, text='Descripción Nueva: '). grid(row=7, column=1)
                    nuevadescripcion= Entry(self.ventanaedicion)
                    nuevadescripcion.grid(row=7, column=2)
                    Label(self.ventanaedicion, text='Link Anterior: ').grid(row=8,column=1)
                    Entry(self.ventanaedicion, textvariable=StringVar(self.ventanaedicion, value=linkanterior), state='readonly').grid(row=8, column=2)
                    Label(self.ventanaedicion, text='Link Nuevo: '). grid(row=9, column=1)
                    nuevolink= Entry(self.ventanaedicion)
                    nuevolink.grid(row=9, column=2)
                    
                    Button(self.ventanaedicion, text='Actualizar!!', command= lambda:self.editarRegistro(nuevotitulo.get(),
                                                                                                         indice,
                                                                                                         nuevoautor.get(),
                                                                                                         nuevogenero.get(),
                                                                                                         nuevadescripcion.get(),
                                                                                                         nuevolink.get())).grid(row=11, column=2, sticky=W+E)
                else:
                    self.mensaje['text'] = 'Por favor seleccione un registro'
                    return
                            
            def editarRegistro(self, nuevotitulo, indice, nuevoautor, nuevogenero, nuevadescripcion,
                               nuevolink):
                consulta = 'UPDATE ebooks SET titulo = ?, autor = ?, genero = ?, descripcion = ?, linkdesc = ? WHERE id = ?'
                parametros = (nuevotitulo,nuevoautor,nuevogenero,nuevadescripcion,nuevolink, indice)
                self.ejecutaConsulta(consulta,parametros)
                self.ventanaedicion.destroy()
                self.mensaje['text'] = 'El ebook ha sido actualizado correctamente'
                self.getLibros()

                    
                
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
                ttk.Button(contenedor, text="Guardar Libro!", command=self.agregarLibro).grid(row=4, column=3, pady=10)
                
            #Creamos un texto para visualizar la confirmación de operaciones (guardado de nuevos registros,eliminación, etc)
            
                self.mensaje = Label(text="", fg='green')
                self.mensaje.grid(row=5, column=2, columnspan=2, sticky= W + E)
                
            #Tabla para visualizar los libros
                self.arbol = ttk.Treeview(ventana,columns=("#1", "#2", "#3","#4",'#5'), selectmode="extended")
                self.arbol.grid(row=6, column=2)
                self.arbol.heading('#0',text="ID")
                self.arbol.heading('#1', text="TITULO")
                self.arbol.heading('#2', text="AUTOR")
                self.arbol.heading('#3', text="GENERO")
                self.arbol.heading('#4', text="DESCARGA")
                self.arbol.heading('#5', text="DESCRIPCION")
                
                
                self.getLibros()
            #Botones de Baja y Modificación
                ttk.Button(text="Borrar", command=self.eliminarLibro).grid(row=9, column=2,sticky=W+E)
                ttk.Button(text="Editar", command=self.editarLibro).grid(row=8, column=2,sticky=W+E)