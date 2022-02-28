from .Lista_Celdas import Lista_Celdas
class NodoPatron():
    def __init__(self, codigo):
        self.codigo = codigo
        self.listaceldas = Lista_Celdas()
        self.siguiente = None

    def agregarCeldas(self,id,fila,columna,color):
        self.listaceldas.InsertaralFinal(id,fila,columna,color)

    def verCelda(self):
        self.listaceldas.mostrarLista()