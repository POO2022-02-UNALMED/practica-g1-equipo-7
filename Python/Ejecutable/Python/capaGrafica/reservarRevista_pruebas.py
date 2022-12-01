from fieldFrame import FieldFrame
import tkinter as tk
lista_opciones = ["2 dias","2 semanas","1 mes"]





lista_mensajes = ["Juan","Carlos","Esteban","Erika","Ella"]


def despliegue(filtro):
    msg = "Escribe el numero de la Revista\n que desea reservas"
    entrada = tk.Label(frame_filtro, text=msg, font=("verdana", 14), padx = 10, pady = 10)
    entryBusqueda = tk.Entry(frame_filtro, font=("verdana", 12))
    botonBusqueda = tk.Button(frame_filtro, text="Reservar", font = ("verdana", 12),background="#61727C", fg= "white")
    
    botonBusqueda.grid(row=4, column=0, padx=5, pady=10) 
    entryBusqueda.grid(row = 3, column = 0, padx=5, pady=10)
    entrada.grid(row = 2, column = 0, padx=5, pady=10)

ventana_principal =tk. Tk()
ventana_principal.geometry("1080x720")
ventana_principal.title("Reservar Revista")
ventana_principal.resizable(False, False)
clicked = tk.StringVar()
frame_listas = tk.Frame(ventana_principal, width = 600, height= 650, borderwidth=5, bg = "grey", padx=5, pady=5, highlightbackground="black",
                     highlightthickness=2)
frame_listas.grid(row = 0, column=0, padx=20, pady=20)

frame_filtro = tk.Frame(ventana_principal, width= 400, height= 650, borderwidth=5, highlightthickness=3, highlightbackground="#61727C")
frame_filtro.grid(row = 0, column=1, padx=20, pady=20)


#Ventana de la derecha

labelFiltro = tk.Label(frame_filtro, text = "Elija el tiempo de reserva", font=("verdana", 14), justify="center")
drop = tk.OptionMenu(frame_filtro, clicked, *lista_opciones, command=despliegue)
drop.grid(row = 1, column= 0, padx=10, pady=10)
labelFiltro.grid(row=0, column=0 , padx=10, pady=10)



ventana_principal.mainloop()