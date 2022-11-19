from Python.gestorAplicacion.servicios.reserva import Reserva
from Python.gestorAplicacion.servicios.prestamo import Prestamo
from Python.gestorAplicacion.servicios.servicio import Servicio
from Python.gestorAplicacion.servicios.tiquete import Tiquete
from Python.gestorAplicacion.servicios.usuario import Usuario

from Python.gestorAplicacion.libreria.categoria import CATEGORIA
from Python.gestorAplicacion.libreria.ejemplar import Ejemplar
from Python.gestorAplicacion.libreria.ejemplarLibro import EjemplarLibro
from Python.gestorAplicacion.libreria.ejemplarRevista import EjemplarRevista
from Python.gestorAplicacion.libreria.estadoEjemplar import EstadoEjemplar
from Python.gestorAplicacion.libreria.genero import GENERO
from Python.gestorAplicacion.libreria.libro import Libro
from Python.gestorAplicacion.libreria.revista import Revista
from Python.gestorAplicacion.libreria.titulo import Titulo



class Biblioteca:
    _ejemplaresLibros = []
    _ejemplaresRevistas = []
    _libros = []
    _revistas = []
    _usuarios = []
    _historialLibrosUsados = []
    _historialRevistasUsadas = []

    def __init__(self):
        #deserializarTodo()
        pass


    # getters y setters
    @classmethod
    def getEjemplaresLibros(cls):
        return cls._ejemplaresLibros

    @classmethod
    def getEjemplaresRevistas(cls):
        return cls._ejemplaresRevistas

    @classmethod
    def getLibros(cls):
        return cls._libros

    @classmethod
    def getRevistas(cls):
        return cls._revistas

    @classmethod
    def getUsuarios(cls):
        return cls._usuarios

    @classmethod
    def getHistorialLibrosUsados(cls):
        return cls._historialLibrosUsados

    @classmethod
    def getHistorialRevistasUsadas(cls):
        return cls._historialRevistasUsadas

    @classmethod
    def setEjemplaresLibros(cls, ejemplares):
        cls._ejemplaresLibros = ejemplares

    def setEjemplaresRevistas(cls, ejemplares):
        cls._ejemplaresRevistas = ejemplares

    @classmethod
    def setLibros(cls, libros):
        cls._libros = libros

    @classmethod
    def setRevistas(cls, revistas):
        cls._revistas = revistas

    @classmethod
    def setUsuarios(cls, usuarios):
        cls._usuarios = usuarios

    @classmethod
    def setHistorialLibrosUsados(cls, historial):
        cls._historialLibrosUsados = historial

    @classmethod
    def setHistorialRevistasUsadas(cls, historial):
        cls._historialRevistasUsadas = historial

    # Metodos
    def añadirLibro(self, libro):
        self._libros.append(libro)

    def añadirRevista(self, revista):
        self._revistas.append(revista)

    def añadirEjemplarLibro(self, ejemplar):
        self._ejemplaresLibros.append(ejemplar)

    def añadirEjemplarRevista(self, ejemplar):
        self._ejemplaresRevistas.append(ejemplar)

    def añadirUsuario(self, usuario):
        self._usuarios = usuario

    def añadirHistorialLibrosUsados(self, libro):
        self._historialLibrosUsados.append(libro)

    def añadirHistorialRevistasUsadas(self, revista):
        self._historialRevistasUsadas.append(revista)
