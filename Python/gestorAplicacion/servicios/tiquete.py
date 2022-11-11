from Python.gestorAplicacion.servicios.servicio import Servicio


class Tiquete():
    def __init__(self, servicio: Servicio, id: int):
        self._servicio = servicio
        self._id = id

    #getters y setters
    def getId(self):
        return self._id

    def getServicio(self):
        return self._servicio

    def setId(self, id: int):
        self._id = id

    def setServicio(self, servicio: Servicio):
        self._servicio = servicio