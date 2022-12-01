from Python.excepciones.errorAplicacion import ErrorAplicacion

class ExcepcionEntry(ErrorAplicacion):

    def __init__(self, error):
        super().__init__(f"Hubo un error en la entrada de los campos: \n {error}")