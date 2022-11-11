import random

from Python.gestorAplicacion.libreria.biblioteca import Biblioteca
from Python.gestorAplicacion.libreria.ejemplar import Ejemplar
from Python.gestorAplicacion.libreria.ejemplarLibro import EjemplarLibro
from Python.gestorAplicacion.libreria.ejemplarRevista import EjemplarRevista
from Python.gestorAplicacion.libreria.titulo import Titulo
from Python.gestorAplicacion.servicios.servicio import Servicio
from Python.gestorAplicacion.servicios.tiquete import Tiquete
from Python.gestorAplicacion.servicios.usuario import Usuario
from datetime import datetime


class Prestamo(Servicio):
    def __init__(self, usuario: Usuario, ejemplar: Ejemplar, tituloEscogido: Titulo, fecha):
        super(Prestamo, self).__init__(usuario, ejemplar, tituloEscogido)
        self._fecha = fecha

    #getters y setters
    def getFecha(self):
        return self._fecha

    def setFecha(self,fecha):
        self._fecha = fecha

    def generarPrestamoLibro(self, usuario: Usuario, ejemplarPrestado: EjemplarLibro, biblioteca: Biblioteca):
        prestamo = Prestamo(usuario, ejemplarPrestado, ejemplarPrestado.getLibro(), datetime.now())
        id_prestamo = random.randint(0,10000)
        tiquete = Tiquete(prestamo, id_prestamo)
        prestamo.setTiquete(tiquete)
        ejemplarPrestado.getEstadoEjemplar().setPrestamo(prestamo)
        ejemplarPrestado.getEstadoEjemplar().setPrestado(True)

        #Se agrega al historial de libros usados de biblioteca y usuario
        biblioteca.añadirHistorialLibrosUsados(ejemplarPrestado.getLibro())
        usuario.añadirHistorialLibros(ejemplarPrestado.getLibro())
        ejemplarPrestado.getLibro().usado()

        #se remueve de disponibles
        Servicio.eliminarDeLibrosDisponibles(ejemplarPrestado)
        usuario.añadirPrestamo(prestamo)
        usuario.añadirTiquete(tiquete)

    def generarPrestamoRevista(self, usuario: Usuario, ejemplarPrestado: EjemplarRevista, biblioteca: Biblioteca):
        prestamo = Prestamo(usuario, ejemplarPrestado, ejemplarPrestado.getRevista(), datetime.now())
        id_prestamo = random.randint(0,10000)
        tiquete = Tiquete(prestamo, id_prestamo)
        prestamo.setTiquete(tiquete)
        ejemplarPrestado.getEstadoEjemplar().setPrestamo(prestamo)
        ejemplarPrestado.getEstadoEjemplar().setPrestado(True)

        #Se agrega al historial de libros usados de biblioteca y usuario
        biblioteca.añadirHistorialRevistasUsadas(ejemplarPrestado.getRevista())
        usuario.añadirHistorialRevistas(ejemplarPrestado.getRevista())
        ejemplarPrestado.getRevista().usado()

        #se remueve de disponibles
        Servicio.eliminarDeRevistasDisponibles(ejemplarPrestado)
        usuario.añadirPrestamo(prestamo)
        usuario.añadirTiquete(tiquete)

    def devolucion(self, indiceDevolcion: int, biblioteca:Biblioteca, usuario: Usuario):
        prestamoAEliminar = usuario.getPrestamos()[indiceDevolcion]
        tiqueteAEliminar = None

        for tiquete in usuario.getTiquetes():
            if tiquete.getServicio() == prestamoAEliminar:
                tiqueteAEliminar = tiquete

        prestamoAEliminar.getEjemplarEscogido().getEstadoEjemplar().setPrestado(False)
        usuario.eliminarPrestamo(prestamoAEliminar)
        usuario.eliminarTiquete(tiqueteAEliminar)

    def toString(self):
        return self.mostrarTituloEscogido() + "Fecha prestamo: " + self.getFecha()