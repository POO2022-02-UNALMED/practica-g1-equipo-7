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

    def generarPrestamoRevista(self, usuario, ejemplarPrestado, biblioteca):
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

    def __str__(self):
        return self.mostrarTituloEscogido() + "Fecha prestamo: " + self.getFecha()

    @classmethod
    def generarFramePrestamo(cls, usuario, biblioteca):


        frameTotal = tk.Frame(width = 1080, height=720)
        frameTotal.grid()

        frameIZQ = tk.Frame(frameTotal, width=500, height=700, bg="red")
        frameDER = tk.Frame(frameTotal, width=500, height=700, bg="green")
        frameDER.grid(column=1, row=0, padx=5)
        frameIZQ.grid(column=0, row=0, padx=5)

        fieldFrameDer = FieldFrame(frameDER, "Prestar Libro", ["Numero"], None, None,
                                   [True])
        fieldFrameDer.grid(row=0, column=0)

        def prestarLibro():
            indice = fieldFrameDer.getValue("Numero")
            print(len(Servicio.getEjemplarLibroDisponibles()))
            ejemplar = Servicio.getEjemplarLibroDisponibles()[int(indice) - 1]
            Prestamo.generarPrestamoLibro(usuario, ejemplar, biblioteca)
            print(len(Servicio.getEjemplarLibroDisponibles()))
            print(usuario.getHistorialLibrosUsados())


        botonPrestar = Button(fieldFrameDer, text= "Prestar", font= ("Helvetica", 16), fg = "white", bg = "Blue", command= prestarLibro)
        botonPrestar.grid(column=1, row=1)

        frame_libro_info = Frame(frameIZQ, width=400, height=40, borderwidth=1, padx=5, pady=5)
        frame_libro_info.grid(column=0, row=0, padx=4, pady=5, columnspan=10)

        label_total = Label(frame_libro_info, text="Numeral      Nombre       Autor      Genero")
        label_total.grid(row=0, column=0)

        for r in range(len(Servicio.getEjemplarLibroDisponibles())):
            nombre_libro = Servicio.getEjemplarLibroDisponibles()[r].getLibro().getNombre()
            nombre_autor = Servicio.getEjemplarLibroDisponibles()[r].getLibro().getAutor()
            nombre_genero = Servicio.getEjemplarLibroDisponibles()[r].getLibro().getGenero()

            frame_libro_info = Frame(frameIZQ, width=400, height= 40, borderwidth=1, padx=5, pady=5)
            frame_libro_info.grid(column=0, row=r+1, padx=4, pady=5, columnspan=10)

            label_total = Label(frame_libro_info, text= f"{r+1}. Nombre: {nombre_libro}      Autor: {nombre_autor}      "
                                                        f"Genero: {nombre_genero}")
            label_total.grid(row=0, column=0)

        return frameTotal