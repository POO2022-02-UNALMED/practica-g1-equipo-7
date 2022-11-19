from Python.gestorAplicacion.libreria.ejemplar import Ejemplar



class EjemplarRevista(Ejemplar):
    def __init__(self, identificador: int, estadoEjemplar, revista):
        super().__init__(identificador, estadoEjemplar)
        self._identificador = identificador
        self._estadoEjemplar = estadoEjemplar
        self._revista = revista

    def getRevista(self):
        return self._revista