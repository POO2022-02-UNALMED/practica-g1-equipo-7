from Python.excepciones.excepcionentry import ExcepcionEntry

class ExcepcionString(ExcepcionEntry):
    def __init__(self):
        super().__init__(f"Tiene que ingresar Algo en el campo")