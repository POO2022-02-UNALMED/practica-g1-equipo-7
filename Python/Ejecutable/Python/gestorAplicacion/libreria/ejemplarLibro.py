
from Python.gestorAplicacion.libreria.ejemplar import Ejemplar


class EjemplarLibro(Ejemplar):
    def __init__(self, identificador: int, estadoEjemplar, libro):
        super(EjemplarLibro, self).__init__(identificador, estadoEjemplar)
        self._identificador = identificador
        self._estadoEjemplar = estadoEjemplar
        self._libro = libro

    def getLibro(self):
        return self._libro