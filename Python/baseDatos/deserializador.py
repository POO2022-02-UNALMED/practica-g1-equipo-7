import pathlib
import pickle
import os

from Python.gestorAplicacion.libreria.biblioteca import Biblioteca

def deserializar(lista, className):
    def camino(className):
        return os.path.join(pathlib.Path(__file__).parent.absolute(), f"temp\{className}.txt")

    try:
        picklefile = open(camino(className), 'rb')

    except:
        picklefile = open(camino(className), 'x')
        picklefile = open(camino(className), 'rb')

        # Unpickle los datos
    if os.path.getsize(camino(className)) > 0:
        lista = pickle.load(picklefile)

        # Cerrar el archivo
    picklefile.close()

    return lista

def deserializarTodo():
    Biblioteca._ejemplaresLibros = deserializar(Biblioteca._ejemplaresLibros, "ejemplaresLibros")
    Biblioteca._ejemplaresRevistas = deserializar(Biblioteca._ejemplaresRevistas, "ejemplaresRevistas")
    Biblioteca._libros = deserializar(Biblioteca._libros, "libros")
    Biblioteca._revistas = deserializar(Biblioteca._revistas, "revistas")
    Biblioteca._usuarios = deserializar(Biblioteca._usuarios, "usuarios")
    Biblioteca._historialLibrosUsados = deserializar(Biblioteca._historialLibrosUsados, "historialLibrosUsados")
    Biblioteca._historialRevistasUsadas = deserializar(Biblioteca._historialRevistasUsadas, "historialRevistasUsadas")


