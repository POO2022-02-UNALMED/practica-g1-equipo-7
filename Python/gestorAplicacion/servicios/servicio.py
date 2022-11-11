from gestorAplicacion.libreria.biblioteca import Biblioteca
from gestorAplicacion.libreria.ejemplar import Ejemplar
from gestorAplicacion.libreria.titulo import Titulo
from gestorAplicacion.servicios.tiquete import Tiquete
from gestorAplicacion.servicios.usuario import Usuario


class Servicio():
    _ejemplarRevistaDisponibles = [];
    _ejemplarLibroDisponibles = [];

    def __init__(self, usuario: Usuario, ejemplarEscogido: Ejemplar, tituloEscogido: Titulo, tiquete = None):
        self._usuario = usuario
        self._ejemplarEscogido = ejemplarEscogido
        self._tituloEscogido = tituloEscogido
        self._tiquete = tiquete

    #Getters y setters
    def getUsuario(self) -> Usuario:
        return self._usuario

    def getEjemplarEscogido(self) -> Ejemplar:
        return self._ejemplarEscogido

    def getTituloEscogido(self) -> Titulo:
        return self._tituloEscogido

    def getTiquete(self) -> Tiquete:
        return self._tiquete

    @classmethod
    def getEjemplarRevistaDisponibles(cls) -> list:
        return cls._ejemplarRevistaDisponibles

    @classmethod
    def getEjemplarLibroDisponibles(cls) -> list:
        return cls._ejemplarLibroDisponibles

    def setUsuario(self, usuario: Usuario):
        self._usuario = usuario

    def setEjemplarEscogido(self, ejemplar: Ejemplar):
        self._ejemplarEscogido = ejemplar

    def setTituloEscogido(self, titulo: Titulo):
        self._tituloEscogido = titulo

    def setTiquete(self, tiquete: Tiquete):
        self._tiquete = tiquete

    @classmethod
    def setEjemplarRevistaDisponibles(cls, ejemplarRevistaDisponibles):
        cls._ejemplarRevistaDisponibles = ejemplarRevistaDisponibles

    @classmethod
    def setEjemplarLibroDisponibles(cls, ejemplarLibroDisponibles):
        cls._ejemplarLibroDisponibles = ejemplarLibroDisponibles

    #Metodos
    def filtrarLibrosDisponibles(self, biblioteca: Biblioteca):
        ejemplares = []
        for ejemplar in biblioteca.getEjemplaresLibros():
            if (ejemplar.getEstadoEjemplar().isPrestado() == False and ejemplar.getEstadoEjemplar().isReservado() == False):
                ejemplares.append(ejemplar)

        self.setEjemplarLibroDisponibles(ejemplares)

    def filtrarRevistasDisponibles(self, biblioteca:Biblioteca):
        ejemplares = []
        for ejemplar in biblioteca.getEjemplaresRevistas():
            if (ejemplar.getEstadoEjemplar().isPrestado() == False and ejemplar.getEstadoEjemplar().isReservado() == False):
                ejemplares.append(ejemplar)

        self.setEjemplarRevistaDisponibles(ejemplares)

    def mostrarTituloEscogido(self):
        return self.getTituloEscogido().mostrarse()

    @classmethod
    def eliminarDeLibrosDisponibles(cls, ejemplarLibro: Ejemplar):
        cls._ejemplarLibroDisponibles.remove(ejemplarLibro)

    @classmethod
    def eliminarDeRevistasDisponibles(cls, ejemplarRevista: Ejemplar):
        cls._ejemplarRevistaDisponibles.remove(ejemplarRevista)