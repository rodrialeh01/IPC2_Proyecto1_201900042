from .NodoCelda import NodoCelda
class Lista_Celdas:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    def Vacio(self):
        return self.cabeza == self.cola == None

    def InsertaralFinal(self,fila,columna, color):
        nuevaCelda = NodoCelda(fila,columna,color)
        if self.Vacio():
            self.cabeza = self.cola = nuevaCelda
        elif self.cabeza == self.cola:
            self.cola = nuevaCelda
            self.cabeza.siguiente = self.cola
            self.cola.anterior = self.cabeza            
        else:
            self.cola.siguiente = nuevaCelda
            self.cola = nuevaCelda
            nuevaCelda.anterior = self.cola
        self.tamaño = self.tamaño +1

    def mostrarLista(self):
        actual = self.cabeza
        for i in range(self.tamaño):
            if actual != None:
                print('(' + str(actual.fila) + ',' + str(actual.columna) + ') = ' + str(actual.color))
                #print('Fila: ', str(actual.fila))
                #print('Columna: ', str(actual.columna))
                #print('Color: ', actual.color)
                actual = actual.siguiente
