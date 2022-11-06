from titulo import Titulo
from genero import GENERO

class Libro(Titulo):
    def __init__(self, nombre, autor, ISBN, genero: GENERO):
        super().__init__(nombre, autor, ISBN)
        self._genero = genero

    def getGenero(self) -> GENERO:
        return self._genero

    def setGenero(self, genero: GENERO):
        self._genero = genero
