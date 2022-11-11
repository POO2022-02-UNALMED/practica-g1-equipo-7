from ejemplar import Ejemplar
from estadoEjemplar import EstadoEjemplar
from libro import Libro

class EjemplarLibro(Ejemplar):
    def __init__(self, identificador: int, estadoEjemplar: EstadoEjemplar, libro: Libro):
        super(EjemplarLibro, self).__init__(identificador, estadoEjemplar)
        self._identificador = identificador
        self._estadoEjemplar = estadoEjemplar
        self._libro = libro

    def getLibro(self) -> Libro:
        return self._libro