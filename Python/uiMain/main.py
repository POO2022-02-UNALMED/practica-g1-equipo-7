from Python.capaGrafica.ventanaInicio import VentanaInicio
from Python.capaGrafica.ventanaUsuario import VentanaUsuario
#from Python.baseDatos.deserializador import deserializarTodo
from Python.gestorAplicacion.libreria.biblioteca import Biblioteca
from Python.gestorAplicacion.servicios.servicio import Servicio
from Python.gestorAplicacion.servicios.usuario import Usuario


#deserializarTodo()
biblioteca_main = Biblioteca()
#usuario = Usuario("Juan", 238283, [],[],[],[],[],[])
usuario = Biblioteca.getUsuarios()[0]

Servicio.setEjemplarLibroDisponibles(biblioteca_main.getEjemplaresLibros())
Servicio.setEjemplarRevistaDisponibles(biblioteca_main.getEjemplaresRevistas())

#ventana = VentanaUsuario(biblioteca_main, usuario)
ventana = VentanaInicio(biblioteca_main, usuario)
ventana.mainloop()



