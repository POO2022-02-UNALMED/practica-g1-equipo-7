from datetime import datetime, timedelta

from tkinter import *
import tkinter as tk
from Python.baseDatos.serializador import serializarTodo
from Python.gestorAplicacion.libreria.biblioteca import Biblioteca
from Python.gestorAplicacion.libreria.ejemplarLibro import EjemplarLibro
from Python.gestorAplicacion.libreria.ejemplarRevista import EjemplarRevista

from Python.gestorAplicacion.servicios.prestamo import Prestamo
from Python.gestorAplicacion.libreria.libro import Libro
from Python.gestorAplicacion.servicios.servicio import Servicio
from Python.gestorAplicacion.libreria.revista import Revista
from Python.gestorAplicacion.servicios.reserva import Reserva





class VentanaUsuario(Tk):


    frames = []

    def __init__(self, biblioteca, usuario ):
        super().__init__()
        self._biblioteca_main = biblioteca
        self._usuario = usuario

        self.title("JJ-Sales - Ventana del Usuario")
        self.geometry("1080x720")
        self.option_add("*tearOff", False)
        self.resizable(False, False)

        #Creando el menú

        self._barra_del_menu = Menu(self)
        archivo = Menu(self._barra_del_menu)
        archivo.add_command(label = "Aplicacion", command = lambda: informacion())
        archivo.add_command(label = "Salir y guardar", command = lambda: Guardar())

        self._barra_del_menu.add_cascade(label = "Archivo" , menu = archivo)


        # Se crea el desplegable de procesos y consultas

        procesos_consultas = Menu(self._barra_del_menu)


        #se añaden los demás desplegables


        #Desplegable de consultas
        #Funcionalidad 0
        info_biblioteca = Menu(self._barra_del_menu)
        info_biblioteca.add_command(label = "Buscar libro" , command = lambda: cambiarFrame(FrameBuscarLibro))
        info_biblioteca.add_command(label = "Buscar revista" , command = lambda: cambiarFrame(FrameBuscarRevista))
        info_biblioteca.add_command(label = "Mis prestamos" , command = lambda: cambiarFrame(FrameMisPrestamos))
        info_biblioteca.add_command(label="Mis reservas", command = lambda: cambiarFrame(FrameMisReservas))

        procesos_consultas.add_cascade(label = "Consultas", menu = info_biblioteca)


        #FUNCIONALIDADES
        #1. Reservas
        realizar_reserva = Menu(self._barra_del_menu)
        realizar_reserva.add_command(label="Reservar libro", command=lambda: cambiarFrame(FrameReservarLibro))
        realizar_reserva.add_command(label="Reservar revista", command=lambda: cambiarFrame(FrameReservarRevista))
        procesos_consultas.add_cascade(label="Realizar reserva", menu=realizar_reserva)

        #2. Prestamos
        realizar_prestamo = Menu(self._barra_del_menu)
        realizar_prestamo.add_command(label="Prestar libro", command=lambda: cambiarFrame(FramePrestarLibro))
        realizar_prestamo.add_command(label="Prestar revista", command=lambda: cambiarFrame(FramePrestarRevista))
        procesos_consultas.add_cascade(label="Realizar prestamo", menu=realizar_prestamo)

        #3. Recomendaciones
        recomendacion = Menu(self._barra_del_menu)
        recomendacion.add_command(label="Recomendar libro", command=lambda: cambiarFrame(Frame()))
        recomendacion.add_command(label="Recomendar revista", command=lambda: cambiarFrame(Frame()))
        procesos_consultas.add_cascade(label="Recomendaciones", menu=recomendacion)

        #4 Gestionar servicios
        gestion_servicios = Menu(self._barra_del_menu)
        gestion_servicios.add_command(label="Realizar devolucion", command=lambda: cambiarFrame(Frame()))
        gestion_servicios.add_command(label="Cancelar reserva ", command=lambda: cambiarFrame(Frame()))
        procesos_consultas.add_cascade(label="Gestionar servicios", menu=gestion_servicios)


        #desplegable de ayuda
        ayuda = Menu(self._barra_del_menu)
        ayuda.add_command(label="Sobre", command=lambda: Ayuda())


        self._barra_del_menu.add_cascade(label = "Procesos y consultas", menu = procesos_consultas)
        self._barra_del_menu.add_cascade(label = "Ayuda", menu = ayuda)








        self.config(menu = self._barra_del_menu)

        #GENERACIÓN DE FRAMES



        FramePrestarLibro = Prestamo.generarFramePrestamoLibro(self._usuario, self._biblioteca_main)
        FramePrestarRevista = Prestamo.generarFramePrestamoRevista(self._usuario, self._biblioteca_main)

        VentanaUsuario.frames.append(FramePrestarLibro)
        VentanaUsuario.frames.append(FramePrestarRevista)
        FrameBuscarLibro = Frame(self)


        def despliegue(filtro):
            entrada = Label(frame_filtro, text="Escribe el {} del libro".format(filtro), font=("verdana", 14), padx = 10, pady = 10)
            entryBusqueda = Entry(frame_filtro, font=("verdana", 12))

            def Filtrar():
                string_Campo = entryBusqueda.get().lower()
                resultados = []
                # Reiniciar el frame de resultados
                #frameAnterior.destroy()
                frame_listas = Frame(FrameBuscarLibro, width=600, height=650, borderwidth=5, padx=5, pady=5)
                frame_listas.grid(row=0, column=0, padx=20, pady=20)
                frame_lista = tk.Frame(frame_listas, width=600)
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
                frame_listas.grid_propagate(False)
                entryBusqueda.delete(0, END)
                filtro = clicked.get().lower()
                cantidad = 0
                if filtro == "autor":
                    for libro in Biblioteca.getLibros():
                        if string_Campo in libro.getAutor().lower():
                            cantidad += 1
                            resultados.append(libro)

                elif filtro == "nombre":
                    for libro in Biblioteca.getLibros():
                        if string_Campo in libro.getNombre().lower():
                            cantidad += 1
                            resultados.append(libro)

                elif filtro == "genero":
                    for libro in Biblioteca.getLibros():
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

            botonBusqueda = Button(frame_filtro, text="Buscar", font=("verdana", 12), background="#61727C",
                                      fg="white", command=Filtrar)
            botonBusqueda.grid(row=4, column=0, padx=10, pady=10)
            entryBusqueda.grid(row=3, column=0, padx=10, pady=10)
            entrada.grid(row=2, column=0, padx=10, pady=10)

        clicked = StringVar()
        frame_filtro = Frame(FrameBuscarLibro, width= 400, height= 650, borderwidth=5, highlightthickness=3, highlightbackground="#61727C")
        frame_filtro.grid(row = 0, column=1, padx=20, pady=20)

        #Ventana de la derecha
        labelFiltro = Label(frame_filtro, text="Filtro deseado", font=("verdana", 14), justify="center")
        drop = tk.OptionMenu(frame_filtro, clicked, *["Nombre","Autor","Genero"], command=despliegue)
        drop.grid(row=1, column=0, padx=10, pady=10)
        labelFiltro.grid(row=0, column=0, padx=10, pady=10)

        #Ventana izquierda
        # Iniciar el frame de resultados
        frame_listas = Frame(FrameBuscarLibro, width=600, height=650, borderwidth=5, padx=5, pady=5)
        frame_listas.grid(row=0, column=0, padx=20, pady=20)
        frame_lista = tk.Frame(frame_listas, width=600)
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
        frame_listas.grid_propagate(False)



        VentanaUsuario.frames.append(FrameBuscarLibro)







        FrameBuscarRevista = Frame(self)

        def despliegue_revista(filtro):
            if filtro.lower() == "categoria":
                msg = "Escribe la {} de la revista".format(filtro)
            else:
                msg = " Escribe el {} de la Revista ".format(filtro)
            entrada = Label(frame_filtro_revista, text=msg, font=("verdana", 14), padx = 10, pady = 10)
            entryBusqueda = Entry(frame_filtro_revista, font=("verdana", 12))

            def Filtrar():
                string_Campo = entryBusqueda.get().lower()
                resultados = []
                # Reiniciar el frame de resultados
                # frameAnterior.destroy()
                frame_listas_revista = Frame(FrameBuscarRevista, width=600, height=650, borderwidth=5, padx=5, pady=5)
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
                entryBusqueda.delete(0, END)
                filtro = clicked_revista.get().lower()
                print(filtro)
                print(string_Campo)
                cantidad = 0
                if filtro == "autor":
                    for revista in Biblioteca.getRevistas():
                        if string_Campo in revista.getAutor().lower():
                            cantidad +=1
                            resultados.append(revista)


                elif filtro == "nombre":
                    for revista in Biblioteca.getRevistas():
                        if string_Campo in revista.getNombre().lower():
                            cantidad += 1
                            resultados.append(revista)

                elif filtro == "categoria":
                    for revista in Biblioteca.getRevistas():
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

            botonBusqueda = Button(frame_filtro_revista, text="Buscar", font=("verdana", 12), background="#61727C",
                                      fg="white", command=Filtrar)
            botonBusqueda.grid(row=4, column=0, padx=10, pady=10)
            entryBusqueda.grid(row=3, column=0, padx=10, pady=10)
            entrada.grid(row=2, column=0, padx=10, pady=10)

        clicked_revista = StringVar()
        #Ventana izquierda
        frame_listas_revista = Frame(FrameBuscarRevista, width=600, height=650, borderwidth=5, padx=5, pady=5)
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

        frame_filtro_revista = Frame(FrameBuscarRevista, width= 400, height= 650, borderwidth=5, highlightthickness=3, highlightbackground="#61727C")
        frame_filtro_revista.grid(row = 0, column=1, padx=20, pady=20)

        #Ventana de la derecha
        labelFiltro = Label(frame_filtro_revista, text="Filtro deseado", font=("verdana", 14), justify="center")
        drop_revista = tk.OptionMenu(frame_filtro_revista, clicked_revista, *["Nombre","Autor","Categoria"], command=despliegue_revista)
        drop_revista.grid(row=1, column=0, padx=10, pady=10)
        labelFiltro.grid(row=0, column=0, padx=10, pady=10)

        VentanaUsuario.frames.append(FrameBuscarRevista)

        FrameMisPrestamos = Frame(self)

        frame_letrero = tk.Frame(FrameMisPrestamos, width=1060, height=100, borderwidth=5, highlightthickness=3,
                                 highlightbackground="#61727C")
        frame_letrero.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        frame_libros = tk.Frame(FrameMisPrestamos, width=520, height=570, borderwidth=5, highlightbackground="#61727C",
                                highlightthickness=3)
        frame_libros.grid(row=1, column=0, padx=10, pady=10)

        #LOGICA PARA LLENAR LA LISTA DE PRÉSTAMOS
        def ActualizarPrestamos():
            lista_prestamos = self._usuario.getPrestamos()
            contLibros = 1
            contRevistas = 1
            for prestamo in lista_prestamos:
                ejemplar = prestamo.getEjemplarEscogido()
                if isinstance(ejemplar, EjemplarLibro):
                    ejemplar = ejemplar.getLibro()
                    print("hola")
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
                    print("hola")
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


        frame_revistas = tk.Frame(FrameMisPrestamos, width=520, height=570, borderwidth=5, highlightthickness=3,
                                  highlightbackground="#61727C")
        frame_revistas.grid(row=1, column=1, padx=10, pady=10)
        boton_actualizar = Button(frame_letrero, width=20, height= 2, text = "Actualizar", command=ActualizarPrestamos,font = ("verdana", 12),background="#61727C", fg= "white")
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
        letrero_revista.grid(row=0, column=0, padx=5, pady=15, sticky="w")
        frame_revistas.grid_propagate(False)
        VentanaUsuario.frames.append(FrameMisPrestamos)

        #frame de mis reservas
        FrameMisReservas = Frame(self)

        frame_letrero_reservas = tk.Frame(FrameMisReservas, width=1060, height=100, borderwidth=5, highlightthickness=3,
                                 highlightbackground="#61727C")
        frame_letrero_reservas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        frame_libros_reservas = tk.Frame(FrameMisReservas, width=520, height=570, borderwidth=5, highlightbackground="#61727C",
                                highlightthickness=3)
        frame_libros_reservas.grid(row=1, column=0, padx=10, pady=10)

        # LOGICA PARA LLENAR LA LISTA DE PRÉSTAMOS
        def ActualizarReservas():
            lista_reservas = self._usuario.getReservas()
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
                    # IMPLEMENTAR LO DE LISTAS ACÁ
                    frame_ejemplar = tk.Frame(frame_libros_reservas, width=600)
                    label_numeral = tk.Label(frame_ejemplar, text="{}. ".format(contLibros), width=7, height=1,
                                             anchor="w",
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
                    contLibros += 1


                elif isinstance(ejemplar, EjemplarRevista):
                    ejemplar = ejemplar.getRevista()
                    print("hola")
                    nombre_revista = ejemplar.getNombre()
                    nombre_autor = ejemplar.getAutor()
                    nombre_categoria = ejemplar.getCategoria()
                    # IMPLEMENTAR LO DE LISTAS ACÁ
                    frame_ejemplar = tk.Frame(frame_revistas_reservas, width=600)

                    label_numeral = tk.Label(frame_ejemplar, text="{}. ".format(contRevistas), width=7, height=1,
                                             anchor="w",
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
                    contRevistas += 1

        frame_revistas_reservas = tk.Frame(FrameMisReservas, width=520, height=570, borderwidth=5, highlightthickness=3,
                                  highlightbackground="#61727C")
        frame_revistas_reservas.grid(row=1, column=1, padx=10, pady=10)
        boton_actualizar_reservas = Button(frame_letrero_reservas, width=20, height=2, text="Actualizar", command=ActualizarReservas,
                                  font=("verdana", 12), background="#61727C", fg="white")
        boton_actualizar_reservas.grid(row=0, column=0, sticky="w", padx=10)

        letrero_reservas = tk.Label(frame_letrero_reservas, text="Mis Reservas", font=("verdana", 16, "bold"), fg="white", borderwidth=3,
                           background="#61727C", width=20, height=2)
        letrero_reservas.grid(row=0, column=1, padx=10)

        letrero_libros_reservas = tk.Label(frame_libros_reservas, text="Libros", font=("verdana", 14, "bold"), fg="white", borderwidth=3,
                                  background="#61727C", width=10, height=2)
        letrero_libros_reservas.grid(row=0, column=0, pady=10, sticky="w")
        frame_libros_reservas.grid_propagate(False)
        letrero_revista_reservas = tk.Label(frame_revistas_reservas, text="Revistas", font=("verdana", 14, "bold"), fg="white",
                                   borderwidth=3, background="#61727C", width=10, height=2)
        letrero_revista_reservas.grid(row=0, column=0, padx=5, pady=15, sticky="w")
        frame_revistas_reservas.grid_propagate(False)
        VentanaUsuario.frames.append(FrameMisReservas)


        FrameReservarLibro = Frame(self)

        def despliegue_reserva_libro(filtro):
            cantidad_tiempo = int(filtro.split(" ")[0])
            print(cantidad_tiempo)
            msg = "Escribe el numero del libro\n que desea reservar"
            entrada = Label(frame_filtro_reserva_libro, text = msg, font=("verdana", 14), padx = 10, pady = 10)
            entryBusqueda = Entry(frame_filtro_reserva_libro, font=("verdana", 12))
            def HacerReservaLibro():
                indice = int(entryBusqueda.get()) - 1

                if indice > len(Servicio.getEjemplarLibroDisponibles()) or indice < 0:
                    print("RAISEAR UN ERROR: no se encontró ese libro")
                else:
                    print(indice)
                    Ejemplar = Servicio.getEjemplarLibroDisponibles()[indice]
                    entryBusqueda.delete(0, END)
                    fecha_inicial = datetime.now()
                    fecha_final = datetime.now()
                    if cantidad_tiempo == 5:
                        fecha_final += timedelta(days=5)

                    elif cantidad_tiempo == 3:
                        fecha_final += timedelta(weeks=3)

                    elif cantidad_tiempo == 2:
                        fecha_final += timedelta(weeks=8)

                    Reserva.generarReservaLibro(self._usuario, Ejemplar, self._biblioteca_main, fecha_final, fecha_inicial)
                    print(f"RESERVA EXITOSO {Ejemplar.getLibro().getNombre()} para el {fecha_inicial, fecha_final}")




            botonBusqueda = Button(frame_filtro_reserva_libro, text="Reservar", font=("verdana", 12), background="#61727C",
                                      fg="white", command=HacerReservaLibro)
            botonBusqueda.grid(row=4, column=0, padx=5, pady=10)
            entryBusqueda.grid(row=3, column=0, padx=5, pady=10)
            entrada.grid(row=2, column=0, padx=5, pady=10)




        clicked_reservar_libro = StringVar()
        frame_listas_reserva_libro = Frame(FrameReservarLibro, width = 600, height= 650, borderwidth=5, padx=5, pady=5)
        frame_listas_reserva_libro.grid(row = 0, column=0, padx=20, pady=20, sticky="n")

        frame_lista = tk.Frame(frame_listas_reserva_libro, width=600)
        frame_lista.grid(row=0, column=0, sticky="w", pady = 5)
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
        for r in range(1, len(Servicio.getEjemplarLibroDisponibles())+1):
            nombre_libro = Servicio.getEjemplarLibroDisponibles()[r-1].getLibro().getNombre()
            nombre_autor = Servicio.getEjemplarLibroDisponibles()[r-1].getLibro().getAutor()
            nombre_genero = Servicio.getEjemplarLibroDisponibles()[r-1].getLibro().getGenero()

            frame_listaa = Frame(frame_listas_reserva_libro, width=600)
            frame_listaa.grid(row=r + 1, column=0, sticky="w")

            label_numeraal = Label(frame_listaa, text="{}. ".format(r), width=7, height=1, anchor="w", relief="groove")
            label_nombree = Label(frame_listaa, text=nombre_libro, width=20, height=1, anchor="w", relief="groove")
            label_autoor = Label(frame_listaa, text=nombre_autor, width=20, height=1, anchor="w", relief="groove")
            label_generoo = Label(frame_listaa, text=nombre_genero, width=20, height=1, anchor="w", relief="groove")

            label_numeraal.grid(row=0, column=0, sticky="w")
            label_nombree.grid(row=0, column=1, sticky="w")
            label_autoor.grid(row=0, column=2, sticky="w")
            label_generoo.grid(row=0, column=3, sticky="w")

        frame_filtro_reserva_libro = Frame(FrameReservarLibro, width= 400, height= 650, borderwidth=5, highlightthickness=3, highlightbackground="#61727C")
        frame_filtro_reserva_libro.grid(row = 0, column=1, padx=20, pady=20)

        labelFiltro_reserva_libro = Label(frame_filtro_reserva_libro, text = "Elija el tiempo de reserva", font=("verdana", 14), justify="center")
        drop_reserva_libro = OptionMenu(frame_filtro_reserva_libro, clicked_reservar_libro, *["5 dias","3 semanas","2 meses"], command=despliegue_reserva_libro)
        drop_reserva_libro.grid(row = 1, column= 0, padx=10, pady=10)
        labelFiltro_reserva_libro.grid(row=0, column=0 , padx=10, pady=10)

        VentanaUsuario.frames.append(FrameReservarLibro)





        FrameReservarRevista = Frame(self)

        def despliegue_reserva_revista(filtro):
            cantidad_tiempo = int(filtro.split(" ")[0])
            print(cantidad_tiempo)
            msg = "Escribe el numero de la revista\n que desea reservar"
            entrada = Label(frame_filtro_reserva_revista, text=msg, font=("verdana", 14), padx=10, pady=10)
            entryBusqueda = Entry(frame_filtro_reserva_revista, font=("verdana", 12))
            def HacerReservaRevista():
                indice = int(entryBusqueda.get())-1
                if indice > len(Servicio.getEjemplarRevistaDisponibles()) or indice < 0:
                    print("RAISEAR UN ERROR: no se encontró esa revista")
                else:
                    print(indice)
                    Ejemplar = Servicio.getEjemplarRevistaDisponibles()[indice]
                    entryBusqueda.delete(0, END)
                    fecha_inicial = datetime.now()
                    fecha_final = datetime.now()
                    if cantidad_tiempo == 5:
                        fecha_final += timedelta(days=5)

                    elif cantidad_tiempo == 3:
                        fecha_final += timedelta(weeks=3)

                    elif cantidad_tiempo == 2:
                        fecha_final += timedelta(weeks=8)

                    Reserva.generarReservaRevista(self._usuario, Ejemplar, self._biblioteca_main, fecha_final, fecha_inicial)
                    print(f"RESERVA EXITOSO {Ejemplar.getRevista().getNombre()} para el {fecha_inicial, fecha_final}")

            botonBusqueda = Button(frame_filtro_reserva_revista, text="Reservar", font=("verdana", 12),
                                   background="#61727C",
                                   fg="white", command=HacerReservaRevista)
            botonBusqueda.grid(row=4, column=0, padx=5, pady=10)
            entryBusqueda.grid(row=3, column=0, padx=5, pady=10)
            entrada.grid(row=2, column=0, padx=5, pady=10)

        clicked_reservar_revista = StringVar()
        frame_listas_reserva_revista = Frame(FrameReservarRevista, width = 600, height= 650, borderwidth=5, padx=5, pady=5)
        frame_listas_reserva_revista.grid(row = 0, column=0, padx=20, pady=20)

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
        frame_listas.grid_propagate(False)

        for r in range(1, len(Servicio.getEjemplarRevistaDisponibles())+1):
            nombre_revista = Servicio.getEjemplarRevistaDisponibles()[r-1].getRevista().getNombre()
            nombre_autor = Servicio.getEjemplarRevistaDisponibles()[r-1].getRevista().getAutor()
            nombre_categoria = Servicio.getEjemplarRevistaDisponibles()[r-1].getRevista().getCategoria()

            frame_listaR = Frame(frame_listas_reserva_revista, width=600)
            frame_listaR.grid(row=r + 1, column=0, sticky="w")

            label_numeraalR = Label(frame_listaR, text="{}. ".format(r), width=7, height=1, anchor="w", relief="groove")
            label_nombreeR = Label(frame_listaR, text=nombre_revista, width=20, height=1, anchor="w", relief="groove")
            label_autoorR = Label(frame_listaR, text=nombre_autor, width=20, height=1, anchor="w", relief="groove")
            label_generooR = Label(frame_listaR, text=nombre_categoria, width=20, height=1, anchor="w", relief="groove")

            label_numeraalR.grid(row=0, column=0, sticky="w")
            label_nombreeR.grid(row=0, column=1, sticky="w")
            label_autoorR.grid(row=0, column=2, sticky="w")
            label_generooR.grid(row=0, column=3, sticky="w")

        frame_filtro_reserva_revista = Frame(FrameReservarRevista, width= 400, height= 650, borderwidth=5, highlightthickness=3, highlightbackground="#61727C")
        frame_filtro_reserva_revista.grid(row = 0, column=1, padx=20, pady=20)

        labelFiltro_reserva_revista = Label(frame_filtro_reserva_revista, text = "Elija el tiempo de reserva", font=("verdana", 14), justify="center")
        drop_reserva_revista = OptionMenu(frame_filtro_reserva_revista, clicked_reservar_revista, *["5 dias","3 semanas","2 meses"], command=despliegue_reserva_revista)
        drop_reserva_revista.grid(row=1, column=0, padx=10, pady=10)
        labelFiltro_reserva_revista.grid(row=0, column=0, padx=10, pady=10)

        VentanaUsuario.frames.append(FrameReservarRevista)















        def informacion():
            ventana = Tk()
            ventana.geometry("640x360")
            ventana.resizable(True,True)
            ventana.title("JJ-Sales - Información de la Aplicación")

            texto = f"JJ Sales es una biblioteca en la que usted podrá \n" \
                    f"realizar préstamos y reservas de sus libros\n" \
                    f"favoritos sin tener que preocuparse por el \n" \
                    f"precio porque es gratis. Además le ofrecemos un sistema\n" \
                    f"de recomendaciones adecuadas a sus gustos para que se lleve la mejor experiencia posible"

            info = Label(ventana, text = texto, font = ("Helvetica", 11))
            info.pack(fill = tk.Y, expand = True)


        def Ayuda():
            ventanaAyuda = Tk()
            ventanaAyuda.geometry("640x360")
            ventanaAyuda.resizable(False, False)
            ventanaAyuda.title("JJ-Sales - Acerca de")

            textoAyuda = f"Desarrolladores:\n" \
                        f"• Esteban Espinosa Parra\n" \
                        f"• Juan Camilo Valencia\n" \
                        f"• Juan Pablo Diaz Cervantes\n" \
                        f"• Samuel Meza\n" \
                        f"• Alejandro Castro Parra"
            devs = Label(ventanaAyuda, text= textoAyuda, justify="left", font=("Helvetica", 12))
            devs.pack(fill=tk.Y, expand=True)




        def Guardar():
            serializarTodo()
            self.destroy()



        def cambiarFrame(frameUtilizado):
            for frame in VentanaUsuario.frames:
                frame.grid_forget()
            frameUtilizado.grid_configure()


