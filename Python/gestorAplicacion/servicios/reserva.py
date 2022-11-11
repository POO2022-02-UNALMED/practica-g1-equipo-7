import random

from Python.gestorAplicacion.libreria.biblioteca import Biblioteca
from Python.gestorAplicacion.libreria.ejemplar import Ejemplar
from Python.gestorAplicacion.libreria.ejemplarLibro import EjemplarLibro
from Python.gestorAplicacion.libreria.ejemplarRevista import EjemplarRevista
from Python.gestorAplicacion.libreria.titulo import Titulo
from Python.gestorAplicacion.servicios.servicio import Servicio
from Python.gestorAplicacion.servicios.tiquete import Tiquete
from Python.gestorAplicacion.servicios.usuario import Usuario


class Reserva(Servicio):
    def __init__(self, usuario: Usuario, ejemplar: Ejemplar, tituloEscogido: Titulo, fechaReserva, fechaDevolucion):
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

    def generarReservaLibro(self, usuario: Usuario, ejemplarLibroReservado: EjemplarLibro, biblioteca: Biblioteca, fechaReserva, fechaDevolucion):
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

    def generarReservaRevista(self, usuario: Usuario, ejemplarRevistaReservada: EjemplarRevista, biblioteca: Biblioteca, fechaReserva, fechaDevolucion):
        reserva = Reserva(usuario, ejemplarRevistaReservada, ejemplarRevistaReservada.getRevista(), fechaReserva, fechaDevolucion)
        idReserva = random.randint(0, 10000)
        tiquete = Tiquete(reserva, idReserva)
        reserva.setTiquete(tiquete)
        ejemplarRevistaReservada.getEstadoEjemplar().setReserva(reserva)
        ejemplarRevistaReservada.getEstadoEjemplar().setReservado(True)

        #Se agrega al historial
        biblioteca.añadirHistorialLibrosUsados(ejemplarRevistaReservada.getRevista())
        usuario.añadirHistorialRevistas(ejemplarRevistaReservada.getRevista())
        ejemplarRevistaReservada.getRevista().usado()

        #Eliminar disponible Recuerda poner un metodo para eliminar de esa lista, Igual en prestamos!!!!!!
        Servicio.eliminarDeRevistasDisponibles(ejemplarRevistaReservada)
        usuario.añadirReserva(reserva)
        usuario.añadirTiquete(tiquete)

    def cancelarReserva(self, indiceCancelarReserva: int, biblioteca: Biblioteca, usuario:Usuario):
        reservaAEliminar = usuario.getReservas()[indiceCancelarReserva]
        tiqueteAEliminar = None

        for tiquete in usuario.getTiquetes():
            if tiquete.getServicio() == reservaAEliminar:
                tiqueteAEliminar = tiquete

        reservaAEliminar.getEjemplarEscogido().getEstadoEjemplar.setReservado(False)
        usuario.eliminarPrestamo(reservaAEliminar)
        usuario.eliminarTiquete(tiqueteAEliminar)

    def toString(self):
        return (self.mostrarTituloEscogido() + "Fecha reserva: " + self.getFechaReserva() + "Fecha devolucion: " + self.getFechaDevolucion())