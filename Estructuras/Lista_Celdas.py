from .NodoCelda import NodoCelda
class Lista_Celdas:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    def Vacio(self):
        return self.cabeza == self.cola == None

    def InsertaralFinal(self,id,fila,columna, color):
        nuevaCelda = NodoCelda(id,fila,columna,color)
        if self.Vacio():
            self.cabeza = self.cola = nuevaCelda
        elif self.cabeza == self.cola:
            self.cola = nuevaCelda
            self.cabeza.siguiente = self.cola
            self.cola.anterior = self.cabeza            
        else:
            self.cola.siguiente = nuevaCelda
            nuevaCelda.anterior = self.cola            
            self.cola = nuevaCelda            
        self.tamaño = self.tamaño +1

    def tamañofilas(self):
        return int(self.cola.fila)
    
    def tamañocolumnas(self):
        return int(self.cola.columna)

    def retornarcelda(self, puntero):
        actual = self.cabeza
        for i in range(self.tamaño):
            if((i+1) == puntero):
                return actual
            actual = actual.siguiente
        return None

    def mostrarLista(self):
        actual = self.cabeza
        for i in range(self.tamaño):
            if actual != None:
                print('ID: ' + str(actual.id) + ' = ' +str(actual.color))
                #print('Fila: ', str(actual.fila))
                #print('Columna: ', str(actual.columna))
                #print('Color: ', actual.color)
                actual = actual.siguiente

    def mostrarCeldas(self):
        actual = self.cabeza
        while(actual != None):
            print('\t\t\t>>> ID:' + str(actual.id))
            print('\t\t\t\t>>> Color: ' + str(actual.color))
            print('\t\t\t\t>>> Fila: ' + str(actual.fila))
            print('\t\t\t\t>>> Columna: ' + str(actual.columna))
            actual = actual.siguiente

    def __len__(self):
        return int(self.tamaño)
