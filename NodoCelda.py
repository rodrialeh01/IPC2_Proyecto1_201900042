class NodoCelda():
    def __init__(self, fila, columna, color):
        self.fila = fila
        self.columna = columna
        self.color = color
        self.siguiente = None
        self.anterior = None