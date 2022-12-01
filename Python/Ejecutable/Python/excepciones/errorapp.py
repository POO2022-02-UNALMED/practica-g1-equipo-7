class ErrorApp(Exception):

    def __init__(self, error):
        super().__init__(f"Manejo de errores en al app:\n{error}")