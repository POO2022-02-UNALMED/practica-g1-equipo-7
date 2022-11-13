import os
import pathlib
from random import randint
from tkinter import *
import tkinter

from Python.capaGrafica.fieldFrame import FieldFrame

class VentanaUsuario(Tk):

    frames = []

    def __init__(self, biblioteca):
        super().__init__()

        self.title("JJ-Sales - Ventana del Usuario")
        self.geometry("1080x720")
        self.option_add("*tearOff", False)
        self.resizable(True,True)

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
        info_biblioteca.add_command(label = "Buscar libro" , command = lambda: cambiarFrame(Frame()))
        info_biblioteca.add_command(label = "Buscar revista" , command = lambda: cambiarFrame(Frame()))
        info_biblioteca.add_command(label = "Mis prestamos" , command = lambda: cambiarFrame(Frame()))
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
        realizar_prestamo.add_command(label="Prestar libro", command=lambda: cambiarFrame(Frame()))
        realizar_prestamo.add_command(label="Prestar revista", command=lambda: cambiarFrame(Frame()))
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
            info.pack(fill = tkinter.Y, expand = True)


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
            devs.pack(fill=tkinter.Y, expand=True)


        def Guardar():
            #aca se serializa
            self.destroy()

        def cambiarFrame(frameUtilizado):
            for frame in VentanaUsuario.frames:
                frame.pack_forget()
            frameUtilizado.pack(fill=BOTH,expand=True, pady = (10,10))

nuevo = VentanaUsuario([])
nuevo.mainloop()