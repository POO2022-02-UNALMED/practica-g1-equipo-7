from ejemplar import Ejemplar
from estadoEjemplar import EstadoEjemplar
from libro import Libro

class EjemplarLibro(Ejemplar):
    def __init__(self, id: int, estadoEjemplar: EstadoEjemplar, libro: Libro):
        super(EjemplarLibro, self).__init__(id, estadoEjemplar)
        self._id = id
        self._estadoEjemplar = estadoEjemplar
        self._libro = libro

    def getLibro(self) -> Libro:
        return self._libro