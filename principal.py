
from tkinter import ttk
from tkinter import *



from ebook import Ebook

if __name__ == '__main__':
    ventana = Tk()
    aplicacion = Ebook(ventana)
    
    ventana.mainloop()