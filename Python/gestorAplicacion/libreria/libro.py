from Python.gestorAplicacion.libreria.titulo import Titulo
import tkinter as tk
from tkinter import *

class Libro(Titulo):
    def __init__(self, nombre, autor, ISBN, genero):
        super().__init__(nombre, autor, ISBN)
        self._genero = genero

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero


    @classmethod
    def masSolicitados(cls, biblioteca, genero):
        libros = []
        nombresLibros = []
        for libro in biblioteca.getHistorialLibrosUsados():
            if libro.getGenero() == genero and libro.getNombre() not in nombresLibros:
                libros.append(libro)
                nombresLibros.append(libro.getNombre())

        return libros


    def __str__(self):
        return(f"{self.getNombre()}  {self.getAutor()}")