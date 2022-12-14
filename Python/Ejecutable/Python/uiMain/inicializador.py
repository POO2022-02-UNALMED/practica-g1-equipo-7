from Python.gestorAplicacion.libreria.libro import Libro
from Python.gestorAplicacion.libreria.revista import Revista
from Python.gestorAplicacion.libreria.genero import GENERO
from Python.gestorAplicacion.libreria.categoria import CATEGORIA
from Python.gestorAplicacion.libreria.ejemplarLibro import EjemplarLibro
from Python.gestorAplicacion.libreria.ejemplarRevista import EjemplarRevista
from Python.gestorAplicacion.libreria.estadoEjemplar import EstadoEjemplar
from Python.gestorAplicacion.servicios.usuario import Usuario
from datetime import datetime


from Python.gestorAplicacion.servicios.prestamo import Prestamo
from Python.gestorAplicacion.servicios.reserva import Reserva
from Python.gestorAplicacion.libreria.biblioteca import Biblioteca
from Python.gestorAplicacion.servicios.servicio import Servicio
from Python.baseDatos.serializador import serializarTodo


libro_soledad = Libro("100 anios de soledad", "Gabriel Garcia Marquez", 373512323, GENERO.FANTASIA.value)
libro_noches = Libro("Las mil y una noches", "Varios autores", 391212871, GENERO.CUENTO.value)
guerra_y_paz = Libro("Guerra y paz", "Leon Tolstoi", 391212291, GENERO.HISTORICA.value)
orgullo = Libro("Orgullo y prejuicio", "Jane Austen", 391219123, GENERO.NOVELA.value)
extranjero = Libro("Extranjero", "Albert Camus", 221212871, GENERO.FILOSOFIA.value)
esperanzas = Libro("Grandes esperanzas", "Charles Dickens", 981212871, GENERO.NOVELA.value)
el_hombre = Libro("El hombre sin atributos", "Robert Musil", 398712871, GENERO.NOVELA.value)

preludio = Libro("Preludio a la fundacion", "Isaac Asimov", 398712822, GENERO.CUENTO.value)
la_muerte = Libro("La muerte de Artemio Cruz", "Carlos Fuentes", 398712000, GENERO.FANTASIA.value)
la_condicion = Libro("Cumbres borrascosas", "Emily Bronte", 398719876, GENERO.FANTASIA.value)
quevedo = Libro("El buscon", "Francisco de Quevedo", 123712871, GENERO.CUENTO.value)
rojo = Libro("Rojo y negro", "Stendhal", 398755555, GENERO.FILOSOFIA.value)
ensayo = Libro("Ensayo sobre la ceguera", "Jose Saramago", 387612871, GENERO.FILOSOFIA.value)
la_colmena = Libro("La colmena", "Camilo Jose Cela", 391002871, GENERO.HISTORICA.value)

guerra_mundial = Libro("Segunda Guerra Mundial", "Marta Diaz", 399991271, GENERO.HISTORICA.value)
verdad = Libro("Yo, Claudio", "Robert Graves", 398712000, GENERO.CUENTO.value)

interestellar = Libro("Interestellar", "Marco Alonso", 398712981, GENERO.CIENCIA.value)
hombre_luna = Libro("Arrivo lunar", "George Maquintosh", 398712761, GENERO.CIENCIA.value)
wether = Libro("Las cuitas del Joven Werther", "Goethe", 876512761, GENERO.ROMANTICISMO.value)
la_caceria = Libro("Las historias de la evolucion", "Daniel Hil", 298712761, GENERO.CIENCIA.value)
elamor = Libro("Una historia de amor", "Liliana Escalar", 111712761, GENERO.ROMANTICISMO.value)
ruptura = Libro("El desapego", "Walter Riso", 398701761, GENERO.ROMANTICISMO.value)

revista_viernes = Revista("Viernes", "El Universal", 323823999, CATEGORIA.ENTRETENIMIENTO.value)
revista_semana = Revista("Semana", "Semana", 278388654, CATEGORIA.ENTRETENIMIENTO.value)
revista_3 = Revista(CATEGORIA.ACTUALIDAD.value)
revista_4 = Revista()
revista_5 = Revista(CATEGORIA.POLITICA.value)
revista_6 = Revista("El Hoy", "Disney", 398700761, CATEGORIA.POLITICA.value)
revista_7 = Revista("Q'Hubo", "Exito", 100712761, CATEGORIA.ACTUALIDAD.value)
revista_8 = Revista("La Pila", "Zona Studios", 398712091, CATEGORIA.ACTUALIDAD.value)
revista_9 = Revista("El manana", "Walter White", 901712761, CATEGORIA.ACTUALIDAD.value)
revista_10 = Revista("La calle", "Street", 675512761, CATEGORIA.POLITICA.value)

EjLibro1 = EjemplarLibro(29392, EstadoEjemplar(False, False, False, None, None), libro_soledad)
EjLibro2 = EjemplarLibro(29299, EstadoEjemplar(False, False, False, None, None), libro_noches)
EjLibro3 = EjemplarLibro(21299, EstadoEjemplar(False, False, False, None, None), libro_noches)
EjLibro4 = EjemplarLibro(28765, EstadoEjemplar(False, False, False, None, None), libro_soledad)
EjLibro5 = EjemplarLibro(20000, EstadoEjemplar(False, False, False, None, None), guerra_y_paz)
EjLibro6 = EjemplarLibro(22341, EstadoEjemplar(False, False, False, None, None), guerra_y_paz)
EjLibro7 = EjemplarLibro(12381, EstadoEjemplar(False, False, False, None, None), orgullo)
EjLibro8 = EjemplarLibro(98231, EstadoEjemplar(False, False, False, None, None), orgullo)
EjLibro9 = EjemplarLibro(90000, EstadoEjemplar(False, False, False, None, None), extranjero)
EjLibro10 = EjemplarLibro(98231, EstadoEjemplar(False, False, False, None, None), extranjero)
EjLibro11 = EjemplarLibro(98231, EstadoEjemplar(False, False, False, None, None), extranjero)
EjLibro12 = EjemplarLibro(98231, EstadoEjemplar(False, False, False, None, None), esperanzas)
EjLibro13 = EjemplarLibro(98221, EstadoEjemplar(False, False, False, None, None), esperanzas)
EjLibro14 = EjemplarLibro(11152, EstadoEjemplar(False, False, False, None, None), esperanzas)
EjLibro15 = EjemplarLibro(20191, EstadoEjemplar(False, False, False, None, None), el_hombre)
EjLibro16 = EjemplarLibro(29371, EstadoEjemplar(False, False, False, None, None), el_hombre)

EjLibro17 = EjemplarLibro(29111, EstadoEjemplar(False, False, False, None, None), preludio)
EjLibro18 = EjemplarLibro(29101, EstadoEjemplar(False, False, False, None, None), la_muerte)
EjLibro19 = EjemplarLibro(39111, EstadoEjemplar(False, False, False, None, None), la_condicion)
EjLibro20 = EjemplarLibro(49111, EstadoEjemplar(False, False, False, None, None), quevedo)
EjLibro21 = EjemplarLibro(59111, EstadoEjemplar(False, False, False, None, None), rojo)
EjLibro22 = EjemplarLibro(69311, EstadoEjemplar(False, False, False, None, None), ensayo)
EjLibro23 = EjemplarLibro(29411, EstadoEjemplar(False, False, False, None, None), la_colmena)
EjLibro24 = EjemplarLibro(29541, EstadoEjemplar(False, False, False, None, None), guerra_mundial)
EjLibro25 = EjemplarLibro(29651, EstadoEjemplar(False, False, False, None, None), verdad)
EjLibro26 = EjemplarLibro(29761, EstadoEjemplar(False, False, False, None, None), interestellar)
EjLibro27 = EjemplarLibro(19471, EstadoEjemplar(False, False, False, None, None), hombre_luna)
EjLibro28 = EjemplarLibro(19181, EstadoEjemplar(False, False, False, None, None), wether)
EjLibro29 = EjemplarLibro(39191, EstadoEjemplar(False, False, False, None, None), la_caceria)
EjLibro30 = EjemplarLibro(49112, EstadoEjemplar(False, False, False, None, None), elamor)
EjLibro31 = EjemplarLibro(59113, EstadoEjemplar(False, False, False, None, None), ruptura)

ejRev1 = EjemplarRevista(23812, EstadoEjemplar(False, False, False, None, None), revista_4)
ejRev2 = EjemplarRevista(11111, EstadoEjemplar(False, False, False, None, None), revista_viernes)
ejRev3 = EjemplarRevista(23411, EstadoEjemplar(False, False, False, None, None), revista_semana)
ejRev4 = EjemplarRevista(12313, EstadoEjemplar(False, False, False, None, None), revista_viernes)
ejRev5 = EjemplarRevista(43561, EstadoEjemplar(False, False, False, None, None), revista_3)
ejRev6 = EjemplarRevista(32456, EstadoEjemplar(False, False, False, None, None), revista_semana)
ejRev7 = EjemplarRevista(56611, EstadoEjemplar(False, False, False, None, None), revista_viernes)
ejRev8 = EjemplarRevista(65467, EstadoEjemplar(False, False, False, None, None), revista_3)
ejRev9 = EjemplarRevista(51231, EstadoEjemplar(False, False, False, None, None), revista_semana)
ejRev10 = EjemplarRevista(54768, EstadoEjemplar(False, False, False, None, None), revista_viernes)
ejRev11 = EjemplarRevista(25674, EstadoEjemplar(False, False, False, None, None), revista_4)
ejRev12 = EjemplarRevista(43677, EstadoEjemplar(False, False, False, None, None), revista_3)
ejRev13 = EjemplarRevista(23455, EstadoEjemplar(False, False, False, None, None), revista_3)
ejRev14 = EjemplarRevista(19600, EstadoEjemplar(False, False, False, None, None), revista_4)
ejRev15 = EjemplarRevista(11133, EstadoEjemplar(False, False, False, None, None), revista_4)
ejRev16 = EjemplarRevista(44551, EstadoEjemplar(False, False, False, None, None), revista_4)
ejRev17 = EjemplarRevista(23455, EstadoEjemplar(False, False, False, None, None), revista_5)
ejRev18 = EjemplarRevista(24354, EstadoEjemplar(False, False, False, None, None), revista_6)
ejRev19 = EjemplarRevista(24354, EstadoEjemplar(False, False, False, None, None), revista_7)
ejRev20 = EjemplarRevista(24354, EstadoEjemplar(False, False, False, None, None), revista_8)
ejRev21 = EjemplarRevista(24354, EstadoEjemplar(False, False, False, None, None), revista_9)
ejRev22 = EjemplarRevista(24354, EstadoEjemplar(False, False, False, None, None), revista_10)
ejRev23 = EjemplarRevista(24354, EstadoEjemplar(False, False, False, None, None), revista_10)

usuario1 = Usuario("Erika", 1823, [], [], [], [], [])
usuario2 = Usuario("Esteban", 2823, [], [], [], [], [])
usuario3 = Usuario("Daniel", 1423, [], [], [], [], [])
usuario4 = Usuario("Juan Enrique", 1123, [], [], [], [], [])
usuario5 = Usuario("David", 1234, [], [], [], [], [])
usuario6 = Usuario("Juan Pablo", 2391, [], [], [], [], [])
usuario7 = Usuario("Juan Sebastian", 1301, [], [], [], [], [])


def inicializar(biblioteca):
    biblioteca.a??adirLibro(libro_soledad)
    biblioteca.a??adirLibro(libro_noches)
    biblioteca.a??adirLibro(guerra_y_paz)
    biblioteca.a??adirLibro(orgullo)
    biblioteca.a??adirLibro(extranjero)
    biblioteca.a??adirLibro(el_hombre)
    biblioteca.a??adirLibro(preludio)
    biblioteca.a??adirLibro(la_muerte)
    biblioteca.a??adirLibro(la_condicion)
    biblioteca.a??adirLibro(quevedo)
    biblioteca.a??adirLibro(rojo)
    biblioteca.a??adirLibro(ensayo)
    biblioteca.a??adirLibro(la_colmena)
    biblioteca.a??adirLibro(guerra_mundial)
    biblioteca.a??adirLibro(verdad)
    biblioteca.a??adirLibro(interestellar)
    biblioteca.a??adirLibro(hombre_luna)
    biblioteca.a??adirLibro(wether)
    biblioteca.a??adirLibro(la_caceria)
    biblioteca.a??adirLibro(elamor)
    biblioteca.a??adirLibro(ruptura)

    biblioteca.a??adirRevista(revista_viernes)
    biblioteca.a??adirRevista(revista_semana)
    biblioteca.a??adirRevista(revista_3)
    biblioteca.a??adirRevista(revista_4)
    biblioteca.a??adirRevista(revista_5)
    biblioteca.a??adirRevista(revista_6)
    biblioteca.a??adirRevista(revista_7)
    biblioteca.a??adirRevista(revista_8)
    biblioteca.a??adirRevista(revista_9)
    biblioteca.a??adirRevista(revista_10)

    biblioteca.a??adirEjemplarLibro(EjLibro1)
    biblioteca.a??adirEjemplarLibro(EjLibro2)
    biblioteca.a??adirEjemplarLibro(EjLibro3)
    biblioteca.a??adirEjemplarLibro(EjLibro4)
    biblioteca.a??adirEjemplarLibro(EjLibro5)
    biblioteca.a??adirEjemplarLibro(EjLibro6)
    biblioteca.a??adirEjemplarLibro(EjLibro7)
    biblioteca.a??adirEjemplarLibro(EjLibro8)
    biblioteca.a??adirEjemplarLibro(EjLibro9)
    biblioteca.a??adirEjemplarLibro(EjLibro10)
    biblioteca.a??adirEjemplarLibro(EjLibro11)
    biblioteca.a??adirEjemplarLibro(EjLibro12)
    biblioteca.a??adirEjemplarLibro(EjLibro13)
    biblioteca.a??adirEjemplarLibro(EjLibro14)
    biblioteca.a??adirEjemplarLibro(EjLibro15)
    biblioteca.a??adirEjemplarLibro(EjLibro16)
    biblioteca.a??adirEjemplarLibro(EjLibro17)
    biblioteca.a??adirEjemplarLibro(EjLibro18)
    biblioteca.a??adirEjemplarLibro(EjLibro19)
    biblioteca.a??adirEjemplarLibro(EjLibro20)
    biblioteca.a??adirEjemplarLibro(EjLibro21)
    biblioteca.a??adirEjemplarLibro(EjLibro22)
    biblioteca.a??adirEjemplarLibro(EjLibro23)
    biblioteca.a??adirEjemplarLibro(EjLibro24)
    biblioteca.a??adirEjemplarLibro(EjLibro25)
    biblioteca.a??adirEjemplarLibro(EjLibro26)
    biblioteca.a??adirEjemplarLibro(EjLibro27)
    biblioteca.a??adirEjemplarLibro(EjLibro28)
    biblioteca.a??adirEjemplarLibro(EjLibro29)
    biblioteca.a??adirEjemplarLibro(EjLibro30)
    biblioteca.a??adirEjemplarLibro(EjLibro31)

    biblioteca.a??adirEjemplarRevista(ejRev1)
    biblioteca.a??adirEjemplarRevista(ejRev2)
    biblioteca.a??adirEjemplarRevista(ejRev3)
    biblioteca.a??adirEjemplarRevista(ejRev4)
    biblioteca.a??adirEjemplarRevista(ejRev5)
    biblioteca.a??adirEjemplarRevista(ejRev6)
    biblioteca.a??adirEjemplarRevista(ejRev7)
    biblioteca.a??adirEjemplarRevista(ejRev8)
    biblioteca.a??adirEjemplarRevista(ejRev9)
    biblioteca.a??adirEjemplarRevista(ejRev10)
    biblioteca.a??adirEjemplarRevista(ejRev11)
    biblioteca.a??adirEjemplarRevista(ejRev12)
    biblioteca.a??adirEjemplarRevista(ejRev13)
    biblioteca.a??adirEjemplarRevista(ejRev14)
    biblioteca.a??adirEjemplarRevista(ejRev15)
    biblioteca.a??adirEjemplarRevista(ejRev16)
    biblioteca.a??adirEjemplarRevista(ejRev17)
    biblioteca.a??adirEjemplarRevista(ejRev18)
    biblioteca.a??adirEjemplarRevista(ejRev19)
    biblioteca.a??adirEjemplarRevista(ejRev20)
    biblioteca.a??adirEjemplarRevista(ejRev21)
    biblioteca.a??adirEjemplarRevista(ejRev22)
    biblioteca.a??adirEjemplarRevista(ejRev23)

    # Usuario1
    Servicio.setEjemplarLibroDisponibles(
        [EjLibro1, EjLibro2, EjLibro3, EjLibro4, EjLibro5, EjLibro6, EjLibro7, EjLibro8, EjLibro9, EjLibro10, EjLibro11,
         EjLibro12, EjLibro13, EjLibro14, EjLibro15, EjLibro16, EjLibro17, EjLibro18, EjLibro19, EjLibro20, EjLibro21,
         EjLibro22, EjLibro23, EjLibro24, EjLibro25, EjLibro26, EjLibro27, EjLibro28, EjLibro29, EjLibro30,
         EjLibro31])

    Servicio.setEjemplarRevistaDisponibles([ejRev1, ejRev2, ejRev3, ejRev4, ejRev5, ejRev6, ejRev7, ejRev8, ejRev9,
                                            ejRev10, ejRev11, ejRev12, ejRev13, ejRev14, ejRev15, ejRev16, ejRev17,
                                            ejRev18, ejRev19, ejRev20, ejRev21, ejRev22, ejRev23])

    Prestamo.generarPrestamoLibro(usuario1, EjLibro1, biblioteca)
    Prestamo.generarPrestamoLibro(usuario1, EjLibro2, biblioteca)
    Prestamo.generarPrestamoLibro(usuario1, EjLibro3, biblioteca)
    Prestamo.generarPrestamoLibro(usuario1, EjLibro4, biblioteca)
    Prestamo.generarPrestamoLibro(usuario1, EjLibro5, biblioteca)
    Prestamo.generarPrestamoLibro(usuario1, EjLibro6, biblioteca)
    Prestamo.generarPrestamoLibro(usuario1, EjLibro7, biblioteca)
    Prestamo.generarPrestamoLibro(usuario1, EjLibro8, biblioteca)
    Prestamo.generarPrestamoLibro(usuario1, EjLibro9, biblioteca)
    Prestamo.generarPrestamoLibro(usuario1, EjLibro10, biblioteca)
    Prestamo.generarPrestamoLibro(usuario1, EjLibro11, biblioteca)
    Prestamo.generarPrestamoLibro(usuario1, EjLibro12, biblioteca)

    Reserva.generarReservaRevista(usuario1, ejRev1, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario1, ejRev2, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario1, ejRev3, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario1, ejRev4, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario1, ejRev5, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario1, ejRev6, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario1, ejRev7, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario1, ejRev8, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario1, ejRev9, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario1, ejRev10, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))

    Prestamo.devolucion(0, biblioteca, usuario1)
    Prestamo.devolucion(0, biblioteca, usuario1)
    Prestamo.devolucion(0, biblioteca, usuario1)
    Prestamo.devolucion(0, biblioteca, usuario1)
    Prestamo.devolucion(0, biblioteca, usuario1)
    Prestamo.devolucion(0, biblioteca, usuario1)
    Prestamo.devolucion(0, biblioteca, usuario1)
    Prestamo.devolucion(0, biblioteca, usuario1)
    Prestamo.devolucion(0, biblioteca, usuario1)
    Prestamo.devolucion(0, biblioteca, usuario1)
    Prestamo.devolucion(0, biblioteca, usuario1)
    Prestamo.devolucion(0, biblioteca, usuario1)
    Reserva.cancelarReserva(0, biblioteca, usuario1)
    Reserva.cancelarReserva(0, biblioteca, usuario1)
    Reserva.cancelarReserva(0, biblioteca, usuario1)
    Reserva.cancelarReserva(0, biblioteca, usuario1)
    Reserva.cancelarReserva(0, biblioteca, usuario1)
    Reserva.cancelarReserva(0, biblioteca, usuario1)
    Reserva.cancelarReserva(0, biblioteca, usuario1)
    Reserva.cancelarReserva(0, biblioteca, usuario1)
    Reserva.cancelarReserva(0, biblioteca, usuario1)
    Reserva.cancelarReserva(0, biblioteca, usuario1)

    # Usuario2

    Prestamo.generarPrestamoLibro(usuario2, EjLibro1, biblioteca)
    Prestamo.generarPrestamoLibro(usuario2, EjLibro2, biblioteca)
    Prestamo.generarPrestamoLibro(usuario2, EjLibro3, biblioteca)
    Prestamo.generarPrestamoLibro(usuario2, EjLibro4, biblioteca)
    Prestamo.generarPrestamoLibro(usuario2, EjLibro5, biblioteca)
    Prestamo.generarPrestamoLibro(usuario2, EjLibro6, biblioteca)
    Prestamo.generarPrestamoLibro(usuario2, EjLibro7, biblioteca)
    Prestamo.generarPrestamoLibro(usuario2, EjLibro8, biblioteca)
    Prestamo.generarPrestamoLibro(usuario2, EjLibro9, biblioteca)
    Prestamo.generarPrestamoLibro(usuario2, EjLibro10, biblioteca)
    Prestamo.generarPrestamoLibro(usuario2, EjLibro11, biblioteca)
    Prestamo.generarPrestamoLibro(usuario2, EjLibro12, biblioteca)

    Reserva.generarReservaRevista(usuario2, ejRev1, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario2, ejRev2, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario2, ejRev3, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario2, ejRev4, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario2, ejRev5, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario2, ejRev6, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario2, ejRev7, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario2, ejRev8, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario2, ejRev9, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario2, ejRev10, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))

    Prestamo.devolucion(0, biblioteca, usuario2)
    Prestamo.devolucion(0, biblioteca, usuario2)
    Prestamo.devolucion(0, biblioteca, usuario2)
    Prestamo.devolucion(0, biblioteca, usuario2)
    Prestamo.devolucion(0, biblioteca, usuario2)
    Prestamo.devolucion(0, biblioteca, usuario2)
    Prestamo.devolucion(0, biblioteca, usuario2)
    Prestamo.devolucion(0, biblioteca, usuario2)
    Prestamo.devolucion(0, biblioteca, usuario2)
    Prestamo.devolucion(0, biblioteca, usuario2)
    Prestamo.devolucion(0, biblioteca, usuario2)
    Prestamo.devolucion(0, biblioteca, usuario2)
    Reserva.cancelarReserva(0, biblioteca, usuario2)
    Reserva.cancelarReserva(0, biblioteca, usuario2)
    Reserva.cancelarReserva(0, biblioteca, usuario2)
    Reserva.cancelarReserva(0, biblioteca, usuario2)
    Reserva.cancelarReserva(0, biblioteca, usuario2)
    Reserva.cancelarReserva(0, biblioteca, usuario2)
    Reserva.cancelarReserva(0, biblioteca, usuario2)
    Reserva.cancelarReserva(0, biblioteca, usuario2)
    Reserva.cancelarReserva(0, biblioteca, usuario2)
    Reserva.cancelarReserva(0, biblioteca, usuario2)

    # usuario 3

    Prestamo.generarPrestamoLibro(usuario3, EjLibro1, biblioteca)
    Prestamo.generarPrestamoLibro(usuario3, EjLibro2, biblioteca)
    Prestamo.generarPrestamoLibro(usuario3, EjLibro3, biblioteca)
    Prestamo.generarPrestamoLibro(usuario3, EjLibro4, biblioteca)
    Prestamo.generarPrestamoLibro(usuario3, EjLibro5, biblioteca)
    Prestamo.generarPrestamoLibro(usuario3, EjLibro6, biblioteca)
    Prestamo.generarPrestamoLibro(usuario3, EjLibro7, biblioteca)
    Prestamo.generarPrestamoLibro(usuario3, EjLibro8, biblioteca)
    Prestamo.generarPrestamoLibro(usuario3, EjLibro9, biblioteca)
    Prestamo.generarPrestamoLibro(usuario3, EjLibro10, biblioteca)
    Prestamo.generarPrestamoLibro(usuario3, EjLibro11, biblioteca)
    Prestamo.generarPrestamoLibro(usuario3, EjLibro12, biblioteca)

    Reserva.generarReservaRevista(usuario3, ejRev1, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario3, ejRev2, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario3, ejRev3, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario3, ejRev4, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario3, ejRev5, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario3, ejRev6, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario3, ejRev7, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario3, ejRev8, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario3, ejRev9, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario3, ejRev10, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))

    Prestamo.devolucion(0, biblioteca, usuario3)
    Prestamo.devolucion(0, biblioteca, usuario3)
    Prestamo.devolucion(0, biblioteca, usuario3)
    Prestamo.devolucion(0, biblioteca, usuario3)
    Prestamo.devolucion(0, biblioteca, usuario3)
    Prestamo.devolucion(0, biblioteca, usuario3)
    Prestamo.devolucion(0, biblioteca, usuario3)
    Prestamo.devolucion(0, biblioteca, usuario3)
    Prestamo.devolucion(0, biblioteca, usuario3)
    Prestamo.devolucion(0, biblioteca, usuario3)
    Prestamo.devolucion(0, biblioteca, usuario3)
    Prestamo.devolucion(0, biblioteca, usuario3)
    Reserva.cancelarReserva(0, biblioteca, usuario3)
    Reserva.cancelarReserva(0, biblioteca, usuario3)
    Reserva.cancelarReserva(0, biblioteca, usuario3)
    Reserva.cancelarReserva(0, biblioteca, usuario3)
    Reserva.cancelarReserva(0, biblioteca, usuario3)
    Reserva.cancelarReserva(0, biblioteca, usuario3)
    Reserva.cancelarReserva(0, biblioteca, usuario3)
    Reserva.cancelarReserva(0, biblioteca, usuario3)
    Reserva.cancelarReserva(0, biblioteca, usuario3)
    Reserva.cancelarReserva(0, biblioteca, usuario3)

    # usuario 4
    Prestamo.generarPrestamoLibro(usuario4, EjLibro1, biblioteca)
    Prestamo.generarPrestamoLibro(usuario4, EjLibro2, biblioteca)
    Prestamo.generarPrestamoLibro(usuario4, EjLibro3, biblioteca)
    Prestamo.generarPrestamoLibro(usuario4, EjLibro4, biblioteca)
    Prestamo.generarPrestamoLibro(usuario4, EjLibro5, biblioteca)
    Prestamo.generarPrestamoLibro(usuario4, EjLibro6, biblioteca)
    Prestamo.generarPrestamoLibro(usuario4, EjLibro7, biblioteca)
    Prestamo.generarPrestamoLibro(usuario4, EjLibro8, biblioteca)
    Prestamo.generarPrestamoLibro(usuario4, EjLibro9, biblioteca)
    Prestamo.generarPrestamoLibro(usuario4, EjLibro10, biblioteca)
    Prestamo.generarPrestamoLibro(usuario4, EjLibro11, biblioteca)
    Prestamo.generarPrestamoLibro(usuario4, EjLibro12, biblioteca)

    Reserva.generarReservaRevista(usuario4, ejRev1, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario4, ejRev2, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario4, ejRev3, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario4, ejRev4, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario4, ejRev5, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario4, ejRev6, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario4, ejRev7, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario4, ejRev8, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario4, ejRev9, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario4, ejRev10, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))

    Prestamo.devolucion(0, biblioteca, usuario4)
    Prestamo.devolucion(0, biblioteca, usuario4)
    Prestamo.devolucion(0, biblioteca, usuario4)
    Prestamo.devolucion(0, biblioteca, usuario4)
    Prestamo.devolucion(0, biblioteca, usuario4)
    Prestamo.devolucion(0, biblioteca, usuario4)
    Prestamo.devolucion(0, biblioteca, usuario4)
    Prestamo.devolucion(0, biblioteca, usuario4)
    Prestamo.devolucion(0, biblioteca, usuario4)
    Prestamo.devolucion(0, biblioteca, usuario4)
    Prestamo.devolucion(0, biblioteca, usuario4)
    Prestamo.devolucion(0, biblioteca, usuario4)
    Reserva.cancelarReserva(0, biblioteca, usuario4)
    Reserva.cancelarReserva(0, biblioteca, usuario4)
    Reserva.cancelarReserva(0, biblioteca, usuario4)
    Reserva.cancelarReserva(0, biblioteca, usuario4)
    Reserva.cancelarReserva(0, biblioteca, usuario4)
    Reserva.cancelarReserva(0, biblioteca, usuario4)
    Reserva.cancelarReserva(0, biblioteca, usuario4)
    Reserva.cancelarReserva(0, biblioteca, usuario4)
    Reserva.cancelarReserva(0, biblioteca, usuario4)
    Reserva.cancelarReserva(0, biblioteca, usuario4)

    # usuario 5
    Prestamo.generarPrestamoLibro(usuario5, EjLibro1, biblioteca)
    Prestamo.generarPrestamoLibro(usuario5, EjLibro2, biblioteca)
    Prestamo.generarPrestamoLibro(usuario5, EjLibro3, biblioteca)
    Prestamo.generarPrestamoLibro(usuario5, EjLibro4, biblioteca)
    Prestamo.generarPrestamoLibro(usuario5, EjLibro5, biblioteca)
    Prestamo.generarPrestamoLibro(usuario5, EjLibro6, biblioteca)
    Prestamo.generarPrestamoLibro(usuario5, EjLibro7, biblioteca)
    Prestamo.generarPrestamoLibro(usuario5, EjLibro8, biblioteca)
    Prestamo.generarPrestamoLibro(usuario5, EjLibro9, biblioteca)
    Prestamo.generarPrestamoLibro(usuario5, EjLibro10, biblioteca)
    Prestamo.generarPrestamoLibro(usuario5, EjLibro11, biblioteca)
    Prestamo.generarPrestamoLibro(usuario5, EjLibro12, biblioteca)

    Reserva.generarReservaRevista(usuario5, ejRev1, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario5, ejRev2, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario5, ejRev3, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario5, ejRev4, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario5, ejRev5, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario5, ejRev6, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario5, ejRev7, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario5, ejRev8, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario5, ejRev9, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario5, ejRev10, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))

    Prestamo.devolucion(0, biblioteca, usuario5)
    Prestamo.devolucion(0, biblioteca, usuario5)
    Prestamo.devolucion(0, biblioteca, usuario5)
    Prestamo.devolucion(0, biblioteca, usuario5)
    Prestamo.devolucion(0, biblioteca, usuario5)
    Prestamo.devolucion(0, biblioteca, usuario5)
    Prestamo.devolucion(0, biblioteca, usuario5)
    Prestamo.devolucion(0, biblioteca, usuario5)
    Prestamo.devolucion(0, biblioteca, usuario5)
    Prestamo.devolucion(0, biblioteca, usuario5)
    Prestamo.devolucion(0, biblioteca, usuario5)
    Prestamo.devolucion(0, biblioteca, usuario5)
    Reserva.cancelarReserva(0, biblioteca, usuario5)
    Reserva.cancelarReserva(0, biblioteca, usuario5)
    Reserva.cancelarReserva(0, biblioteca, usuario5)
    Reserva.cancelarReserva(0, biblioteca, usuario5)
    Reserva.cancelarReserva(0, biblioteca, usuario5)
    Reserva.cancelarReserva(0, biblioteca, usuario5)
    Reserva.cancelarReserva(0, biblioteca, usuario5)
    Reserva.cancelarReserva(0, biblioteca, usuario5)
    Reserva.cancelarReserva(0, biblioteca, usuario5)
    Reserva.cancelarReserva(0, biblioteca, usuario5)

    # usuario 6

    Prestamo.generarPrestamoLibro(usuario6, EjLibro1, biblioteca)
    Prestamo.generarPrestamoLibro(usuario6, EjLibro2, biblioteca)
    Prestamo.generarPrestamoLibro(usuario6, EjLibro3, biblioteca)
    Prestamo.generarPrestamoLibro(usuario6, EjLibro4, biblioteca)
    Prestamo.generarPrestamoLibro(usuario6, EjLibro5, biblioteca)
    Prestamo.generarPrestamoLibro(usuario6, EjLibro6, biblioteca)
    Prestamo.generarPrestamoLibro(usuario6, EjLibro7, biblioteca)
    Prestamo.generarPrestamoLibro(usuario6, EjLibro8, biblioteca)
    Prestamo.generarPrestamoLibro(usuario6, EjLibro9, biblioteca)
    Prestamo.generarPrestamoLibro(usuario6, EjLibro10, biblioteca)
    Prestamo.generarPrestamoLibro(usuario6, EjLibro11, biblioteca)
    Prestamo.generarPrestamoLibro(usuario6, EjLibro12, biblioteca)

    Reserva.generarReservaRevista(usuario6, ejRev1, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario6, ejRev2, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario6, ejRev3, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario6, ejRev4, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario6, ejRev5, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario6, ejRev6, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario6, ejRev7, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario6, ejRev8, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario6, ejRev9, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario6, ejRev10, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))

    Prestamo.devolucion(0, biblioteca, usuario6)
    Prestamo.devolucion(0, biblioteca, usuario6)
    Prestamo.devolucion(0, biblioteca, usuario6)
    Prestamo.devolucion(0, biblioteca, usuario6)
    Prestamo.devolucion(0, biblioteca, usuario6)
    Prestamo.devolucion(0, biblioteca, usuario6)
    Prestamo.devolucion(0, biblioteca, usuario6)
    Prestamo.devolucion(0, biblioteca, usuario6)
    Prestamo.devolucion(0, biblioteca, usuario6)
    Prestamo.devolucion(0, biblioteca, usuario6)
    Prestamo.devolucion(0, biblioteca, usuario6)
    Prestamo.devolucion(0, biblioteca, usuario6)
    Reserva.cancelarReserva(0, biblioteca, usuario6)
    Reserva.cancelarReserva(0, biblioteca, usuario6)
    Reserva.cancelarReserva(0, biblioteca, usuario6)
    Reserva.cancelarReserva(0, biblioteca, usuario6)
    Reserva.cancelarReserva(0, biblioteca, usuario6)
    Reserva.cancelarReserva(0, biblioteca, usuario6)
    Reserva.cancelarReserva(0, biblioteca, usuario6)
    Reserva.cancelarReserva(0, biblioteca, usuario6)
    Reserva.cancelarReserva(0, biblioteca, usuario6)
    Reserva.cancelarReserva(0, biblioteca, usuario6)

    # usuario 7
    Prestamo.generarPrestamoLibro(usuario7, EjLibro1, biblioteca)
    Prestamo.generarPrestamoLibro(usuario7, EjLibro2, biblioteca)
    Prestamo.generarPrestamoLibro(usuario7, EjLibro3, biblioteca)
    Prestamo.generarPrestamoLibro(usuario7, EjLibro4, biblioteca)
    Prestamo.generarPrestamoLibro(usuario7, EjLibro5, biblioteca)
    Prestamo.generarPrestamoLibro(usuario7, EjLibro6, biblioteca)
    Prestamo.generarPrestamoLibro(usuario7, EjLibro7, biblioteca)
    Prestamo.generarPrestamoLibro(usuario7, EjLibro8, biblioteca)
    Prestamo.generarPrestamoLibro(usuario7, EjLibro9, biblioteca)
    Prestamo.generarPrestamoLibro(usuario7, EjLibro10, biblioteca)
    Prestamo.generarPrestamoLibro(usuario7, EjLibro11, biblioteca)
    Prestamo.generarPrestamoLibro(usuario7, EjLibro12, biblioteca)

    Reserva.generarReservaRevista(usuario7, ejRev1, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario7, ejRev2, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario7, ejRev3, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario7, ejRev4, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario7, ejRev5, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario7, ejRev6, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario7, ejRev7, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario7, ejRev8, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario7, ejRev9, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))
    Reserva.generarReservaRevista(usuario7, ejRev10, biblioteca, datetime(2022, 3, 4),
                                  datetime(2022, 7, 5))

    Prestamo.devolucion(0, biblioteca, usuario7)
    Prestamo.devolucion(0, biblioteca, usuario7)
    Prestamo.devolucion(0, biblioteca, usuario7)
    Prestamo.devolucion(0, biblioteca, usuario7)
    Prestamo.devolucion(0, biblioteca, usuario7)
    Prestamo.devolucion(0, biblioteca, usuario7)
    Prestamo.devolucion(0, biblioteca, usuario7)
    Prestamo.devolucion(0, biblioteca, usuario7)
    Prestamo.devolucion(0, biblioteca, usuario7)
    Prestamo.devolucion(0, biblioteca, usuario7)
    Prestamo.devolucion(0, biblioteca, usuario7)
    Prestamo.devolucion(0, biblioteca, usuario7)
    Reserva.cancelarReserva(0, biblioteca, usuario7)
    Reserva.cancelarReserva(0, biblioteca, usuario7)
    Reserva.cancelarReserva(0, biblioteca, usuario7)
    Reserva.cancelarReserva(0, biblioteca, usuario7)
    Reserva.cancelarReserva(0, biblioteca, usuario7)
    Reserva.cancelarReserva(0, biblioteca, usuario7)
    Reserva.cancelarReserva(0, biblioteca, usuario7)
    Reserva.cancelarReserva(0, biblioteca, usuario7)
    Reserva.cancelarReserva(0, biblioteca, usuario7)
    Reserva.cancelarReserva(0, biblioteca, usuario7)


