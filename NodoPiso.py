from Lista_Patron import Lista_Patron
class NodoPiso():
    def __init__(self, nombre, fila, columna,costovoltear, costointercambiar):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.costovoltear = costovoltear
        self.costointercambiar = costointercambiar
        self.listapatrones = Lista_Patron()
        self.siguiente = None
    
    def agregarPatron(self,codigo):
        self.listapatrones.InsertaralFinal(codigo)

    def agregarCelda(self,fila,columna,color):
        self.listapatrones.cola.listaceldas.InsertaralFinal(fila,columna,color)

    def verPatron(self):
        self.listapatrones.mostrarLista()
