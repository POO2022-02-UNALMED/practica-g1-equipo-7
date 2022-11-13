from tkinter import *

class FieldFrame(Frame):
    def __init__(self, ventana, tituloCriterios="", criterios=None, tituloValores="", valores=None, habilitado=None):
        super().__init__(ventana)
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores
        self._habilitado = habilitado

        self._elementos = []

        label_Criterios = Label(self, text = tituloCriterios, font = ("Helvetica", 14))
        label_Criterios.grid(column = 0, row = 0, padx = (10,10), pady = (10,10))

        label_Valores = Label(self, text=tituloValores, font=("Helvetica", 14))
        label_Valores.grid(column=1, row=0, padx=(10, 10), pady=(10, 10))

        # Crear cada uno de los criterios
        for i in range(len(criterios)):
            # Crear y colocar nombre de cada criterio
            label_criterio = Label(self, text=criterios[i], font=("Helvetica", 12))
            label_criterio.grid(column=0, row=i + 1, padx=(10, 10), pady=(10, 10))

            # Crear y colocar entrada de cada criterio
            entry = Entry(self, font=("Helvetica", 12))
            entry.grid(column=1, row=i + 1, padx=(10, 10), pady=(10, 10))

            # Colocar el valor inicial si lo hay
            if valores is not None:
                entry.insert(0, valores[i])

            # Si el campo es no-editable, deshabilitarlo
            if habilitado is not None and not habilitado[i]:
                entry.configure(state = DISABLED)

            # Anadir a la lista de elementos
            self._elementos.append(entry)

        # GetValue
        # criterio: El criterio cuyo valor se quiere obtener

    def getValue(self, criterio):
        indice = self._criterios.index(criterio)
        return self._elementos[indice].get()