from Python.excepciones.errorapp import ErrorApp

class ExcepcionEntry(ErrorApp):

    def __init__(self, error):
        super().__init__(f"Hubo un error en la entrada de los campos: \n {error}")