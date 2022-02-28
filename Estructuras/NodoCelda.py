class NodoCelda():
    def __init__(self,id, fila, columna, color):
        self.id = id
        self.fila = fila
        self.columna = columna
        self.color = color
        self.siguiente = None
        self.anterior = None