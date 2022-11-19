



class Servicio():
    _ejemplarRevistaDisponibles = []
    _ejemplarLibroDisponibles = []

    def __init__(self, usuario, ejemplarEscogido, tituloEscogido, tiquete = None):
        self._usuario = usuario
        self._ejemplarEscogido = ejemplarEscogido
        self._tituloEscogido = tituloEscogido
        self._tiquete = tiquete

    #Getters y setters
    def getUsuario(self):
        return self._usuario

    def getEjemplarEscogido(self):
        return self._ejemplarEscogido

    def getTituloEscogido(self):
        return self._tituloEscogido

    def getTiquete(self):
        return self._tiquete

    @classmethod
    def getEjemplarRevistaDisponibles(cls) -> list:
        return cls._ejemplarRevistaDisponibles

    @classmethod
    def getEjemplarLibroDisponibles(cls) -> list:
        return cls._ejemplarLibroDisponibles

    def setUsuario(self, usuario):
        self._usuario = usuario

    def setEjemplarEscogido(self, ejemplar):
        self._ejemplarEscogido = ejemplar

    def setTituloEscogido(self, titulo):
        self._tituloEscogido = titulo

    def setTiquete(self, tiquete):
        self._tiquete = tiquete

    @classmethod
    def setEjemplarRevistaDisponibles(cls, ejemplarRevistaDisponibles):
        cls._ejemplarRevistaDisponibles = ejemplarRevistaDisponibles

    @classmethod
    def setEjemplarLibroDisponibles(cls, ejemplarLibroDisponibles):
        cls._ejemplarLibroDisponibles = ejemplarLibroDisponibles

    #Metodos
    def filtrarLibrosDisponibles(self, biblioteca):
        ejemplares = []
        for ejemplar in biblioteca.getEjemplaresLibros():
            if (ejemplar.getEstadoEjemplar().isPrestado() == False and ejemplar.getEstadoEjemplar().isReservado() == False):
                ejemplares.append(ejemplar)

        self.setEjemplarLibroDisponibles(ejemplares)

    def filtrarRevistasDisponibles(self, biblioteca):
        ejemplares = []
        for ejemplar in biblioteca.getEjemplaresRevistas():
            if (ejemplar.getEstadoEjemplar().isPrestado() == False and ejemplar.getEstadoEjemplar().isReservado() == False):
                ejemplares.append(ejemplar)

        self.setEjemplarRevistaDisponibles(ejemplares)

    def mostrarTituloEscogido(self):
        return self.getTituloEscogido().mostrarse()

    @classmethod
    def eliminarDeLibrosDisponibles(cls, ejemplarLibro):
        for ejemplarL in cls._ejemplarLibroDisponibles:
            if ejemplarLibro == ejemplarL:
                cls._ejemplarLibroDisponibles.remove(ejemplarLibro)

    @classmethod
    def eliminarDeRevistasDisponibles(cls, ejemplarRevista):
        for ejemplarR in cls._ejemplarRevistaDisponibles:
            if ejemplarRevista == ejemplarR:
                cls._ejemplarRevistaDisponibles.remove(ejemplarRevista)