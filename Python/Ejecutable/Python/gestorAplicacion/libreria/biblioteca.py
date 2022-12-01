from Python.baseDatos.deserializador import deserializar


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
        Biblioteca._ejemplaresLibros = deserializar(Biblioteca._ejemplaresLibros, "ejemplaresLibros")
        Biblioteca._ejemplaresRevistas = deserializar(Biblioteca._ejemplaresRevistas, "ejemplaresRevistas")
        Biblioteca._libros = deserializar(Biblioteca._libros, "libros")
        Biblioteca._revistas = deserializar(Biblioteca._revistas, "revistas")
        Biblioteca._usuarios = deserializar(Biblioteca._usuarios, "usuarios")
        Biblioteca._historialLibrosUsados = deserializar(Biblioteca._historialLibrosUsados, "historialLibrosUsados")
        Biblioteca._historialRevistasUsadas = deserializar(Biblioteca._historialRevistasUsadas,"historialRevistasUsadas")
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

    # Metodos (Volverlos de clase)
    @classmethod
    def añadirLibro(cls, libro):
        cls._libros.append(libro)

    def añadirRevista(self, revista):
        self._revistas.append(revista)

    def añadirEjemplarLibro(self, ejemplar):
        self._ejemplaresLibros.append(ejemplar)

    def añadirEjemplarRevista(self, ejemplar):
        self._ejemplaresRevistas.append(ejemplar)
    @classmethod
    def añadirUsuario(cls, usuario):
        cls._usuarios.append(usuario)

    def añadirHistorialLibrosUsados(self, libro):
        self._historialLibrosUsados.append(libro)

    def añadirHistorialRevistasUsadas(self, revista):
        self._historialRevistasUsadas.append(revista)
