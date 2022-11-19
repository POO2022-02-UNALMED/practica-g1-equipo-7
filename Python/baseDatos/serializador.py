import pathlib
import pickle
import os

from Python.gestorAplicacion.libreria.biblioteca import Biblioteca


def camino(className):
    return os.path.join(pathlib.Path(__file__).parent.absolute(), f"temp\{className}.txt")
def serializar(lista, className):

    try:
        picklefile = open(camino(className), 'wb')

        pickle.dump(lista, picklefile)

        picklefile.close()
    except:
        print("Error de serialización")

def serializarTodo():
    serializar(Biblioteca.getEjemplaresLibros(), "ejemplaresLibros")
    serializar(Biblioteca.getEjemplaresRevistas(), "ejemplaresRevistas")
    serializar(Biblioteca.getLibros(), "libros")
    serializar(Biblioteca.getRevistas(),"revistas")
    serializar(Biblioteca.getUsuarios(), "usuarios")
    serializar(Biblioteca.getHistorialLibrosUsados(), "historialLibrosUsados")
    serializar(Biblioteca.getHistorialRevistasUsadas(), "historialRevistasUsadas")