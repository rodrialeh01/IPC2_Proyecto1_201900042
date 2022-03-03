#IMPORTANDO LA CLASE NODOCELDA
from .NodoCelda import NodoCelda

#CLASE DE LA LISTA DE CELDAS
class Lista_Celdas:
    #CONSTRUCTOR
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    #VERIFICA SI LA LISTA ESTA VACIA
    def Vacio(self):
        return self.cabeza == self.cola == None

    #METODO PARA INSERTAR LAS CELDAS AL FINAL DE LA LISTA
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

    #FUNCION PARA RETORNAR EL TAMAÑO DE LAS FILAS
    def tamañofilas(self):
        return int(self.cola.fila)
    
    #FUNCION PARA RETORNAR EL TAMAÑO DE LAS COLUMNAS
    def tamañocolumnas(self):
        return int(self.cola.columna)

    #FUNCION PARA RETORNAR EL NODO DE CELDA
    def retornarcelda(self, puntero):
        actual = self.cabeza
        for i in range(self.tamaño):
            if((i+1) == puntero):
                return actual
            actual = actual.siguiente
        return None

    #MÉTODO PARA VISUALIZAR LA LISTA DE CELDAS CON UNICAMENTE EL ID Y SU COLOR
    def mostrarLista(self):
        actual = self.cabeza
        for i in range(self.tamaño):
            if actual != None:
                print('ID: ' + str(actual.id) + ' = ' +str(actual.color))
                actual = actual.siguiente

    #MÉTODO PARA MOSTRAR LA LISTA DE CELDAS
    def mostrarCeldas(self):
        actual = self.cabeza
        while(actual != None):
            print('\t\t\t>>> ID:' + str(actual.id))
            print('\t\t\t\t>>> Color: ' + str(actual.color))
            print('\t\t\t\t>>> Fila: ' + str(actual.fila))
            print('\t\t\t\t>>> Columna: ' + str(actual.columna))
            actual = actual.siguiente

    #FUNCON PARA RETORNAR EL NODO DE LA CELDA POR MEDIO DE SU FILA Y COLUMNA
    def retornarcelda(self,fila,columna):
        actual = self.cabeza
        while(actual != None):
            if int(actual.fila) == int(fila) and int(actual.columna) == int(columna):
                return actual
            actual = actual.siguiente

    #METODO PARA EL TAMAÑO DE LA LISTA
    def __len__(self):
        return int(self.tamaño)
