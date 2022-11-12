from titulo import Titulo
from categoria import CATEGORIA
from random import randint

class Revista(Titulo):
    def __init__(self, nombre = "Independiente", autor = "Escritor anonimo", ISBN = randint(10000,99999), categoria = CATEGORIA.ACTUALIDAD):
        super().__init__(nombre, autor, ISBN)
        self._categoria = categoria

    def getCategoria(self) -> CATEGORIA:
        return self._categoria

    def setCategoria(self, categoria: CATEGORIA):
        self._categoria = categoria

