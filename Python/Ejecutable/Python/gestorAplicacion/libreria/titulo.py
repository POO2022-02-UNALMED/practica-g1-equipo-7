

class Titulo():

    def __init__(self, nombre: str, autor: str, ISBN: int):
        self._nombre = nombre
        self._autor = autor
        self._ISBN = ISBN
        self._usos = 0

    def getNombre(self) -> str:
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getAutor(self) -> str:
        return self._autor

    def setAutor(self, autor: str):
        self._autor = autor

    def getISBN(self) -> int:
        return self._ISBN

    def getUsos(self) -> int:
        return self._usos

    def setUsos(self, usos: int):
        self._usos = usos

    def usado(self):
        self._usos += 1

    def mostrarse(self):
        pass