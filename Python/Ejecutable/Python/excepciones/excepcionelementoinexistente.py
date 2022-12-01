from Python.excepciones.errorapp import ErrorApp

class ExcepcionElementoInexistente(ErrorApp):

    def __init__(self):
        super().__init__(f"El elemento al que intentó acceder no existe")