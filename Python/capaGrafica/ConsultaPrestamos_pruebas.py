from fieldFrame import FieldFrame
import tkinter as tk

ventana_principal =tk. Tk()
ventana_principal.geometry("1080x720")
ventana_principal.title("Mis prestamos")
ventana_principal.resizable(False, False)
#ventana_principal.config(background="#61727C")

#Contenedores principales
frame_letrero = tk.Frame(ventana_principal, width=1060, height=100, borderwidth=5, highlightthickness=3, highlightbackground="#61727C")
frame_letrero.grid(row = 0, column=0, columnspan=2, padx=10, pady=10)

frame_libros = tk.Frame(ventana_principal, width = 520, height= 570, borderwidth=5, highlightbackground="#61727C", highlightthickness=3)
frame_libros.grid(row = 1, column=0, padx=10, pady=10)

frame_revistas = tk.Frame(ventana_principal, width= 520, height= 570, borderwidth=5, highlightthickness=3, highlightbackground="#61727C")
frame_revistas.grid(row = 1, column=1, padx=10, pady=10)

#Letrero
letrero = tk.Label(frame_letrero, text="Mis prestamos", font=("verdana", 16, "bold"), fg="white",borderwidth=3, background="#61727C", width=20, height=2)
letrero.grid(row=0, column=0)

#Evitar que el grid cambie de tamaño

#frame libros
letrero_libros = tk.Label(frame_libros, text="Libros", font=("verdana", 14, "bold"), fg="white",borderwidth=3, background="#61727C", width=10, height=2)
letrero_libros.grid(row=0, column = 0)

#Evitar que el grid cambie de tamaño
frame_libros.grid_propagate(False)

#frame revista
letrero_revista = tk.Label(frame_revistas, text="Revistas", font=("verdana", 14, "bold"), fg="white",borderwidth=3, background="#61727C", width=10, height=2)
letrero_revista.grid(row=0, column = 0, padx=5, pady=5)

#Evitar que el grid cambie de tamaño
frame_revistas.grid_propagate(False)
ventana_principal.mainloop()