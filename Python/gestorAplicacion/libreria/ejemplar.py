from estadoEjemplar import EstadoEjemplar

class Ejemplar():
    def __init__(self, id: int, estadoEjemplar: EstadoEjemplar):
        self._id = id
        self._estadoEjemplar = estadoEjemplar

    def getId(self) -> int:
        return self._id

    def getEstadoEjemplar(self) -> EstadoEjemplar:
        return self._estadoEjemplar
