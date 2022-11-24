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
    def generarFramePrestamoLibro(cls, usuario, biblioteca):


        frameTotal = tk.Frame(width = 1080, height=720)
        frameTotal.grid()

        frameIZQ = tk.Frame(frameTotal, width=600, height=650, borderwidth=5, padx=5, pady=5)
        frameDER = tk.Frame(frameTotal, width=400, height=650, borderwidth=5, highlightthickness=3, highlightbackground="#61727C")
        frameDER.grid(row=0, column=1, padx=50, pady=250, sticky="n")
        frameIZQ.grid(row=0, column=0, padx=20)
        """def prestarLibro():
            indice = fieldFrameDer.getValue("Numero")
            ejemplar = Servicio.getEjemplarLibroDisponibles()[int(indice) - 1]
            Prestamo.generarPrestamoLibro(usuario, ejemplar, biblioteca)
            print(usuario.getHistorialLibrosUsados())"""

        # Frame de la derecha
        msg = "Escribe el numero del Libro\n que desea prestar"
        entrada = tk.Label(frameDER, text=msg, font=("verdana", 14), padx=10, pady=10)
        entryPrestar = tk.Entry(frameDER, font=("verdana", 12))
        botonPrestar = tk.Button(frameDER, text="Prestar", font=("verdana", 12), background="#61727C", fg="white")

        botonPrestar.grid(row=4, column=0, padx=5, pady=10)
        entryPrestar.grid(row=3, column=0, padx=5, pady=10)
        entrada.grid(row=2, column=0, padx=5, pady=10)

        # Frame de la izquierda
        frame_revista_info = Frame(frameIZQ, width=400, height=40, borderwidth=1, padx=5, pady=5)
        frame_revista_info.grid(column=0, row=0, padx=4, pady=5, columnspan=10)

        frame_lista = tk.Frame(frameIZQ, width=600)
        frame_lista.grid(row=0, column=0, sticky="w")
        label_numeral = tk.Label(frame_lista, text="Numeral", width=7, height=1, justify="left", relief="groove")
        label_nombre = tk.Label(frame_lista, text="Nombre", width=20, height=1, justify="right", relief="groove")
        label_autor = tk.Label(frame_lista, text="Autor", width=20, height=1, justify="left", relief="groove")
        label_genero = tk.Label(frame_lista, text="Genero", width=20, height=1, justify="left", relief="groove")

        label_numeral.grid(row=0, column=0, sticky="w")
        label_nombre.grid(row=0, column=1, sticky="w")
        label_autor.grid(row=0, column=2, sticky="w")
        label_genero.grid(row=0, column=3, sticky="w")

        # label_total = Label(frame_lista, text="Formato: Numeral  -  Nombre  -  Autor  -  Genero")
        # label_total.grid(row=0, column=0, sticky="nw")

        for r in range(len(Servicio.getEjemplarLibroDisponibles())):
            nombre_libro = Servicio.getEjemplarLibroDisponibles()[r].getLibro().getNombre()
            nombre_autor = Servicio.getEjemplarLibroDisponibles()[r].getLibro().getAutor()
            nombre_genero = Servicio.getEjemplarLibroDisponibles()[r].getLibro().getGenero()

            frame_lista = tk.Frame(frameIZQ, width=600)
            frame_lista.grid(row=r + 1, column=0, sticky="w")

            label_numeral = tk.Label(frame_lista, text="{}. ".format(r), width=7, height=1, anchor="w", relief="groove")
            label_nombre = tk.Label(frame_lista, text=nombre_libro, width=20, height=1, anchor="w", relief="groove")
            label_autor = tk.Label(frame_lista, text=nombre_autor, width=20, height=1, anchor="w", relief="groove")
            label_genero = tk.Label(frame_lista, text=nombre_genero, width=20, height=1, anchor="w", relief="groove")

            label_numeral.grid(row=0, column=0, sticky="w")
            label_nombre.grid(row=0, column=1, sticky="w")
            label_autor.grid(row=0, column=2, sticky="w")
            label_genero.grid(row=0, column=3, sticky="w")
            # label_total = Label(frameIZQ,text=f"{r + 1}. Nombre: {nombre_revista} | Autor: {nombre_autor} | "f"Genero: {nombre_genero}")
            # label_total.grid(row=r+1, column=0, padx=5, pady=5, sticky="nw")

        return frameTotal

    @classmethod
    def generarFramePrestamoRevista(cls, usuario, biblioteca):

        frameTotal = tk.Frame(width=1080, height=720)
        frameTotal.grid()

        frameIZQ = tk.Frame(frameTotal, width = 600, height= 700, borderwidth=5, padx=5, pady=5)
        frameDER = tk.Frame(frameTotal, width= 400, height= 650, borderwidth=5, highlightthickness=3, highlightbackground="#61727C")
        frameDER.grid(row = 0, column=1, padx=50, pady=250, sticky = "n")
        frameIZQ.grid(row = 0, column=0, padx=20)

        """def prestarRevista():
            indice = fieldFrameDer.getValue("Numero")
            print(len(Servicio.getEjemplarRevistaDisponibles()))
            ejemplar = Servicio.getEjemplarRevistaDisponibles()[int(indice) - 1]
            Prestamo.generarPrestamoRevista(usuario, ejemplar, biblioteca)
            print(len(Servicio.getEjemplarRevistaDisponibles()))
            print(usuario.getHistorialRevistasUsadas())"""

        #Frame de la derecha
        msg = "Escribe el numero de la Revista\n que desea prestar"
        entrada = tk.Label(frameDER, text=msg, font=("verdana", 14), padx = 10, pady = 10)
        entryPrestar = tk.Entry(frameDER, font=("verdana", 12))
        botonPrestar = tk.Button(frameDER, text="Prestar", font = ("verdana", 12),background="#61727C", fg= "white")
        
        botonPrestar.grid(row=4, column=0, padx=5, pady=10) 
        entryPrestar.grid(row = 3, column = 0, padx=5, pady=10)
        entrada.grid(row = 2, column = 0, padx=5, pady=10)


        #Frame de la izquierda
        frame_revista_info = Frame(frameIZQ, width=400, height=40, borderwidth=1, padx=5, pady=5)
        frame_revista_info.grid(column=0, row=0, padx=4, pady=5, columnspan=10)

        frame_lista = tk.Frame(frameIZQ, width=600)
        frame_lista.grid(row= 0, column=0, sticky="w")
        label_numeral = tk.Label(frame_lista, text="Numeral", width=7, height=1, justify="left", relief="groove")
        label_nombre = tk.Label(frame_lista, text="Nombre", width=20, height=1, justify="right", relief="groove")
        label_autor = tk.Label(frame_lista, text="Autor", width=20, height=1, justify="left", relief="groove")
        label_genero = tk.Label(frame_lista, text="Categoria", width=20, height=1, justify="left", relief="groove")

        label_numeral.grid(row=0, column=0, sticky="w")
        label_nombre.grid(row=0, column=1, sticky="w")
        label_autor.grid(row=0, column=2, sticky="w")
        label_genero.grid(row=0, column=3, sticky="w")

        #label_total = Label(frame_lista, text="Formato: Numeral  -  Nombre  -  Autor  -  Genero")
        #label_total.grid(row=0, column=0, sticky="nw")

        for r in range(1, len(Servicio.getEjemplarRevistaDisponibles())+1):
            nombre_revista = Servicio.getEjemplarRevistaDisponibles()[r-1].getRevista().getNombre()
            nombre_autor = Servicio.getEjemplarRevistaDisponibles()[r-1].getRevista().getAutor()
            nombre_genero = Servicio.getEjemplarRevistaDisponibles()[r-1].getRevista().getCategoria()

            frame_lista = tk.Frame(frameIZQ, width=600)
            frame_lista.grid(row=r + 1, column=0, sticky="w")

            label_numeral = tk.Label(frame_lista,text = "{}. ".format(r), width=7, height = 1, anchor="w",relief="groove")
            label_nombre = tk.Label(frame_lista, text = nombre_revista, width=20, height = 1, anchor="w",relief="groove")
            label_autor = tk.Label(frame_lista, text = nombre_autor, width=20, height = 1, anchor="w",relief="groove")
            label_genero = tk.Label(frame_lista, text = nombre_genero, width=20, height = 1, anchor="w",relief="groove")

            label_numeral.grid(row = 0, column = 0, sticky = "w")
            label_nombre.grid(row=0, column=1, sticky = "w")
            label_autor.grid(row=0, column=2, sticky = "w")
            label_genero.grid(row=0, column=3, sticky = "w")
            #label_total = Label(frameIZQ,text=f"{r + 1}. Nombre: {nombre_revista} | Autor: {nombre_autor} | "f"Genero: {nombre_genero}")
            #label_total.grid(row=r+1, column=0, padx=5, pady=5, sticky="nw")

        return frameTotal