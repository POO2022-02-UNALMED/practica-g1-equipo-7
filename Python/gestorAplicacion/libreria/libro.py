from Python.gestorAplicacion.libreria.biblioteca import Biblioteca
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

    """
     * Esta función sirve para filtrar los libros más utilizados por gnereo (tomando en cuenta el historial de libros usados) 
     * @param biblioteca Biblioteca en la que se encuentran los libros a filtrar
     * @param genero Genero de los libros
     * @return Retorna los resultados que se encontraron compatibles con el filtro aplicado
     """
    @classmethod
    def masSolicitados(cls, biblioteca, genero):
        libros = []
        nombresLibros = []
        for libro in Biblioteca.getHistorialLibrosUsados():
            if libro.getGenero() == genero and libro.getNombre() not in nombresLibros:
                libros.append(libro)
                nombresLibros.append(libro.getNombre())

        return libros


    def __str__(self):
        return(f"{self.getNombre()}  {self.getAutor()}")