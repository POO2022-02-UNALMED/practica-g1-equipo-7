from Python.gestorAplicacion.libreria.biblioteca import Biblioteca
from Python.gestorAplicacion.libreria.titulo import Titulo
from Python.gestorAplicacion.libreria.categoria import CATEGORIA

from random import randint

class Revista(Titulo):
    def __init__(self, nombre = "Independiente", autor = "Escritor anonimo", ISBN = randint(10000,99999), categoria = CATEGORIA.ACTUALIDAD.value):
        super().__init__(nombre, autor, ISBN)
        self._categoria = categoria

    def getCategoria(self):
        return self._categoria

    def setCategoria(self, categoria):
        self._categoria = categoria

    @classmethod
    def masSolicitadas(cls, biblioteca, categoria):
        revistas = []
        nombresRevistas = []
        for revista in Biblioteca.getHistorialRevistasUsadas():
            if revista.getCategoria() == categoria and revista.getNombre() not in nombresRevistas:
                revistas.append(revista)
                nombresRevistas.append(revista.getNombre())

        return revistas

