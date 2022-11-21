from Python.gestorAplicacion.libreria.categoria import CATEGORIA
from Python.gestorAplicacion.libreria.genero import GENERO
from Python.gestorAplicacion.libreria.libro import Libro
from Python.gestorAplicacion.libreria.revista import Revista
from Python.gestorAplicacion.servicios.prestamo import Prestamo
from Python.gestorAplicacion.servicios.reserva import Reserva
from Python.gestorAplicacion.servicios.tiquete import Tiquete


class Usuario():
    def __init__(self, nombre: str, id: int, prestamos: list, reservas: list, tiquetes: list, historialLibrosUsados: list,
                 historialResvistasUsadas: list, multa = False, generoFavorito = GENERO.NOVELA, categoriaFavorita = CATEGORIA.ACTUALIDAD):
        self._nombre = nombre
        self._id = id
        self._prestamos = prestamos
        self._reservas = reservas
        self._tiquetes = tiquetes
        self._historialLibrosUsados = historialLibrosUsados
        self._historialRevistasUsadas = historialResvistasUsadas
        self._multa = multa
        self._generoFavorito = generoFavorito
        self._categoriaFavorita = categoriaFavorita

    #getters y setters
    def getNombre(self)-> str:
        return self._nombre

    def getId(self) -> int:
        return self._id

    def getPrestamos(self)-> list:
        return self._prestamos

    def getReservas(self)-> list:
        return self._reservas

    def getTiquetes(self)-> list:
        return self._tiquetes

    def getHistorialLibrosUsados(self)-> list:
        return self._historialLibrosUsados

    def getHistorialRevistasUsadas(self)-> list:
        return self._historialRevistasUsadas

    def getGeneroFavorito(self)-> GENERO:
        return self._generoFavorito

    def getCategoriaFavorita(self)-> CATEGORIA:
        return self._categoriaFavorita

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def setId(self, id: int):
        self._id = id

    def setPrestamos(self, prestamos: list):
        self._prestamos = prestamos

    def setReservas(self, reservas: list):
        self._reservas = reservas

    def setTiquetes(self, tiquetes: list):
        self._tiquetes = tiquetes

    def setHistorialLibrosUsados(self, historial: list):
        self._historialLibrosUsados = historial

    def setHistorialRevistasUsadas(self, historial: list):
        self._historialRevistasUsadas = historial

    def setGeneroFavorito(self, genero = GENERO):
        self._generoFavorito = genero

    def setCategoriaFavorita(self, categoria: CATEGORIA):
        self._categoriaFavorita = categoria

    #Metodos
    def encontrarGeneroFavorito(self):
        generosLeidos = {}

        for libro in self.getHistorialLibrosUsados():
            if libro.getGenero() in generosLeidos:
                generosLeidos[libro.getGenero()] += 1
            else:
                generosLeidos[libro.getGenero()] = 1

        #Buscar el genero más leido
        generoFavorito = max(generosLeidos, key=generosLeidos.get)
        self.setGeneroFavorito(generoFavorito)

    def encontrarCategoriaFavorita(self):
        categoriasLeidas = {}

        for revista in self.getHistorialRevistasUsadas():
            if revista.getCategoria() in categoriasLeidas:
                categoriasLeidas[revista.getCategoria()] += 1
            else:
                categoriasLeidas[revista.getCategoria()] = 1

        #Buscar categoria favorita
        categoriaFavorita = max(categoriasLeidas, key=categoriasLeidas.get)
        self.setCategoriaFavorita(categoriaFavorita)

    def añadirHistorialLibros(self, libro: Libro):
        self._historialLibrosUsados.append(libro)

    def añadirHistorialRevistas(self, revista: Revista):
        self._historialRevistasUsadas.append(Revista)

    def añadirReserva(self, reserva: Reserva):
        self._reservas.append(reserva)

    def añadirPrestamo(self, prestamo: Prestamo):
        self._prestamos.append(prestamo)

    def añadirTiquete(self, tiquete: Tiquete):
        self._tiquetes.append(tiquete)

    def eliminarReserva(self, reserva: Reserva):
        for r in self._reservas:
            if reserva == r:
                self._reservas.remove(reserva)

    def eliminarPrestamo(self, prestamo: Prestamo):
        for p in self._prestamos:
            if prestamo == p:
                self._prestamos.remove(prestamo)

    def eliminarTiquete(self, tiquete: Tiquete):
        self._tiquetes.remove(tiquete)

    def encontrarGeneroFavorito(self):
        diccionario = {}
        generoFavorito = None
        for libro in self._historialLibrosUsados:
            if libro.getGenero() not in diccionario:
                diccionario[libro.getGenero()] = 0
            else:
                diccionario[libro.getGenero()] += 1

        maxLeido = 0
        for genero in diccionario:
            if diccionario[genero] > maxLeido:
                generoFavorito = genero
                maxLeido = diccionario[genero]

        return generoFavorito

