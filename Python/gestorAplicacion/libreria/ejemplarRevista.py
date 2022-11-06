from ejemplar import Ejemplar
from estadoEjemplar import EstadoEjemplar
from revista import Revista


class EjemplarRevista(Ejemplar):
    def __init__(self, id: int, estadoEjemplar: EstadoEjemplar, revista: Revista):
        super().__init__(id, estadoEjemplar)
        self._id = id
        self._estadoEjemplar = estadoEjemplar
        self._revista = revista

    def getRevista(self) -> Revista:
        return self._revista