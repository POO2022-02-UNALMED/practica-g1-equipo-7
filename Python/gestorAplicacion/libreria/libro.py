from Python.gestorAplicacion.libreria.titulo import Titulo


class Libro(Titulo):
    def __init__(self, nombre, autor, ISBN, genero):
        super().__init__(nombre, autor, ISBN)
        self._genero = genero

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero


    @classmethod
    def filtrarLibros(cls, filtro: str, palabra: str, biblioteca):
        pass


