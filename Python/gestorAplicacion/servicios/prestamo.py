import random

import tkinter as tk
from tkinter import *

from Python.gestorAplicacion.servicios.servicio import Servicio
from Python.gestorAplicacion.servicios.tiquete import Tiquete



from datetime import datetime
from Python.capaGrafica.fieldFrame import FieldFrame


class Prestamo(Servicio):
    def __init__(self, usuario, ejemplar, tituloEscogido, fecha):
        super(Prestamo, self).__init__(usuario, ejemplar, tituloEscogido)
        self._fecha = fecha

    #getters y setters
    def getFecha(self):
        return self._fecha

    def setFecha(self,fecha):
        self._fecha = fecha




    """* Esta función lo que hace es añadir un prestamo al usuario, genera un tiquete y actualiza el 
       estado del libro que prestó
     * @param usuario Usuario al cual se le va a generar el prestamo
     * @param ejemplarPrestado Libro prestado
     * @param biblioteca Biblioteca que contiene los libros que estan disponibles para prestar
     """
    @classmethod
    def generarPrestamoLibro(cls, usuario, ejemplarPrestado, biblioteca):
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

    """* Esta función lo que hace es añadir un prestamo al usuario, genera un tiquete y actualiza el 
       estado de la revista que prestó
     * @param usuario Usuario al cual se le va a generar el prestamo
     * @param ejemplarRevistaPrestada Revista prestada
     * @param biblioteca Biblioteca que contiene las revistas que estan disponibles para prestar
     """
    @classmethod
    def generarPrestamoRevista(cls, usuario, ejemplarPrestado, biblioteca):
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

    """* El usuario elige el prestamo a devolver, se busca el prestamo y posteriormente se cambia el estado 
       de esta a 'FALSE'; de esta manera el servicio que estaba prestado vuelve a estar disponible. También
       se elimina el tiquete correspondiente a ese prestamo (almacenado en la lista 'tiquetes')
     * @param indiceTituloDevolucion Es el prestamo que se desea devolver 
     * @param biblioteca Parametro necesario para el contexto de la funcionalidad
     * @param usuario Usuario al que se le va a afectuar la devolucíon del prestamo 
     """
    @classmethod
    def devolucion(cls, indiceDevolcion: int, biblioteca, usuario):
        prestamoAEliminar = usuario.getPrestamos()[indiceDevolcion]
        tiqueteAEliminar = None

        for tiquete in usuario.getTiquetes():
            if tiquete.getServicio() == prestamoAEliminar:
                tiqueteAEliminar = tiquete

        prestamoAEliminar.getEjemplarEscogido().getEstadoEjemplar().setPrestado(False)
        usuario.eliminarPrestamo(prestamoAEliminar)
        usuario.eliminarTiquete(tiqueteAEliminar)

        biblioteca.añadirEjemplarLibro(prestamoAEliminar.getEjemplarEscogido())

    def __str__(self):
        return self.mostrarTituloEscogido() + "Fecha prestamo: " + self.getFecha()

