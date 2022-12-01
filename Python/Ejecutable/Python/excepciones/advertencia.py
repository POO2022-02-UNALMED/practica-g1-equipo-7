from tkinter import messagebox

class Advertencia():
    def __init__(self, mensaje):
        self._mensaje = mensaje
        messagebox.showinfo(title = "Error", message=mensaje)