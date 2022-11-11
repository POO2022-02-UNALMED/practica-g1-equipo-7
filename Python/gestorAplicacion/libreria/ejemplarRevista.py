from ejemplar import Ejemplar
from estadoEjemplar import EstadoEjemplar
from revista import Revista


class EjemplarRevista(Ejemplar):
    def __init__(self, identificador: int, estadoEjemplar: EstadoEjemplar, revista: Revista):
        super().__init__(identificador, estadoEjemplar)
        self._identificador = identificador
        self._estadoEjemplar = estadoEjemplar
        self._revista = revista

    def getRevista(self) -> Revista:
        return self._revista