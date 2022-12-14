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
    """* Se recorre la lista 'historialLibrosUsados' para posteriormente crear un diccionario que contendra 
       la cantidad de veces que se repite cada genero. Teniendo ya este diccionario creado, se busca cu??l
        es el genero que m??s aparece y este se define como el favorito
        """
    def encontrarGeneroFavorito(self):
        generosLeidos = {}
        for libro in self.getHistorialLibrosUsados():
            if libro.getGenero() in generosLeidos:
                generosLeidos[libro.getGenero()] += 1
            else:
                generosLeidos[libro.getGenero()] = 1

        #Buscar el genero m??s leido
        generoFavorito = max(generosLeidos, key=generosLeidos.get, default=0)
        self.setGeneroFavorito(generoFavorito)

    """* Se recorre la lista 'historialRevistasUsadas' para posteriormente crear un diccionario que contendra
       la cantidad de veces que se repite cada categoria. Teniendo ya este diccionario creado, se busca 
       cu??l es la categoria que m??s aparece y esta se define como la favorita
       """
    def encontrarCategoriaFavorita(self):
        categoriasLeidas = {}
        for revista in self.getHistorialRevistasUsadas():
            if revista.getCategoria() in categoriasLeidas:
                categoriasLeidas[revista.getCategoria()] += 1
            else:
                categoriasLeidas[revista.getCategoria()] = 1

        #Buscar categoria favorita
        categoriaFavorita = max(categoriasLeidas, key=categoriasLeidas.get, default=0)
        self.setCategoriaFavorita(categoriaFavorita)

    def a??adirHistorialLibros(self, libro: Libro):
        self._historialLibrosUsados.append(libro)

    def a??adirHistorialRevistas(self, revista: Revista):
        self._historialRevistasUsadas.append(revista)

    def a??adirReserva(self, reserva: Reserva):
        self._reservas.append(reserva)

    def a??adirPrestamo(self, prestamo: Prestamo):
        self._prestamos.append(prestamo)

    def a??adirTiquete(self, tiquete: Tiquete):
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



