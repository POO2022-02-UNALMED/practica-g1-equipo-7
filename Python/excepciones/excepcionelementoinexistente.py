from Python.excepciones.errorAplicacion import ErrorAplicacion

class ExcepcionElementoInexistente(ErrorAplicacion):

    def __init__(self):
        super().__init__(f"El elemento al que intentó acceder no existe")