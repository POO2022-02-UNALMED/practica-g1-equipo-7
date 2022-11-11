from estadoEjemplar import EstadoEjemplar

class Ejemplar():
    def __init__(self, identificador: int, estadoEjemplar: EstadoEjemplar):
        self._identificador = identificador
        self._estadoEjemplar = estadoEjemplar

    def getIdentificador(self) -> int:
        return self._identificador

    def getEstadoEjemplar(self) -> EstadoEjemplar:
        return self._estadoEjemplar
