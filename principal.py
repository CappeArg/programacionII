from tkinter import ttk
from tkinter import *

import sqlite3

from ebook import Ebook

if __name__ == '__main__':
    ventana = Tk()
    aplicacion = Ebook(ventana)
    
    ventana.mainloop()