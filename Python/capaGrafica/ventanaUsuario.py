
from tkinter import *
import tkinter as tk
from Python.baseDatos.serializador import serializarTodo

from Python.gestorAplicacion.servicios.prestamo import Prestamo
from Python.gestorAplicacion.libreria.libro import Libro
from Python.gestorAplicacion.servicios.servicio import Servicio
from Python.gestorAplicacion.libreria.revista import Revista





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
        info_biblioteca.add_command(label="Mis reservas", command=lambda: cambiarFrame(Frame()))

        procesos_consultas.add_cascade(label = "Consultas", menu = info_biblioteca)


        #FUNCIONALIDADES
        #1. Reservas
        realizar_reserva = Menu(self._barra_del_menu)
        realizar_reserva.add_command(label="Reservar libro", command=lambda: cambiarFrame(Frame()))
        realizar_reserva.add_command(label="Reservar revista", command=lambda: cambiarFrame(Frame()))
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
                entryBusqueda.delete(0, END)
                filtro = clicked.get().lower()
                print(filtro)
                print(string_Campo)
                cantidad = 0
                if filtro == "autor":
                    for libro in Servicio.getEjemplarLibroDisponibles():
                        if string_Campo in libro.getLibro().getAutor().lower():
                            cantidad += 1
                            nombre_libro = libro.getLibro().getNombre()
                            nombre_autor = libro.getLibro().getAutor()
                            nombre_genero = libro.getLibro().getGenero()
                            #IMPLEMENTAR LO DE LISTAS ACÁ


                elif filtro == "nombre":
                    for libro in Servicio.getEjemplarLibroDisponibles():
                        if string_Campo in libro.getLibro().getNombre().lower():
                            cantidad += 1
                            nombre_libro = libro.getLibro().getNombre()
                            nombre_autor = libro.getLibro().getAutor()
                            nombre_genero = libro.getLibro().getGenero()
                            #IMPLEMENTAR LO DE LISTAS ACÁ

                elif filtro == "genero":
                    for libro in Servicio.getEjemplarLibroDisponibles():
                        if string_Campo in libro.getLibro().getGenero().lower():
                            cantidad += 1
                            nombre_libro = libro.getLibro().getNombre()
                            nombre_autor = libro.getLibro().getAutor()
                            nombre_genero = libro.getLibro().getGenero()
                            #IMPLEMENTAR LO DE LISTAS ACÁ

                if cantidad == 0:
                    print(
                        "EXCEPTION: NO SE ENCONTRARON RESULTADOS (esto iría en una ventana pequeña que se pueda cerrar y ya")

            botonBusqueda = Button(frame_filtro, text="Buscar", font=("verdana", 12), background="#61727C",
                                      fg="white", command=Filtrar)
            botonBusqueda.grid(row=4, column=0, padx=10, pady=10)
            entryBusqueda.grid(row=3, column=0, padx=10, pady=10)
            entrada.grid(row=2, column=0, padx=10, pady=10)

        clicked = StringVar()
        frame_listas = Frame(FrameBuscarLibro, width = 600, height= 650, borderwidth=5, bg = "grey", padx=5, pady=5, highlightbackground="black",
                     highlightthickness=2)
        frame_listas.grid(row=0, column=0, padx=20, pady=20)

        frame_filtro = Frame(FrameBuscarLibro, width= 400, height= 650, borderwidth=5, highlightthickness=3, highlightbackground="#61727C")
        frame_filtro.grid(row = 0, column=1, padx=20, pady=20)

        #Ventana de la derecha
        labelFiltro = Label(frame_filtro, text="Filtro deseado", font=("verdana", 14), justify="center")
        drop = tk.OptionMenu(frame_filtro, clicked, *["Nombre","Autor","Genero"], command=despliegue)
        drop.grid(row=1, column=0, padx=10, pady=10)
        labelFiltro.grid(row=0, column=0, padx=10, pady=10)
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
                entryBusqueda.delete(0, END)
                filtro = clicked_revista.get().lower()
                print(filtro)
                print(string_Campo)
                cantidad = 0
                if filtro == "autor":
                    for revista in Servicio.getEjemplarRevistaDisponibles():
                        if string_Campo in revista.getRevista().getAutor().lower():
                            cantidad +=1
                            nombre_revista = revista.getRevista().getNombre()
                            nombre_autor = revista.getRevista().getAutor()
                            nombre_categoria = revista.getRevista().getCategoria()
                            # IMPLEMENTAR LO DE LISTAS ACÁ


                elif filtro == "nombre":
                    for revista in Servicio.getEjemplarRevistaDisponibles():
                        if string_Campo in revista.getRevista().getNombre().lower():
                            cantidad += 1
                            nombre_revista = revista.getRevista().getNombre()
                            nombre_autor = revista.getRevista().getAutor()
                            nombre_categoria = revista.getRevista().getCategoria()
                            # IMPLEMENTAR LO DE LISTAS ACÁ

                elif filtro == "categoria":
                    for revista in Servicio.getEjemplarRevistaDisponibles():
                        if string_Campo in revista.getRevista().getCategoria().lower():
                            cantidad += 1
                            nombre_revista = revista.getRevista().getNombre()
                            nombre_autor = revista.getRevista().getAutor()
                            nombre_categoria = revista.getRevista().getCategoria()
                            # IMPLEMENTAR LO DE LISTAS ACÁ

                if cantidad == 0:
                    print("EXCEPTION: NO SE ENCONTRARON RESULTADOS (esto iría en una ventana pequeña que se pueda cerrar y ya")


            botonBusqueda = Button(frame_filtro_revista, text="Buscar", font=("verdana", 12), background="#61727C",
                                      fg="white", command=Filtrar)
            botonBusqueda.grid(row=4, column=0, padx=10, pady=10)
            entryBusqueda.grid(row=3, column=0, padx=10, pady=10)
            entrada.grid(row=2, column=0, padx=10, pady=10)

        clicked_revista = StringVar()
        frame_listas_revista = Frame(FrameBuscarRevista, width = 600, height= 650, borderwidth=5, bg = "grey", padx=5, pady=5, highlightbackground="black",
                     highlightthickness=2)
        frame_listas_revista.grid(row=0, column=0, padx=20, pady=20)

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
            for prestamo in lista_prestamos:
                ejemplar = prestamo.getEjemplarEscogido().getLibro()
                if isinstance(ejemplar, Libro):
                    print("hola")
                    nombre_libro = ejemplar.getNombre()
                    nombre_autor = ejemplar.getAutor()
                    nombre_genero = ejemplar.getGenero()
                    # IMPLEMENTAR LO DE LISTAS ACÁ


                elif isinstance(ejemplar, Revista):
                    print("hola")
                    nombre_revista = ejemplar.getNombre()
                    nombre_autor = ejemplar.getAutor()
                    nombre_categoria = ejemplar.getCategoria()
                    # IMPLEMENTAR LO DE LISTAS ACÁ


        frame_revistas = tk.Frame(FrameMisPrestamos, width=520, height=570, borderwidth=5, highlightthickness=3,
                                  highlightbackground="#61727C")
        frame_revistas.grid(row=1, column=1, padx=10, pady=10)
        boton_actualizar = Button(frame_revistas, width=30, height= 40, text = "Actualizar", command=ActualizarPrestamos)
        boton_actualizar.grid(row = 0, column=0)


        letrero = tk.Label(frame_letrero, text="Mis prestamos", font=("verdana", 16, "bold"), fg="white", borderwidth=3,
                           background="#61727C", width=20, height=2)
        letrero.grid(row=0, column=0)

        letrero_libros = tk.Label(frame_libros, text="Libros", font=("verdana", 14, "bold"), fg="white", borderwidth=3,
                                  background="#61727C", width=10, height=2)
        letrero_libros.grid(row=0, column=0)
        frame_libros.grid_propagate(False)
        letrero_revista = tk.Label(frame_revistas, text="Revistas", font=("verdana", 14, "bold"), fg="white",
                                   borderwidth=3, background="#61727C", width=10, height=2)
        letrero_revista.grid(row=0, column=0, padx=5, pady=5)
        frame_revistas.grid_propagate(False)




        VentanaUsuario.frames.append(FrameMisPrestamos)
















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


