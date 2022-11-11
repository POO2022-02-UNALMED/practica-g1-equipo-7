class Biblioteca:

    def __init__(self, ejemplaresLibros: list, ejemplaresRevistas: list, libros: list, revistas: list, usuarios: list, historialLibrosUsados: list, historialRevistasUsadas: list):
        self._ejemplaresLibros = ejemplaresLibros
        self._ejemplaresRevistas = ejemplaresRevistas
        self._libros = libros
        self._revistas = revistas
        self._usuarios = usuarios
        self._historialLibrosUsados = historialLibrosUsados
        self._historialRevistasUsadas = historialRevistasUsadas


    #getters y setters
    def getEjemplaresLibros(self):
        return self._ejemplaresLibros

    def getEjemplaresRevistas(self):
        return self._ejemplaresRevistas

    def getLibros(self):
        return self._libros

    def getRevistas(self):
        return self._revistas

    def getUsuarios(self):
        return self._usuarios

    def getHistorialLibrosUsados(self):
        return self._historialLibrosUsados

    def getHistorialRevistasUsadas(self):
        return self._historialRevistasUsadas

    def setEjemplaresLibros(self, ejemplares):
        self._ejemplaresLibros = ejemplares

    def setEjemplaresRevistas(self, ejemplares):
        self._ejemplaresRevistas = ejemplares

    def setLibros(self, libros):
        self._libros = libros

    def setRevistas(self, revistas):
        self._revistas = revistas

    def setUsuarios(self, usuarios):
        self._usuarios = usuarios

    def setHistorialLibrosUsados(self, historial):
        self._historialLibrosUsados = historial

    def setHistorialRevistasUsadas(self, historial):
        self._historialRevistasUsadas = historial

    #Metodos
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