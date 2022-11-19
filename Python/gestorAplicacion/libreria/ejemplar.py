

class Ejemplar():
    def __init__(self, identificador: int, estadoEjemplar):
        self._identificador = identificador
        self._estadoEjemplar = estadoEjemplar

    def getIdentificador(self) -> int:
        return self._identificador

    def getEstadoEjemplar(self):
        return self._estadoEjemplar
