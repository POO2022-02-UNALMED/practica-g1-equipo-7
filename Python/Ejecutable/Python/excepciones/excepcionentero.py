from Python.excepciones.excepcionentry import ExcepcionEntry

class ExcepcionEntero(ExcepcionEntry):
    def __init__(self):
        super().__init__(f"Tiene que ingresar un numero valido en el campo")

