import random
import tkinter as tk
from datetime import datetime, timedelta

from Python.gestorAplicacion.servicios.servicio import Servicio
from Python.gestorAplicacion.servicios.tiquete import Tiquete



class Reserva(Servicio):
    def __init__(self, usuario, ejemplar, tituloEscogido, fechaReserva, fechaDevolucion):
        super(Reserva, self).__init__(usuario, ejemplar, tituloEscogido)
        self._fechaReserva = fechaReserva
        self._fechaDevolucion = fechaDevolucion

    #getters y setters
    def getFechaReserva(self):
        return self._fechaReserva

    def getFechaDevolucion(self):
        return self._fechaDevolucion

    def setFechaReserva(self, fecha):
        self._fechaReserva = fecha

    def setFechaDevolucion(self, fecha):
        self._fechaDevolucion = fecha

    """* Esta función lo que hace es añadir la reserva al usuario (en la fecha correspondiente), genera un
       tiquete y actualiza el estado del libro que este reservó
     * @param usuario Usuario al cual se le va a generar la reserva
     * @param ejemplarLibroReservado Libro que se va a reservar
     * @param biblioteca Biblioteca que contiene los ejemplares disponibles para reservar
     * @param fecha_reserva Fecha en la que se realizo la reserva
     * @param fecha_devolucion Fecha en la que se debe devolver la revista"""
    @classmethod
    def generarReservaLibro(cls, usuario, ejemplarLibroReservado, biblioteca, fechaReserva, fechaDevolucion):
        reserva = Reserva(usuario, ejemplarLibroReservado, ejemplarLibroReservado.getLibro(), fechaReserva, fechaDevolucion)
        idReserva = random.randint(0, 10000)
        tiquete = Tiquete(reserva, idReserva)
        reserva.setTiquete(tiquete)
        ejemplarLibroReservado.getEstadoEjemplar().setReserva(reserva)
        ejemplarLibroReservado.getEstadoEjemplar().setReservado(True)

        #Se agrega al historial
        biblioteca.añadirHistorialLibrosUsados(ejemplarLibroReservado.getLibro())
        usuario.añadirHistorialLibros(ejemplarLibroReservado.getLibro())
        ejemplarLibroReservado.getLibro().usado()

        #Eliminar disponible Recuerda poner un metodo para eliminar de esa lista, Igual en prestamos!!!!!!
        Servicio.eliminarDeLibrosDisponibles(ejemplarLibroReservado)
        usuario.añadirReserva(reserva)
        usuario.añadirTiquete(tiquete)

    """* Esta función lo que hace es añadir la reserva al usuario (en la fecha correspondiente), genera un
       tiquete y actualiza el estado del libro que este reservó
     * @param usuario Usuario al cual se le va a generar la reserva 
     * @param ejemplarRevistaReservada Revista reservada
     * @param biblioteca Biblioteca que contiene los ejemplares disponibles para reservar
     * @param fecha_reserva Fecha en la que se realizo la reserva
     * @param fecha_devolucion Fecha en la que se debe devolver la revista
     """
    @classmethod
    def generarReservaRevista(cls, usuario, ejemplarRevistaReservada, biblioteca , fechaReserva, fechaDevolucion):
        reserva = Reserva(usuario, ejemplarRevistaReservada, ejemplarRevistaReservada.getRevista(), fechaReserva, fechaDevolucion)
        idReserva = random.randint(0, 10000)
        tiquete = Tiquete(reserva, idReserva)
        reserva.setTiquete(tiquete)
        ejemplarRevistaReservada.getEstadoEjemplar().setReserva(reserva)
        ejemplarRevistaReservada.getEstadoEjemplar().setReservado(True)

        #Se agrega al historial
        biblioteca.añadirHistorialRevistasUsadas(ejemplarRevistaReservada.getRevista())
        usuario.añadirHistorialRevistas(ejemplarRevistaReservada.getRevista())
        ejemplarRevistaReservada.getRevista().usado()

        #Eliminar disponible Recuerda poner un metodo para eliminar de esa lista, Igual en prestamos!!!!!!
        Servicio.eliminarDeRevistasDisponibles(ejemplarRevistaReservada)
        usuario.añadirReserva(reserva)
        usuario.añadirTiquete(tiquete)

    """* El usuario elige la reserva a cancelar, se busca la reserva y posteriormente se cambia el estado 
       de esta a 'FALSE'; de esta manera el servicio que estaba reservado vuelve a estar disponible. También
       se elimina el tiquete correspondiente a esa reserva (almacenado en la lista 'tiquetes')
     * @param indiceCancelarReserva Es la reserva que se desea cancelar
     * @param biblioteca Parametro necesario para el contexto de la funcionalidad
     * @param usuario Usuario al que se le va a afectuar la cancelacíon de la reserva 
     """
    @classmethod
    def cancelarReserva(cls, indiceCancelarReserva: int, biblioteca, usuario):
        reservaAEliminar = usuario.getReservas()[indiceCancelarReserva]
        tiqueteAEliminar = None

        for tiquete in usuario.getTiquetes():
            if tiquete.getServicio() == reservaAEliminar:
                tiqueteAEliminar = tiquete

        reservaAEliminar.getEjemplarEscogido().getEstadoEjemplar().setReservado(False)
        usuario.eliminarReserva(reservaAEliminar)
        usuario.eliminarTiquete(tiqueteAEliminar)

        biblioteca.añadirEjemplarRevista(reservaAEliminar.getEjemplarEscogido())

    def toString(self):
        return (self.mostrarTituloEscogido() + "Fecha reserva: " + self.getFechaReserva() + "Fecha devolucion: " + self.getFechaDevolucion())