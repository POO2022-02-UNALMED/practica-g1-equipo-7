from Python.gestorAplicacion.servicios.prestamo import Prestamo
from Python.gestorAplicacion.servicios.reserva import Reserva

class EstadoEjemplar():
    def __init__(self, prestado: bool, reservado: bool, retraso: bool, prestamo: Prestamo, reserva: Reserva):
        self._prestado = prestado
        self._reservado = reservado
        self._retraso = retraso
        self._prestamo = prestamo
        self._reserva = reserva

    def isPrestado(self) -> bool:
        return self._prestado

    def isReservado(self) -> bool:
        return self._reservado

    def isRetraso(self) -> bool:
        return self._retraso

    def getPrestamo(self) -> Prestamo:
        return self._prestamo

    def getReserva(self) -> Reserva:
        return self._reserva

    def setPrestado(self, prestado: bool):
        self._prestado = prestado

    def setReservado(self, reservado: bool):
        self._reservado = reservado

    def setRetraso(self, retraso: bool):
        self._retraso = retraso

    def setPrestamo(self, prestamo: Prestamo):
        self._prestamo = prestamo

    def setReserva(self, reserva: Reserva):
        self._reserva = reserva
