import tkinter as tk
from tkinter import Frame
from tkinter import ttk
from tkinter import messagebox

class FieldFrame(Frame):
    def __init__(self, frame, tituloFuncion, descripcion, tituloCriterios, criterios, tituloValores, valores,val=None, habilitados=None):
        self._tituloFuncion = tituloFuncion # titulo funcionalidad
        self._descripcion = descripcion # descripcion de la funcionalidad
        self._tituloCriterios = tituloCriterios
        self._criterios = criterios
        self._tituloValores = tituloValores
        self._valores = valores