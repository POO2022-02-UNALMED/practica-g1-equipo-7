from Python.capaGrafica.ventanaInicio import VentanaInicio
from Python.capaGrafica.ventanaUsuario import VentanaUsuario
from Python.baseDatos.deserializador import deserializarTodo
from Python.gestorAplicacion.libreria.biblioteca import Biblioteca

deserializarTodo()

ventana = VentanaInicio()

ventana.mainloop()



