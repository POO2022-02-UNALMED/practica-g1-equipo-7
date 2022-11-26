from Python.excepciones.excepcionentry import ExcepcionEntry

class ExcepcionString(ExcepcionEntry):
    def __init__(self):
        super().__init__(f"Tiene que ingresar un string en el campo")