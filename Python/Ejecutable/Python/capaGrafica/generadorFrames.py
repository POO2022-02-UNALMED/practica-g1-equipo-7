import tkinter as tk
from datetime import datetime, timedelta

from Python.capaGrafica.fieldFrame import FieldFrame
from Python.gestorAplicacion.libreria.ejemplarLibro import EjemplarLibro
from Python.gestorAplicacion.libreria.ejemplarRevista import EjemplarRevista
from Python.gestorAplicacion.libreria.libro import Libro
from Python.gestorAplicacion.libreria.revista import Revista
from Python.gestorAplicacion.servicios.prestamo import Prestamo
from Python.gestorAplicacion.servicios.reserva import Reserva
from Python.gestorAplicacion.servicios.servicio import Servicio


from Python.excepciones.errorapp import ErrorApp

from Python.excepciones.excepcionentero import ExcepcionEntero
from Python.excepciones.excepcionstring import ExcepcionString
from Python.excepciones.excepcionelementoinexistente import ExcepcionElementoInexistente
from Python.excepciones.advertencia import Advertencia


class GeneradorFrames():
    @classmethod
    def generarFramePrestamoLibro(cls, usuario, biblioteca):
        print(len(Servicio.getEjemplarLibroDisponibles()))

        frameTotal = tk.Frame(width=1080, height=720)
        frameTotal.grid()

        frameIZQ = tk.Frame(frameTotal, width=600, height=700, borderwidth=5, padx=5, pady=5)
        frameDER = tk.Frame(frameTotal, width=400, height=650, borderwidth=5, highlightthickness=3,
                            highlightbackground="#61727C")
        frameDER.grid(row=0, column=1, padx=50, pady=250, sticky="n")
        frameIZQ.grid(row=0, column=0, padx=20)
        frameIZQ.grid_propagate(False)

        # Frame de la derecha
        msg = "Escribe el numero del Libro\n que desea prestar"
        fieldFramePrestamo = FieldFrame(frameDER, criterios=[msg])
        #entrada = tk.Label(frameDER, text=msg, font=("verdana", 14), padx=10, pady=10)
        #entryPrestar = tk.Entry(frameDER, font=("verdana", 12))

        def prestarLibro():
            try:
                #indice = entryPrestar.get()
                indice = fieldFramePrestamo.getValue(0)
                if indice == "":
                    raise ExcepcionEntero()
                elif not (48 <= ord(indice[0]) <= 57):
                    raise ExcepcionEntero()
                indice = int(indice) - 1

                if indice > len(Servicio.getEjemplarLibroDisponibles()) - 1 or indice < 0:
                    raise ExcepcionElementoInexistente()
                else:
                    Ejemplar = Servicio.getEjemplarLibroDisponibles()[indice]
                    Prestamo.generarPrestamoLibro(usuario, Ejemplar, biblioteca)
                    #entryPrestar.delete(0, tk.END)
                    fieldFramePrestamo.delValue(0)
                    print("PRÉSTAMO EXITOSO")

                frameIZQ.grid_forget()
                generarListaLibrosDisponibles()
            except ErrorApp as e:
                Advertencia(str(e))


        botonPrestar = tk.Button(frameDER, text="Prestar", font=("verdana", 12), background="#61727C", fg="white",
                                 command=prestarLibro)
        fieldFramePrestamo.grid(row = 2, column = 0)
        botonPrestar.grid(row=4, column=0, padx=5, pady=10)
        #entryPrestar.grid(row=3, column=0, padx=5, pady=10)
        #entrada.grid(row=2, column=0, padx=5, pady=10)

        def generarListaLibrosDisponibles():
            #Esto se hace para actualizar la disponibilidad
            Servicio.filtrarLibrosDisponibles(biblioteca)

            frameIZQ = tk.Frame(frameTotal, width=600, height=700, borderwidth=5, padx=5, pady=5)
            frameIZQ.grid(row=0, column=0, padx=20)
            frameIZQ.grid_propagate(False)

            # 5 dias, 3 semanas, 2 meses

            # Frame de la izquierda
            # frame_revista_info = Frame(frameIZQ, width=400, height=40, borderwidth=1, padx=5, pady=5)
            # frame_revista_info.grid(column=0, row=0, padx=4, pady=5, columnspan=10)

            frame_lista = tk.Frame(frameIZQ, width=600, height=20)
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

            for r in range(1, len(Servicio.getEjemplarLibroDisponibles()) + 1):
                nombre_libro = Servicio.getEjemplarLibroDisponibles()[r - 1].getLibro().getNombre()
                nombre_autor = Servicio.getEjemplarLibroDisponibles()[r - 1].getLibro().getAutor()
                nombre_genero = Servicio.getEjemplarLibroDisponibles()[r - 1].getLibro().getGenero()

                frame_lista = tk.Frame(frameIZQ, width=600)
                frame_lista.grid(row=r + 1, column=0, sticky="w")

                label_numeral = tk.Label(frame_lista, text="{}. ".format(r), width=7, height=1, anchor="w",
                                         relief="groove")
                label_nombre = tk.Label(frame_lista, text=nombre_libro, width=20, height=1, anchor="w", relief="groove")
                label_autor = tk.Label(frame_lista, text=nombre_autor, width=20, height=1, anchor="w", relief="groove")
                label_genero = tk.Label(frame_lista, text=nombre_genero, width=20, height=1, anchor="w",
                                        relief="groove")

                label_numeral.grid(row=0, column=0, sticky="w")
                label_nombre.grid(row=0, column=1, sticky="w")
                label_autor.grid(row=0, column=2, sticky="w")
                label_genero.grid(row=0, column=3, sticky="w")
                # label_total = Label(frameIZQ,text=f"{r + 1}. Nombre: {nombre_revista} | Autor: {nombre_autor} | "f"Genero: {nombre_genero}")
                # label_total.grid(row=r+1, column=0, padx=5, pady=5, sticky="nw")

        generarListaLibrosDisponibles()
        return frameTotal

    @classmethod
    def generarFramePrestamoRevista(cls, usuario, biblioteca):

        frameTotal = tk.Frame(width=1080, height=720)
        frameTotal.grid()

        frameIZQ = tk.Frame(frameTotal, width=600, height=700, borderwidth=5, padx=5, pady=5)
        frameDER = tk.Frame(frameTotal, width=400, height=650, borderwidth=5, highlightthickness=3,
                            highlightbackground="#61727C")
        frameDER.grid(row=0, column=1, padx=50, pady=250, sticky="n")
        frameIZQ.grid(row=0, column=0, padx=20)

        # Frame de la derecha
        msg = "Escribe el numero de la Revista\n que desea prestar"
        #entrada = tk.Label(frameDER, text=msg, font=("verdana", 14), padx=10, pady=10)
        #entryPrestar = tk.Entry(frameDER, font=("verdana", 12))
        fieldFramePrestamo = FieldFrame(frameDER, criterios=[msg])

        def prestarRevista():
            try:
                #indice = entryPrestar.get()
                indice = fieldFramePrestamo.getValue(0)
                if indice == "":
                    raise ExcepcionEntero()
                elif not (48 <= ord(indice[0]) <= 57):
                    raise ExcepcionEntero()
                indice = int(indice) - 1
                if indice >= len(Servicio.getEjemplarRevistaDisponibles()) or indice < 0:
                    raise ExcepcionElementoInexistente()
                else:
                    Ejemplar = Servicio.getEjemplarRevistaDisponibles()[indice]
                    #entryPrestar.delete(0, tk.END)
                    fieldFramePrestamo.delValue(0)
                    Prestamo.generarPrestamoRevista(usuario, Ejemplar, biblioteca)
                    print(f"PRÉSTAMO EXITOSO {Ejemplar.getRevista().getNombre()}")

                frameIZQ.grid_forget()
                generarListaRevistasDisponibles()
            except ErrorApp as e:
                Advertencia(str(e))

        botonPrestar = tk.Button(frameDER, text="Prestar", font=("verdana", 12), background="#61727C", fg="white",
                                 command=prestarRevista)

        fieldFramePrestamo.grid(row = 2, column = 0)
        botonPrestar.grid(row=4, column=0, padx=5, pady=10)
        #entryPrestar.grid(row=3, column=0, padx=5, pady=10)
        #entrada.grid(row=2, column=0, padx=5, pady=10)

        # Frame de la izquierda
        def generarListaRevistasDisponibles():
            #Se hace para actualizar la disponibilidad
            Servicio.filtrarRevistasDisponibles(biblioteca)
            frameIZQ = tk.Frame(frameTotal, width=600, height=700, borderwidth=5, padx=5, pady=5)
            frameIZQ.grid(row=0, column=0, padx=20)
            frameIZQ.grid_propagate(False)
            frame_revista_info = tk.Frame(frameIZQ, width=400, height=40, borderwidth=1, padx=5, pady=5)
            frame_revista_info.grid(column=0, row=0, padx=4, pady=5, columnspan=10)

            frame_lista = tk.Frame(frameIZQ, width=600)
            frame_lista.grid(row=0, column=0, sticky="w")
            label_numeral = tk.Label(frame_lista, text="Numeral", width=7, height=1, justify="left", relief="groove")
            label_nombre = tk.Label(frame_lista, text="Nombre", width=20, height=1, justify="right", relief="groove")
            label_autor = tk.Label(frame_lista, text="Autor", width=20, height=1, justify="left", relief="groove")
            label_genero = tk.Label(frame_lista, text="Categoria", width=20, height=1, justify="left", relief="groove")

            label_numeral.grid(row=0, column=0, sticky="w")
            label_nombre.grid(row=0, column=1, sticky="w")
            label_autor.grid(row=0, column=2, sticky="w")
            label_genero.grid(row=0, column=3, sticky="w")

            # label_total = Label(frame_lista, text="Formato: Numeral  -  Nombre  -  Autor  -  Genero")
            # label_total.grid(row=0, column=0, sticky="nw")

            for r in range(1, len(Servicio.getEjemplarRevistaDisponibles()) + 1):
                nombre_revista = Servicio.getEjemplarRevistaDisponibles()[r - 1].getRevista().getNombre()
                nombre_autor = Servicio.getEjemplarRevistaDisponibles()[r - 1].getRevista().getAutor()
                nombre_genero = Servicio.getEjemplarRevistaDisponibles()[r - 1].getRevista().getCategoria()

                frame_lista = tk.Frame(frameIZQ, width=600)
                frame_lista.grid(row=r + 1, column=0, sticky="w")

                label_numeral = tk.Label(frame_lista, text="{}. ".format(r), width=7, height=1, anchor="w",
                                         relief="groove")
                label_nombre = tk.Label(frame_lista, text=nombre_revista, width=20, height=1, anchor="w",
                                        relief="groove")
                label_autor = tk.Label(frame_lista, text=nombre_autor, width=20, height=1, anchor="w", relief="groove")
                label_genero = tk.Label(frame_lista, text=nombre_genero, width=20, height=1, anchor="w",
                                        relief="groove")

                label_numeral.grid(row=0, column=0, sticky="w")
                label_nombre.grid(row=0, column=1, sticky="w")
                label_autor.grid(row=0, column=2, sticky="w")
                label_genero.grid(row=0, column=3, sticky="w")
                # label_total = Label(frameIZQ,text=f"{r + 1}. Nombre: {nombre_revista} | Autor: {nombre_autor} | "f"Genero: {nombre_genero}")
                # label_total.grid(row=r+1, column=0, padx=5, pady=5, sticky="nw")

        generarListaRevistasDisponibles()
        return frameTotal

    @classmethod
    def generarFrameReservarLibro(cls, usuario, biblioteca):
        print(len(Servicio.getEjemplarLibroDisponibles()))
        frameReservarLibro = tk.Frame(width=1080, height=720)
        frame_listas_reserva_libro = tk.Frame(frameReservarLibro, width=600, height=650, borderwidth=5, padx=5, pady=5)
        frame_listas_reserva_libro.grid(row=0, column=0, padx=20, pady=20, sticky="n")
        frame_filtro_reserva_libro = tk.Frame(frameReservarLibro, width=400, height=650, borderwidth=5,
                                              highlightthickness=3, highlightbackground="#61727C")
        frame_filtro_reserva_libro.grid(row=0, column=1, padx=20, pady=20)

        def despliegue_reserva_libro(filtro):
            cantidad_tiempo = int(filtro.split(" ")[0])
            print(len(Servicio.getEjemplarLibroDisponibles()))
            msg = "Escribe el numero del libro\n que desea reservar"
            #entrada = tk.Label(frame_filtro_reserva_libro, text=msg, font=("verdana", 14), padx=10, pady=10)
            #entryBusqueda = tk.Entry(frame_filtro_reserva_libro, font=("verdana", 12))
            fieldFrameReserva = FieldFrame(frame_filtro_reserva_libro, criterios=[msg])
            fieldFrameReserva.grid(row = 2, column = 0, padx=5)
            #entryBusqueda.grid(row=3, column=0, padx=5, pady=10)
            #entrada.grid(row=2, column=0, padx=5, pady=10)

            def HacerReservaLibro():
                try:
                    #indice = entryBusqueda.get()
                    indice = fieldFrameReserva.getValue(0)
                    if indice == "":
                        raise ExcepcionEntero()
                    elif not (48 <= ord(indice[0]) <= 57):
                        raise ExcepcionEntero()
                    indice = int(indice) - 1

                    if indice >= len(Servicio.getEjemplarLibroDisponibles()) or indice < 0:
                        raise ExcepcionElementoInexistente()
                    else:
                        print(indice)
                        Ejemplar = Servicio.getEjemplarLibroDisponibles()[indice]
                        #entryBusqueda.delete(0, tk.END)
                        fieldFrameReserva.delValue(0)
                        fecha_inicial = datetime.now()
                        fecha_final = datetime.now()
                        if cantidad_tiempo == 5:
                            fecha_final += timedelta(days=5)

                        elif cantidad_tiempo == 3:
                            fecha_final += timedelta(weeks=3)

                        elif cantidad_tiempo == 2:
                            fecha_final += timedelta(weeks=8)

                        Reserva.generarReservaLibro(usuario, Ejemplar, biblioteca, fecha_inicial, fecha_final)
                        frame_listas_reserva_libro.grid_forget()
                        generarListaLibroDisponibles()
                        print(f"RESERVA EXITOSO {Ejemplar.getLibro().getNombre()} para el {fecha_inicial, fecha_final}")
                except ErrorApp as e:
                    Advertencia(str(e))

            botonBusqueda = tk.Button(frame_filtro_reserva_libro, text="Reservar", font=("verdana", 12),
                                      background="#61727C", fg="white", command=HacerReservaLibro)
            botonBusqueda.grid(row=4, column=0, padx=5, pady=10)

        def generarListaLibroDisponibles():
            #Se hace para actualizar la disponibilidad
            Servicio.filtrarLibrosDisponibles(biblioteca)
            frame_listas_reserva_libro = tk.Frame(frameReservarLibro, width=600, height=700, borderwidth=5, padx=5,
                                                  pady=5)
            frame_listas_reserva_libro.grid(row=0, column=0, padx=20)

            frame_lista = tk.Frame(frame_listas_reserva_libro, width=600)
            frame_lista.grid(row=0, column=0, sticky="w", pady=5)
            label_numeral = tk.Label(frame_lista, text="Numeral", width=7, height=1, justify="left",
                                     relief="groove")
            label_nombre = tk.Label(frame_lista, text="Nombre", width=20, height=1, justify="right",
                                    relief="groove")
            label_autor = tk.Label(frame_lista, text="Autor", width=20, height=1, justify="left", relief="groove")
            label_genero = tk.Label(frame_lista, text="Genero", width=20, height=1, justify="left",
                                    relief="groove")

            label_numeral.grid(row=0, column=0, sticky="w")
            label_nombre.grid(row=0, column=1, sticky="w")
            label_autor.grid(row=0, column=2, sticky="w")
            label_genero.grid(row=0, column=3, sticky="w")
            frame_listas_reserva_libro.grid_propagate(False)
            for r in range(1, len(Servicio.getEjemplarLibroDisponibles()) + 1):
                nombre_libro = Servicio.getEjemplarLibroDisponibles()[r - 1].getLibro().getNombre()
                nombre_autor = Servicio.getEjemplarLibroDisponibles()[r - 1].getLibro().getAutor()
                nombre_genero = Servicio.getEjemplarLibroDisponibles()[r - 1].getLibro().getGenero()

                frame_listaa = tk.Frame(frame_listas_reserva_libro, width=600)
                frame_listaa.grid(row=r + 1, column=0, sticky="w")

                label_numeraal = tk.Label(frame_listaa, text="{}. ".format(r), width=7, height=1, anchor="w",
                                          relief="groove")
                label_nombree = tk.Label(frame_listaa, text=nombre_libro, width=20, height=1, anchor="w",
                                         relief="groove")
                label_autoor = tk.Label(frame_listaa, text=nombre_autor, width=20, height=1, anchor="w",
                                        relief="groove")
                label_generoo = tk.Label(frame_listaa, text=nombre_genero, width=20, height=1, anchor="w",
                                         relief="groove")

                label_numeraal.grid(row=0, column=0, sticky="w")
                label_nombree.grid(row=0, column=1, sticky="w")
                label_autoor.grid(row=0, column=2, sticky="w")
                label_generoo.grid(row=0, column=3, sticky="w")

        clicked_reservar_libro = tk.StringVar()
        labelFiltro_reserva_libro = tk.Label(frame_filtro_reserva_libro, text="Elija el tiempo de reserva",
                                             font=("verdana", 14), justify="center")
        drop_reserva_libro = tk.OptionMenu(frame_filtro_reserva_libro, clicked_reservar_libro,
                                           *["5 dias", "3 semanas", "2 meses"], command=despliegue_reserva_libro)
        drop_reserva_libro.grid(row=1, column=0, padx=10, pady=10)
        labelFiltro_reserva_libro.grid(row=0, column=0, padx=10, pady=10)

        generarListaLibroDisponibles()
        return frameReservarLibro

    @classmethod
    def generarFrameReservaRevista(cls, usuario, biblioteca):
        frameReservarRevista = tk.Frame(width=1080, height=720)
        frame_listas_reserva_revista = tk.Frame(frameReservarRevista, width=600, height=650, borderwidth=5, padx=5,
                                                pady=5)
        frame_listas_reserva_revista.grid(row=0, column=0, padx=20, pady=20)


        def despliegue_reserva_revista(filtro):
            cantidad_tiempo = int(filtro.split(" ")[0])

            msg = "Escribe el numero de la revista\n que desea reservar"
            #entrada = tk.Label(frame_filtro_reserva_revista, text=msg, font=("verdana", 14), padx=10, pady=10)
            #entryBusqueda = tk.Entry(frame_filtro_reserva_revista, font=("verdana", 12))
            fieldFrameReserva = FieldFrame(frame_filtro_reserva_revista, criterios=[msg])

            def HacerReservaRevista():
                try:
                    #indice = entryBusqueda.get()
                    indice = fieldFrameReserva.getValue(0)
                    if indice == "":
                        raise ExcepcionEntero()
                    elif not (48 <= ord(indice[0]) <= 57):
                        raise ExcepcionEntero()
                    indice = int(indice) - 1
                    if indice >= len(Servicio.getEjemplarRevistaDisponibles()) or indice < 0:
                        raise ExcepcionElementoInexistente()
                    else:

                        Ejemplar = Servicio.getEjemplarRevistaDisponibles()[indice]
                        #entryBusqueda.delete(0, tk.END)
                        fieldFrameReserva.delValue(0)
                        fecha_inicial = datetime.now()
                        fecha_final = datetime.now()
                        if cantidad_tiempo == 5:
                            fecha_final += timedelta(days=5)

                        elif cantidad_tiempo == 3:
                            fecha_final += timedelta(weeks=3)

                        elif cantidad_tiempo == 2:
                            fecha_final += timedelta(weeks=8)

                        Reserva.generarReservaRevista(usuario, Ejemplar, biblioteca, fecha_inicial, fecha_final)
                        frame_listas_reserva_revista.grid_forget()
                        generarListaRevistasDisponibles()
                        print(f"RESERVA EXITOSO {Ejemplar.getRevista().getNombre()} para el {fecha_inicial, fecha_final}")
                except ErrorApp as e:
                    Advertencia(str(e))


            botonBusqueda = tk.Button(frame_filtro_reserva_revista, text="Reservar", font=("verdana", 12),
                                      background="#61727C",
                                      fg="white", command=HacerReservaRevista)
            fieldFrameReserva.grid(row=2, column=0)
            botonBusqueda.grid(row=4, column=0, padx=5, pady=10)
            #entryBusqueda.grid(row=3, column=0, padx=5, pady=10)
            #entrada.grid(row=2, column=0, padx=5, pady=10)

        clicked_reservar_revista = tk.StringVar()
        def generarListaRevistasDisponibles():
            #Se hace para actualizar la disponibilidad
            Servicio.filtrarRevistasDisponibles(biblioteca)
            frame_listas_reserva_revista = tk.Frame(frameReservarRevista, width=600, height=650, borderwidth=5, padx=5,
                                                    pady=5)
            frame_listas_reserva_revista.grid(row=0, column=0, padx=20, pady=20)

            frame_lista = tk.Frame(frame_listas_reserva_revista, width=600)
            frame_lista.grid(row=0, column=0, sticky="w", pady=5)
            label_numeral = tk.Label(frame_lista, text="Numeral", width=7, height=1, justify="left",
                                     relief="groove")
            label_nombre = tk.Label(frame_lista, text="Nombre", width=20, height=1, justify="right",
                                    relief="groove")
            label_autor = tk.Label(frame_lista, text="Autor", width=20, height=1, justify="left", relief="groove")
            label_genero = tk.Label(frame_lista, text="Categoria", width=20, height=1, justify="left",
                                    relief="groove")

            label_numeral.grid(row=0, column=0, sticky="w")
            label_nombre.grid(row=0, column=1, sticky="w")
            label_autor.grid(row=0, column=2, sticky="w")
            label_genero.grid(row=0, column=3, sticky="w")
            frame_listas_reserva_revista.grid_propagate(False)

            for r in range(1, len(Servicio.getEjemplarRevistaDisponibles()) + 1):
                nombre_revista = Servicio.getEjemplarRevistaDisponibles()[r - 1].getRevista().getNombre()
                nombre_autor = Servicio.getEjemplarRevistaDisponibles()[r - 1].getRevista().getAutor()
                nombre_categoria = Servicio.getEjemplarRevistaDisponibles()[r - 1].getRevista().getCategoria()

                frame_listaR = tk.Frame(frame_listas_reserva_revista, width=600)
                frame_listaR.grid(row=r + 1, column=0, sticky="w")

                label_numeraalR = tk.Label(frame_listaR, text="{}. ".format(r), width=7, height=1, anchor="w",
                                           relief="groove")
                label_nombreeR = tk.Label(frame_listaR, text=nombre_revista, width=20, height=1, anchor="w",
                                          relief="groove")
                label_autoorR = tk.Label(frame_listaR, text=nombre_autor, width=20, height=1, anchor="w", relief="groove")
                label_generooR = tk.Label(frame_listaR, text=nombre_categoria, width=20, height=1, anchor="w",
                                          relief="groove")

                label_numeraalR.grid(row=0, column=0, sticky="w")
                label_nombreeR.grid(row=0, column=1, sticky="w")
                label_autoorR.grid(row=0, column=2, sticky="w")
                label_generooR.grid(row=0, column=3, sticky="w")

        frame_filtro_reserva_revista = tk.Frame(frameReservarRevista, width=400, height=650, borderwidth=5,
                                                highlightthickness=3, highlightbackground="#61727C")
        frame_filtro_reserva_revista.grid(row=0, column=1, padx=20, pady=20)

        labelFiltro_reserva_revista = tk.Label(frame_filtro_reserva_revista, text="Elija el tiempo de reserva",
                                               font=("verdana", 14), justify="center")
        drop_reserva_revista = tk.OptionMenu(frame_filtro_reserva_revista, clicked_reservar_revista,
                                             *["5 dias", "3 semanas", "2 meses"], command=despliegue_reserva_revista)
        drop_reserva_revista.grid(row=1, column=0, padx=10, pady=10)
        labelFiltro_reserva_revista.grid(row=0, column=0, padx=10, pady=10)
        generarListaRevistasDisponibles()
        return frameReservarRevista

    @classmethod
    def generarFrameMisReservas(cls, usuario):
        frameMisReservas = tk.Frame(width=1080, height=720)
        frame_letrero_reservas = tk.Frame(frameMisReservas, width=1060, height=100, borderwidth=5, highlightthickness=3,
                                          highlightbackground="#61727C")
        frame_letrero_reservas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        frame_libros_reservas = tk.Frame(frameMisReservas, width=520, height=570, borderwidth=5,
                                         highlightbackground="#61727C",
                                         highlightthickness=3)
        frame_libros_reservas.grid(row=1, column=0, padx=10, pady=10)

        # LOGICA PARA LLENAR LA LISTA DE PRÉSTAMOS
        def ActualizarReservas():
            lista_reservas = usuario.getReservas()
            contLibros = 1
            contRevistas = 1
            for reserva in lista_reservas:
                ejemplar = reserva.getEjemplarEscogido()
                if isinstance(ejemplar, EjemplarLibro):
                    ejemplar = ejemplar.getLibro()
                    print("hola")
                    nombre_libro = ejemplar.getNombre()
                    nombre_autor = ejemplar.getAutor()
                    nombre_genero = ejemplar.getGenero()
                    fecha = "{}/{}/{}".format(reserva.getFechaDevolucion().day, reserva.getFechaDevolucion().month, reserva.getFechaDevolucion().year)
                    # IMPLEMENTAR LO DE LISTAS ACÁ
                    frame_ejemplar = tk.Frame(frame_libros_reservas, width=600)
                    label_numeral = tk.Label(frame_ejemplar, text="{}. ".format(contLibros), width=7, height=1,
                                             anchor="w",
                                             relief="groove")
                    label_nombre = tk.Label(frame_ejemplar, text=nombre_libro, width=20, height=1, anchor="w",
                                            relief="groove")
                    label_autor = tk.Label(frame_ejemplar, text=nombre_autor, width=20, height=1, anchor="w",
                                           relief="groove")
                    label_genero = tk.Label(frame_ejemplar, text=nombre_genero, width=10, height=1, anchor="w",
                                            relief="groove")
                    label_fecha = tk.Label(frame_ejemplar, text=fecha, width=10, height=1, anchor="w",
                                            relief="groove")
                    label_numeral.grid(row=0, column=0, sticky="w")
                    label_nombre.grid(row=0, column=1, sticky="w")
                    label_autor.grid(row=0, column=2, sticky="w")
                    label_genero.grid(row=0, column=3, sticky="w")
                    label_fecha.grid(row=0, column=4, sticky="w")
                    frame_ejemplar.grid(row=contLibros, column=0)
                    contLibros += 1


                elif isinstance(ejemplar, EjemplarRevista):
                    ejemplar = ejemplar.getRevista()
                    print("hola")
                    nombre_revista = ejemplar.getNombre()
                    nombre_autor = ejemplar.getAutor()
                    nombre_categoria = ejemplar.getCategoria()
                    fecha = "{}/{}/{}".format(reserva.getFechaDevolucion().day, reserva.getFechaDevolucion().month,
                                              reserva.getFechaDevolucion().year)
                    # IMPLEMENTAR LO DE LISTAS ACÁ
                    frame_ejemplar = tk.Frame(frame_revistas_reservas, width=600)

                    label_numeral = tk.Label(frame_ejemplar, text="{}. ".format(contRevistas), width=7, height=1,
                                             anchor="w",
                                             relief="groove")
                    label_nombre = tk.Label(frame_ejemplar, text=nombre_revista, width=20, height=1, anchor="w",
                                            relief="groove")
                    label_autor = tk.Label(frame_ejemplar, text=nombre_autor, width=15, height=1, anchor="w",
                                           relief="groove")
                    label_genero = tk.Label(frame_ejemplar, text=nombre_categoria, width=15, height=1, anchor="w",
                                            relief="groove")
                    label_fecha = tk.Label(frame_ejemplar, text=fecha, width=10, height=1, anchor="w",
                                           relief="groove")
                    label_numeral.grid(row=0, column=0, sticky="w")
                    label_nombre.grid(row=0, column=1, sticky="w")
                    label_autor.grid(row=0, column=2, sticky="w")
                    label_genero.grid(row=0, column=3, sticky="w")
                    label_fecha.grid(row=0, column=4, sticky="w")
                    frame_ejemplar.grid(row=contRevistas, column=0, sticky="w")
                    contRevistas += 1
            if contLibros == 1 and contRevistas == 1:
                print("LO SENTIMOS NO HAY NADA PARA MOSTRAR")
        frame_revistas_reservas = tk.Frame(frameMisReservas, width=520, height=570, borderwidth=5, highlightthickness=3,
                                           highlightbackground="#61727C")
        frame_revistas_reservas.grid(row=1, column=1, padx=10, pady=10)
        boton_actualizar_reservas = tk.Button(frame_letrero_reservas, width=20, height=2, text="Actualizar",
                                           command=ActualizarReservas,
                                           font=("verdana", 12), background="#61727C", fg="white")
        boton_actualizar_reservas.grid(row=0, column=0, sticky="w", padx=10)

        letrero_reservas = tk.Label(frame_letrero_reservas, text="Mis Reservas", font=("verdana", 16, "bold"),
                                    fg="white", borderwidth=3,
                                    background="#61727C", width=20, height=2)
        letrero_reservas.grid(row=0, column=1, padx=10)

        letrero_libros_reservas = tk.Label(frame_libros_reservas, text="Libros", font=("verdana", 14, "bold"),
                                           fg="white", borderwidth=3,
                                           background="#61727C", width=10, height=2)
        letrero_libros_reservas.grid(row=0, column=0, pady=10, sticky="w")
        frame_libros_reservas.grid_propagate(False)
        letrero_revista_reservas = tk.Label(frame_revistas_reservas, text="Revistas", font=("verdana", 14, "bold"),
                                            fg="white",
                                            borderwidth=3, background="#61727C", width=10, height=2)
        letrero_revista_reservas.grid(row=0, column=0, padx=5, pady=10, sticky="w")
        frame_revistas_reservas.grid_propagate(False)

        return frameMisReservas

    @classmethod
    def generarFrameBuscarLibro(cls, biblioteca):
        frameBuscarLibro =  tk.Frame(width=1080, height=720)

        def despliegue(filtro):
            #entrada = tk.Label(frame_filtro, text="Escribe el {} del libro".format(filtro), font=("verdana", 14), padx = 10, pady = 10)
            #entryBusqueda = tk.Entry(frame_filtro, font=("verdana", 12))
            fieldFrameBusqueda = FieldFrame(frame_filtro, criterios=["Escribe el {} del libro".format(filtro)])
            fieldFrameBusqueda.grid(row = 2, column = 0)

            def Filtrar():
                try:
                    #string_Campo = entryBusqueda.get().lower()
                    string_Campo = fieldFrameBusqueda.getValue(0)
                    if string_Campo == "":
                        raise ExcepcionString()
                    elif 48 <= ord(string_Campo[0]) <= 57:
                        raise ExcepcionString()

                    resultados = []
                    # Reiniciar el frame de resultados
                    #frameAnterior.destroy()
                    frame_listas = tk.Frame(frameBuscarLibro, width=600, height=650, borderwidth=5, padx=5, pady=5)
                    frame_listas.grid(row=0, column=0, padx=20, pady=20)
                    frame_lista = tk.Frame(frame_listas, width=600)
                    frame_lista.grid(row=0, column=0, sticky="w")
                    label_numeral = tk.Label(frame_lista, text="Numeral", width=7, height=1, justify="left",
                                             relief="groove")
                    label_nombre = tk.Label(frame_lista, text="Nombre", width=20, height=1, justify="right",
                                            relief="groove")
                    label_autor = tk.Label(frame_lista, text="Autor", width=20, height=1, justify="left", relief="groove")
                    label_genero = tk.Label(frame_lista, text="Genero", width=20, height=1, justify="left",
                                            relief="groove")

                    label_numeral.grid(row=0, column=0, sticky="w")
                    label_nombre.grid(row=0, column=1, sticky="w")
                    label_autor.grid(row=0, column=2, sticky="w")
                    label_genero.grid(row=0, column=3, sticky="w")
                    frame_listas.grid_propagate(False)
                    #entryBusqueda.delete(0, tk.END)
                    fieldFrameBusqueda.delValue(0)
                    filtro = clicked.get().lower()
                    cantidad = 0
                    if filtro == "autor":
                        for libro in biblioteca.getLibros():
                            if string_Campo in libro.getAutor().lower():
                                cantidad += 1
                                resultados.append(libro)

                    elif filtro == "nombre":
                        for libro in biblioteca.getLibros():
                            if string_Campo in libro.getNombre().lower():
                                cantidad += 1
                                resultados.append(libro)

                    elif filtro == "genero":
                        for libro in biblioteca.getLibros():
                            if string_Campo in libro.getGenero().lower():
                                cantidad += 1
                                resultados.append(libro)

                    if cantidad == 0:
                        print(
                            "EXCEPTION: NO SE ENCONTRARON RESULTADOS (esto iría en una ventana pequeña que se pueda cerrar y ya")
                    else:
                        #se muestran los resultados del libro
                        for i in range(len(resultados)):
                            libro = resultados[i]
                            nombre_libro = libro.getNombre()
                            nombre_autor = libro.getAutor()
                            nombre_genero = libro.getGenero()
                            # IMPLEMENTAR LO DE LISTAS ACÁ

                            frame_libros = tk.Frame(frame_listas, width=600)
                            label_numeral = tk.Label(frame_libros, text="{}. ".format(i+1), width=7, height=1, anchor="w",
                                                     relief="groove")
                            label_nombre = tk.Label(frame_libros, text=nombre_libro, width=20, height=1, anchor="w",
                                                    relief="groove")
                            label_autor = tk.Label(frame_libros, text=nombre_autor, width=20, height=1, anchor="w",
                                                   relief="groove")
                            label_genero = tk.Label(frame_libros, text=nombre_genero, width=20, height=1, anchor="w",
                                                    relief="groove")

                            label_numeral.grid(row=0, column=0, sticky="w")
                            label_nombre.grid(row=0, column=1, sticky="w")
                            label_autor.grid(row=0, column=2, sticky="w")
                            label_genero.grid(row=0, column=3, sticky="w")
                            frame_libros.grid(row=i+1, column=0)
                except ErrorApp as e:
                    Advertencia(str(e))

            botonBusqueda = tk.Button(frame_filtro, text="Buscar", font=("verdana", 12), background="#61727C",
                                      fg="white", command=Filtrar)
            botonBusqueda.grid(row=4, column=0, padx=10, pady=10)
            #entryBusqueda.grid(row=3, column=0, padx=10, pady=10)
            #entrada.grid(row=2, column=0, padx=10, pady=10)

        clicked = tk.StringVar()
        frame_filtro = tk.Frame(frameBuscarLibro, width= 400, height= 650, borderwidth=5, highlightthickness=3, highlightbackground="#61727C")
        frame_filtro.grid(row = 0, column=1, padx=20, pady=20)

        #Ventana de la derecha
        labelFiltro = tk.Label(frame_filtro, text="Filtro deseado", font=("verdana", 14), justify="center")
        drop = tk.OptionMenu(frame_filtro, clicked, *["Nombre","Autor","Genero"], command=despliegue)
        drop.grid(row=1, column=0, padx=10, pady=10)
        labelFiltro.grid(row=0, column=0, padx=10, pady=10)

        #Ventana izquierda
        # Iniciar el frame de resultados
        frame_listas = tk.Frame(frameBuscarLibro, width=600, height=650, borderwidth=5, padx=5, pady=5)
        frame_listas.grid(row=0, column=0, padx=20, pady=20)
        frame_lista = tk.Frame(frame_listas, width=600)
        frame_lista.grid(row=0, column=0, sticky="w")
        label_numeral = tk.Label(frame_lista, text="Numeral", width=7, height=1, justify="left",
                                 relief="groove")
        label_nombre = tk.Label(frame_lista, text="Nombre", width=20, height=1, justify="right",
                                relief="groove")
        label_autor = tk.Label(frame_lista, text="Autor", width=20, height=1, justify="left", relief="groove")
        label_genero = tk.Label(frame_lista, text="Genero", width=20, height=1, justify="left",
                                relief="groove")

        label_numeral.grid(row=0, column=0, sticky="w")
        label_nombre.grid(row=0, column=1, sticky="w")
        label_autor.grid(row=0, column=2, sticky="w")
        label_genero.grid(row=0, column=3, sticky="w")
        frame_listas.grid_propagate(False)

        return frameBuscarLibro

    @classmethod
    def generarFrameBuscarRevista(cls, biblioteca):
        frameBuscarRevista =  tk.Frame(width=1080, height=720)
        def despliegue_revista(filtro):
            if filtro.lower() == "categoria":
                msg = "Escribe la {} de la revista".format(filtro)
            else:
                msg = " Escribe el {} de la Revista ".format(filtro)
            #entrada = tk.Label(frame_filtro_revista, text=msg, font=("verdana", 14), padx = 10, pady = 10)
            #entryBusqueda = tk.Entry(frame_filtro_revista, font=("verdana", 12))

            fieldFrameBusqueda = FieldFrame(frame_filtro_revista, criterios=[msg])
            fieldFrameBusqueda.grid(row=2, column = 0)
            def Filtrar():
                try:

                    #string_Campo = entryBusqueda.get().lower()
                    string_Campo = fieldFrameBusqueda.getValue(0)
                    if string_Campo == "":
                        raise ExcepcionEntero()
                    elif 48 <= ord(string_Campo[0]) <= 57:
                        raise ExcepcionString()
                    resultados = []
                    # Reiniciar el frame de resultados
                    # frameAnterior.destroy()
                    frame_listas_revista = tk.Frame(frameBuscarRevista, width=600, height=650, borderwidth=5, padx=5, pady=5)
                    frame_listas_revista.grid(row=0, column=0, padx=20, pady=20)
                    frame_lista = tk.Frame(frame_listas_revista, width=600)
                    frame_lista.grid(row=0, column=0, sticky="w")
                    label_numeral = tk.Label(frame_lista, text="Numeral", width=7, height=1, justify="left",
                                             relief="groove")
                    label_nombre = tk.Label(frame_lista, text="Nombre", width=20, height=1, justify="right",
                                            relief="groove")
                    label_autor = tk.Label(frame_lista, text="Autor", width=20, height=1, justify="left", relief="groove")
                    label_genero = tk.Label(frame_lista, text="Categoria", width=20, height=1, justify="left",
                                            relief="groove")

                    label_numeral.grid(row=0, column=0, sticky="w")
                    label_nombre.grid(row=0, column=1, sticky="w")
                    label_autor.grid(row=0, column=2, sticky="w")
                    label_genero.grid(row=0, column=3, sticky="w")
                    frame_listas_revista.grid_propagate(False)
                    #entryBusqueda.delete(0, tk.END)
                    fieldFrameBusqueda.delValue(0)
                    filtro = clicked_revista.get().lower()
                    cantidad = 0
                    if filtro == "autor":
                        for revista in biblioteca.getRevistas():
                            if string_Campo in revista.getAutor().lower():
                                cantidad +=1
                                resultados.append(revista)


                    elif filtro == "nombre":
                        for revista in biblioteca.getRevistas():
                            if string_Campo in revista.getNombre().lower():
                                cantidad += 1
                                resultados.append(revista)

                    elif filtro == "categoria":
                        for revista in biblioteca.getRevistas():
                            if string_Campo in revista.getCategoria().lower():
                                cantidad += 1
                                resultados.append(revista)

                    if cantidad == 0:
                        print("EXCEPTION: NO SE ENCONTRARON RESULTADOS (esto iría en una ventana pequeña que se pueda cerrar y ya")
                    else:
                        for i in range(len(resultados)):
                            revista = resultados[i]
                            nombre_revista = revista.getNombre()
                            nombre_autor = revista.getAutor()
                            nombre_categoria = revista.getCategoria()
                            frame_revista = tk.Frame(frame_listas_revista, width=600)

                            label_numeral = tk.Label(frame_revista, text="{}. ".format(i+1), width=7, height=1, anchor="w",
                                                     relief="groove")
                            label_nombre = tk.Label(frame_revista, text=nombre_revista, width=20, height=1, anchor="w",
                                                    relief="groove")
                            label_autor = tk.Label(frame_revista, text=nombre_autor, width=20, height=1, anchor="w",
                                                   relief="groove")
                            label_genero = tk.Label(frame_revista, text=nombre_categoria, width=20, height=1, anchor="w",
                                                    relief="groove")

                            label_numeral.grid(row=0, column=0, sticky="w")
                            label_nombre.grid(row=0, column=1, sticky="w")
                            label_autor.grid(row=0, column=2, sticky="w")
                            label_genero.grid(row=0, column=3, sticky="w")
                            frame_revista.grid(row=i + 1, column=0, sticky="w")
                except ErrorApp as e:
                    Advertencia(str(e))
            botonBusqueda = tk.Button(frame_filtro_revista, text="Buscar", font=("verdana", 12), background="#61727C",
                                      fg="white", command=Filtrar)
            botonBusqueda.grid(row=4, column=0, padx=10, pady=10)
            #entryBusqueda.grid(row=3, column=0, padx=10, pady=10)
            #entrada.grid(row=2, column=0, padx=10, pady=10)

        clicked_revista = tk.StringVar()
        #Ventana izquierda
        frame_listas_revista = tk.Frame(frameBuscarRevista, width=600, height=650, borderwidth=5, padx=5, pady=5)
        frame_listas_revista.grid(row=0, column=0, padx=20, pady=20)
        frame_lista = tk.Frame(frame_listas_revista, width=600)
        frame_lista.grid(row=0, column=0, sticky="w")
        label_numeral = tk.Label(frame_lista, text="Numeral", width=7, height=1, justify="left",
                                 relief="groove")
        label_nombre = tk.Label(frame_lista, text="Nombre", width=20, height=1, justify="right",
                                relief="groove")
        label_autor = tk.Label(frame_lista, text="Autor", width=20, height=1, justify="left", relief="groove")
        label_genero = tk.Label(frame_lista, text="Categoria", width=20, height=1, justify="left",
                                relief="groove")

        label_numeral.grid(row=0, column=0, sticky="w")
        label_nombre.grid(row=0, column=1, sticky="w")
        label_autor.grid(row=0, column=2, sticky="w")
        label_genero.grid(row=0, column=3, sticky="w")
        frame_listas_revista.grid_propagate(False)

        frame_filtro_revista = tk.Frame(frameBuscarRevista, width= 400, height= 650, borderwidth=5, highlightthickness=3, highlightbackground="#61727C")
        frame_filtro_revista.grid(row = 0, column=1, padx=20, pady=20)

        #Ventana de la derecha
        labelFiltro = tk.Label(frame_filtro_revista, text="Filtro deseado", font=("verdana", 14), justify="center")
        drop_revista = tk.OptionMenu(frame_filtro_revista, clicked_revista, *["Nombre","Autor","Categoria"], command=despliegue_revista)
        drop_revista.grid(row=1, column=0, padx=10, pady=10)
        labelFiltro.grid(row=0, column=0, padx=10, pady=10)

        return frameBuscarRevista

    @classmethod
    def generarFrameMisPrestamos(cls, usuario):
        frameMisPrestamos =   tk.Frame(width=1080, height=720)
        frame_letrero = tk.Frame(frameMisPrestamos, width=1060, height=100, borderwidth=5, highlightthickness=3,
                                 highlightbackground="#61727C")
        frame_letrero.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        frame_libros = tk.Frame(frameMisPrestamos, width=520, height=570, borderwidth=5, highlightbackground="#61727C",
                                highlightthickness=3)
        frame_libros.grid(row=1, column=0, padx=10, pady=10)

        #LOGICA PARA LLENAR LA LISTA DE PRÉSTAMOS
        def ActualizarPrestamos():

            lista_prestamos = usuario.getPrestamos()
            contLibros = 1
            contRevistas = 1
            for prestamo in lista_prestamos:
                ejemplar = prestamo.getEjemplarEscogido()
                if isinstance(ejemplar, EjemplarLibro):
                    ejemplar = ejemplar.getLibro()

                    nombre_libro = ejemplar.getNombre()
                    nombre_autor = ejemplar.getAutor()
                    nombre_genero = ejemplar.getGenero()
                    # IMPLEMENTAR LO DE LISTAS ACÁ
                    frame_ejemplar = tk.Frame(frame_libros, width=600)
                    label_numeral = tk.Label(frame_ejemplar, text="{}. ".format(contLibros), width=7, height=1, anchor="w",
                                             relief="groove")
                    label_nombre = tk.Label(frame_ejemplar, text=nombre_libro, width=20, height=1, anchor="w",
                                            relief="groove")
                    label_autor = tk.Label(frame_ejemplar, text=nombre_autor, width=20, height=1, anchor="w",
                                           relief="groove")
                    label_genero = tk.Label(frame_ejemplar, text=nombre_genero, width=20, height=1, anchor="w",
                                            relief="groove")

                    label_numeral.grid(row=0, column=0, sticky="w")
                    label_nombre.grid(row=0, column=1, sticky="w")
                    label_autor.grid(row=0, column=2, sticky="w")
                    label_genero.grid(row=0, column=3, sticky="w")
                    frame_ejemplar.grid(row=contLibros, column=0)
                    contLibros+=1


                elif isinstance(ejemplar, EjemplarRevista):
                    ejemplar = ejemplar.getRevista()

                    nombre_revista = ejemplar.getNombre()
                    nombre_autor = ejemplar.getAutor()
                    nombre_categoria = ejemplar.getCategoria()
                    # IMPLEMENTAR LO DE LISTAS ACÁ
                    frame_ejemplar = tk.Frame(frame_revistas, width=600)

                    label_numeral = tk.Label(frame_ejemplar, text="{}. ".format(contRevistas), width=7, height=1, anchor="w",
                                             relief="groove")
                    label_nombre = tk.Label(frame_ejemplar, text=nombre_revista, width=20, height=1, anchor="w",
                                            relief="groove")
                    label_autor = tk.Label(frame_ejemplar, text=nombre_autor, width=20, height=1, anchor="w",
                                           relief="groove")
                    label_genero = tk.Label(frame_ejemplar, text=nombre_categoria, width=20, height=1, anchor="w",
                                            relief="groove")

                    label_numeral.grid(row=0, column=0, sticky="w")
                    label_nombre.grid(row=0, column=1, sticky="w")
                    label_autor.grid(row=0, column=2, sticky="w")
                    label_genero.grid(row=0, column=3, sticky="w")
                    frame_ejemplar.grid(row=contRevistas, column=0, sticky="w")
                    contRevistas+=1

            if contLibros == 1 and contRevistas == 1:
                print("LO SENTIMOS NO HAY NADA QUE MOSTRAR")
        frame_revistas = tk.Frame(frameMisPrestamos, width=520, height=570, borderwidth=5, highlightthickness=3,
                                  highlightbackground="#61727C")
        frame_revistas.grid(row=1, column=1, padx=10, pady=10)
        boton_actualizar = tk.Button(frame_letrero, width=20, height= 2, text = "Actualizar", command=ActualizarPrestamos,font = ("verdana", 12),background="#61727C", fg= "white")
        boton_actualizar.grid(row = 0, column=0, sticky="w", padx=10)


        letrero = tk.Label(frame_letrero, text="Mis prestamos", font=("verdana", 16, "bold"), fg="white", borderwidth=3,
                           background="#61727C", width=20, height=2)
        letrero.grid(row=0, column=1, padx= 10)

        letrero_libros = tk.Label(frame_libros, text="Libros", font=("verdana", 14, "bold"), fg="white", borderwidth=3,
                                  background="#61727C", width=10, height=2)
        letrero_libros.grid(row=0, column=0, pady=10, sticky="w")
        frame_libros.grid_propagate(False)
        letrero_revista = tk.Label(frame_revistas, text="Revistas", font=("verdana", 14, "bold"), fg="white",
                                   borderwidth=3, background="#61727C", width=10, height=2)
        letrero_revista.grid(row=0, column=0, padx=5, pady=10, sticky="w")
        frame_revistas.grid_propagate(False)

        return frameMisPrestamos

    @classmethod
    def generarFrameRecomendarLibro(cls, usuario, biblioteca):
        frameRecomendarLibro =   tk.Frame(width=1080, height=720)
        # Contenedores principales
        frame_letrero = tk.Frame(frameRecomendarLibro, width=1060, height=100, borderwidth=5, highlightthickness=3,
                                 highlightbackground="#61727C")
        frame_letrero.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        frame_libros = tk.Frame(frameRecomendarLibro, width=1060, height=570, borderwidth=5, highlightbackground="#61727C",
                                highlightthickness=3)
        frame_libros.grid(row=1, column=0, padx=10, pady=10)

        usuario.encontrarGeneroFavorito()
        if usuario.getGeneroFavorito() == 0:
            print("NO TIENE UN GÉNERO FAVORITO")
            label_sinGenero = tk.Label(frame_libros, font=("verdana", 12, "bold"), text="Aun no cuenta con genero favorito.\nRealice prestamos o reservas para encontaralo.", width=50)
            label_sinGenero.grid(row = 0, column = 0, pady = 225, padx = 250)

        else:

            librosMasSolicitados = Libro.masSolicitados(biblioteca, usuario.getGeneroFavorito())

            frame_info = tk.Frame(frame_libros, width=500, height=50)
            label_nombre = tk.Label(frame_info, font=("verdana", 12, "bold"), text="Nombre", width=30)
            label_autor = tk.Label(frame_info, font=("verdana", 12, "bold"), text="Autor", width=30)
            label_genero = tk.Label(frame_info, font=("verdana", 12, "bold"), text="Genero", width=15)

            label_nombre.grid(row=0, column=1, sticky="w", pady=10)
            label_autor.grid(row=0, column=2, sticky="w", pady=10)
            label_genero.grid(row=0, column=3, sticky="w", pady=10)
            frame_info.grid(row=0, column=0, sticky="w", pady=10)
            for i in range(len(librosMasSolicitados)):
                numeral = i+1
                nombre_libro = librosMasSolicitados[i].getNombre()
                nombre_autor = librosMasSolicitados[i].getAutor()
                nombre_genero = librosMasSolicitados[i].getGenero()


                frame_info = tk.Frame(frame_libros, width=500, height = 50)
                label_numeral = tk.Label(frame_info,font = ("verdana", 12, "bold"), text = numeral,width = 3, anchor= "w")
                label_nombre = tk.Label(frame_info, font=("verdana", 12, "bold"), text = nombre_libro,width = 30, anchor= "w")
                label_autor = tk.Label(frame_info, font=("verdana", 12, "bold"), text = nombre_autor,width = 30, anchor= "w")
                label_genero = tk.Label(frame_info, font=("verdana", 12, "bold"), text = nombre_genero,width = 30, anchor= "w")

                label_numeral.grid(row = 0, column= 0, sticky ="w", pady=10)
                label_nombre.grid(row=0, column=1, sticky ="w", pady=10)
                label_autor.grid(row=0, column=2, sticky ="w", pady=10)
                label_genero.grid(row=0, column=3, sticky ="w", pady=10)
                frame_info.grid(row = i+1, column = 0, sticky ="w", pady=10)

        # Letrero
        letrero = tk.Label(frame_letrero, text="Libros recomendados para ti", font=("verdana", 16, "bold"), fg="white",
                           borderwidth=3, background="#61727C", width=30, height=2)
        letrero.grid(row=0, column=0)

        # Evitar que el grid cambie de tamaño
        frame_libros.grid_propagate(False)

        return frameRecomendarLibro

    @classmethod
    def generarFrameRecomendarRevista(cls, usuario, biblioteca):
        frameRecomendarRevista = tk.Frame(width=1080, height=720)
        # Contenedores principales
        frame_letrero = tk.Frame(frameRecomendarRevista, width=1060, height=100, borderwidth=5, highlightthickness=3, highlightbackground="#61727C")
        frame_letrero.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        frame_revistas = tk.Frame(frameRecomendarRevista, width=1060, height=570, borderwidth=5, highlightbackground="#61727C", highlightthickness=3)
        frame_revistas.grid(row=1, column=0, padx=10, pady=10)

        usuario.encontrarCategoriaFavorita()
        if usuario.getCategoriaFavorita() == 0:
            print("NO TIENE UNA CATEGORÍA FAVORITA")
            label_sinCategoria = tk.Label(frame_revistas, font=("verdana", 12, "bold"),
                                       text="Aun no cuenta con Categoria favorita.\nRealice prestamos o reservas para encontarala.",
                                       width=50)
            label_sinCategoria.grid(row=0, column=0, pady=225, padx=250)
        else:
            revistasMasSolicitadas = Revista.masSolicitadas(biblioteca, usuario.getCategoriaFavorita())

            frame_info = tk.Frame(frame_revistas, width=500, height=50)
            label_nombre = tk.Label(frame_info, font=("verdana", 12, "bold"), text="Nombre", width=30)
            label_autor = tk.Label(frame_info, font=("verdana", 12, "bold"), text="Autor", width=30)
            label_genero = tk.Label(frame_info, font=("verdana", 12, "bold"), text="Categoria", width=15)

            label_nombre.grid(row=0, column=1, sticky="w", pady=10)
            label_autor.grid(row=0, column=2, sticky="w", pady=10)
            label_genero.grid(row=0, column=3, sticky="w", pady=10)
            frame_info.grid(row=0, column=0, sticky="w", pady=10)
            for i in range(len(revistasMasSolicitadas)):
                numeral = i + 1
                nombre_revista= revistasMasSolicitadas[i].getNombre()
                nombre_autor = revistasMasSolicitadas[i].getAutor()
                nombre_categoria = revistasMasSolicitadas[i].getCategoria()

                frame_info = tk.Frame(frame_revistas, width=500, height=50)
                label_numeral = tk.Label(frame_info, font=("verdana", 12, "bold"), text=numeral, width=3, anchor="w")
                label_nombre = tk.Label(frame_info, font=("verdana", 12, "bold"), text=nombre_revista, width=30, anchor="w")
                label_autor = tk.Label(frame_info, font=("verdana", 12, "bold"), text=nombre_autor, width=30, anchor="w")
                label_genero = tk.Label(frame_info, font=("verdana", 12, "bold"), text=nombre_categoria, width=30, anchor="w")

                label_numeral.grid(row=0, column=0, sticky="w", pady=10)
                label_nombre.grid(row=0, column=1, sticky="w", pady=10)
                label_autor.grid(row=0, column=2, sticky="w", pady=10)
                label_genero.grid(row=0, column=3, sticky="w", pady=10)
                frame_info.grid(row=i + 1, column=0, sticky="w", pady=10)
        # Letrero
        letrero = tk.Label(frame_letrero, text="Revistas recomendadas para ti", font=("verdana", 16, "bold"),
                           fg="white", borderwidth=3, background="#61727C", width=30, height=2)
        letrero.grid(row=0, column=0)

        # Evitar que el grid cambie de tamaño
        frame_revistas.grid_propagate(False)

        return frameRecomendarRevista

    @classmethod
    def generarFrameDevolucion(cls, usuario, biblioteca):
        frameDevolucion = tk.Frame(width=1080, height=720)
        frame_listas = tk.Frame(frameDevolucion, width=600, height=650, borderwidth=5, padx=5, pady=5)
        frame_listas.grid(row=0, column=0, padx=20, pady=20)
        frame_listas.grid_propagate(False)

        frame_filtro = tk.Frame(frameDevolucion, width=400, height=650, borderwidth=5, highlightthickness=3,
                                highlightbackground="#61727C")
        frame_filtro.grid(row=0, column=1, padx=20, pady=20)

        #Funcion que llama a la devolcion
        def devolucion():
            try:
                #indice = entryDevolucion.get()
                indice = fieldFrameDevolucion.getValue(0)
                if indice == "":
                    raise ExcepcionEntero()
                elif not (48 <= ord(indice[0]) <= 57):
                    raise ExcepcionEntero()
                indice = int(indice) - 1
                if indice >= len(usuario.getPrestamos()) or indice < 0:
                    raise ExcepcionElementoInexistente()

                else:
                    Prestamo.devolucion(indice, biblioteca, usuario)
                    #entryDevolucion.delete(0, tk.END)
                    fieldFrameDevolucion.delValue(0)
                    print("DEVOLCION EXITOSA")

                frame_listas.grid_forget()
                generarListaPrestamos()
            except ErrorApp as e:
                Advertencia(str(e))


        #Ventana izquierda
        def generarListaPrestamos():
            frame_listas = tk.Frame(frameDevolucion, width=600, height=650, borderwidth=5, padx=5, pady=5)
            frame_listas.grid(row=0, column=0, padx=20, pady=20)
            frame_listas.grid_propagate(False)

            # 5 dias, 3 semanas, 2 meses

            # Frame de la izquierda
            # frame_revista_info = Frame(frameIZQ, width=400, height=40, borderwidth=1, padx=5, pady=5)
            # frame_revista_info.grid(column=0, row=0, padx=4, pady=5, columnspan=10)

            frame_lista = tk.Frame(frame_listas, width=600, height=20)
            frame_lista.grid(row=0, column=0, sticky="w", pady = 5)
            label_numeral = tk.Label(frame_lista, text="Numeral", width=7, height=1, justify="left", relief="groove")
            label_nombre = tk.Label(frame_lista, text="Nombre", width=20, height=1, justify="right", relief="groove")
            label_autor = tk.Label(frame_lista, text="Autor", width=20, height=1, justify="left", relief="groove")
            label_genero = tk.Label(frame_lista, text="Tipo", width=20, height=1, justify="left", relief="groove")

            label_numeral.grid(row=0, column=0, sticky="w")
            label_nombre.grid(row=0, column=1, sticky="w")
            label_autor.grid(row=0, column=2, sticky="w")
            label_genero.grid(row=0, column=3, sticky="w")

            # label_total = Label(frame_lista, text="Formato: Numeral  -  Nombre  -  Autor  -  Genero")
            # label_total.grid(row=0, column=0, sticky="nw")

            for r in range(1, len(usuario.getPrestamos()) + 1):
                if isinstance(usuario.getPrestamos()[r - 1].getEjemplarEscogido(), EjemplarLibro):
                    tiuloPrestado = usuario.getPrestamos()[r -1].getEjemplarEscogido().getLibro()
                    tipo = "Libro"
                else:
                    tiuloPrestado = usuario.getPrestamos()[r - 1].getEjemplarEscogido().getRevista()
                    tipo = "Revista"
                nombre_libro = tiuloPrestado.getNombre()
                nombre_autor = tiuloPrestado.getAutor()


                frame_lista = tk.Frame(frame_listas, width=600)
                frame_lista.grid(row=r + 1, column=0, sticky="w")

                label_numeral = tk.Label(frame_lista, text="{}. ".format(r), width=7, height=1, anchor="w",
                                         relief="groove")
                label_nombre = tk.Label(frame_lista, text=nombre_libro, width=20, height=1, anchor="w", relief="groove")
                label_autor = tk.Label(frame_lista, text=nombre_autor, width=20, height=1, anchor="w", relief="groove")
                label_genero = tk.Label(frame_lista, text=tipo, width=20, height=1, anchor="w",
                                        relief="groove")

                label_numeral.grid(row=0, column=0, sticky="w")
                label_nombre.grid(row=0, column=1, sticky="w")
                label_autor.grid(row=0, column=2, sticky="w")
                label_genero.grid(row=0, column=3, sticky="w")

        generarListaPrestamos()
        # Ventana de la derecha
        msg = "Escriba el numero de la devolucion\n que desea realizar"
        #entrada = tk.Label(frame_filtro, text=msg, font=("verdana", 14), padx=10, pady=10)
        #entryDevolucion = tk.Entry(frame_filtro, font=("verdana", 12))
        fieldFrameDevolucion= FieldFrame(frame_filtro, criterios=[msg])
        botonDevolcion = tk.Button(frame_filtro, text="Devolver", font=("verdana", 12), background="#61727C", fg="white", command = devolucion)

        fieldFrameDevolucion.grid(row=2, column=0, padx = 5)
        botonDevolcion.grid(row=4, column=0, padx=5, pady=10)
        #entryDevolucion.grid(row=3, column=0, padx=5, pady=10)
        #entrada.grid(row=2, column=0, padx=5, pady=10)

        return frameDevolucion

    @classmethod
    def generarFrameCancelacion(cls, usuario, biblioteca):
        frameCancelacion = tk.Frame(width=1080, height=720)
        frame_listas = tk.Frame(frameCancelacion, width=600, height=650, borderwidth=5, padx=5, pady=5)
        frame_listas.grid(row=0, column=0, padx=20, pady=20)
        frame_listas.grid_propagate(False)

        frame_filtro = tk.Frame(frameCancelacion, width=400, height=650, borderwidth=5, highlightthickness=3,
                                highlightbackground="#61727C")
        frame_filtro.grid(row=0, column=1, padx=20, pady=20)

        # Funcion que llama a la devolcion
        def cancelacion():
            try:
                #indice = entryDevolucion.get()
                indice = fieldFrameDevolucion.getValue(0)
                if indice == "":
                    raise ExcepcionEntero()
                elif not (48 <= ord(indice[0]) <= 57):
                    raise ExcepcionEntero()
                indice = int(indice) - 1
                if indice >= len(usuario.getReservas())  or indice < 0:
                    raise ExcepcionElementoInexistente()

                else:
                    Reserva.cancelarReserva(indice, biblioteca, usuario)
                    #entryDevolucion.delete(0, tk.END)
                    fieldFrameDevolucion.delValue(0)
                    print("CANCELACION EXITOSA")

                frame_listas.grid_forget()
                generarListaReservas()

            except ErrorApp as e:
                Advertencia(str(e))

        # Ventana izquierda
        def generarListaReservas():
            frame_listas = tk.Frame(frameCancelacion, width=600, height=650, borderwidth=5, padx=5, pady=5)
            frame_listas.grid(row=0, column=0, padx=20, pady=20)
            frame_listas.grid_propagate(False)

            # 5 dias, 3 semanas, 2 meses

            # Frame de la izquierda
            # frame_revista_info = Frame(frameIZQ, width=400, height=40, borderwidth=1, padx=5, pady=5)
            # frame_revista_info.grid(column=0, row=0, padx=4, pady=5, columnspan=10)

            frame_lista = tk.Frame(frame_listas, width=600, height=20)
            frame_lista.grid(row=0, column=0, sticky="w", pady=5)
            label_numeral = tk.Label(frame_lista, text="Numeral", width=7, height=1, justify="left", relief="groove")
            label_nombre = tk.Label(frame_lista, text="Nombre", width=20, height=1, justify="right", relief="groove")
            label_autor = tk.Label(frame_lista, text="Autor", width=20, height=1, justify="left", relief="groove")
            label_genero = tk.Label(frame_lista, text="Tipo", width=20, height=1, justify="left", relief="groove")
            label_fecha = tk.Label(frame_lista, text="Devolucion", width=10, height=1, anchor="w",relief="groove")


            label_numeral.grid(row=0, column=0, sticky="w")
            label_nombre.grid(row=0, column=1, sticky="w")
            label_autor.grid(row=0, column=2, sticky="w")
            label_genero.grid(row=0, column=3, sticky="w")
            label_fecha.grid(row=0, column=4, sticky="w")


            # label_total = Label(frame_lista, text="Formato: Numeral  -  Nombre  -  Autor  -  Genero")
            # label_total.grid(row=0, column=0, sticky="nw")

            for r in range(1, len(usuario.getReservas()) + 1):
                if isinstance(usuario.getReservas()[r - 1].getEjemplarEscogido(), EjemplarLibro):
                    tiuloReservado = usuario.getReservas()[r - 1].getEjemplarEscogido().getLibro()
                    tipo = "Libro"
                else:
                    tiuloReservado = usuario.getReservas()[r - 1].getEjemplarEscogido().getRevista()
                    tipo = "Revista"
                nombre_libro = tiuloReservado.getNombre()
                nombre_autor = tiuloReservado.getAutor()
                fecha = "{}/{}/{}".format(usuario.getReservas()[r - 1].getFechaDevolucion().day,
                                          usuario.getReservas()[r - 1].getFechaDevolucion().month,
                                          usuario.getReservas()[r - 1].getFechaDevolucion().year)

                frame_lista = tk.Frame(frame_listas, width=600)
                frame_lista.grid(row=r + 1, column=0, sticky="w")

                label_numeral = tk.Label(frame_lista, text="{}. ".format(r), width=7, height=1, anchor="w",
                                         relief="groove")
                label_nombre = tk.Label(frame_lista, text=nombre_libro, width=20, height=1, anchor="w", relief="groove")
                label_autor = tk.Label(frame_lista, text=nombre_autor, width=20, height=1, anchor="w", relief="groove")
                label_genero = tk.Label(frame_lista, text=tipo, width=20, height=1, anchor="w",
                                        relief="groove")
                label_fecha = tk.Label(frame_lista, text=fecha, width=10, height=1, anchor="w",
                                       relief="groove")



                label_numeral.grid(row=0, column=0, sticky="w")
                label_nombre.grid(row=0, column=1, sticky="w")
                label_autor.grid(row=0, column=2, sticky="w")
                label_genero.grid(row=0, column=3, sticky="w")
                label_fecha.grid(row=0, column=4, sticky="w")

        generarListaReservas()
        # Ventana de la derecha
        msg = "Escriba el numero de la reserva\n que desea cancelar"
        #entrada = tk.Label(frame_filtro, text=msg, font=("verdana", 14), padx=10, pady=10)
        #entryDevolucion = tk.Entry(frame_filtro, font=("verdana", 12))
        fieldFrameDevolucion = FieldFrame(frame_filtro, criterios=[msg])
        botonDevolcion = tk.Button(frame_filtro, text="Cancelar", font=("verdana", 12), background="#61727C",
                                   fg="white", command=cancelacion)

        fieldFrameDevolucion.grid(row=2, column=0,padx=5)
        botonDevolcion.grid(row=4, column=0, padx=5, pady=10)
        #entryDevolucion.grid(row=3, column=0, padx=5, pady=10)
        #entrada.grid(row=2, column=0, padx=5, pady=10)

        return frameCancelacion