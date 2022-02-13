from Nodo import Nodo
class Lista_Pisos:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    def Vacio(self):
        return self.cabeza == self.cola == None

    def InsertaralFinal(self,data):
        nuevoPiso = Nodo(data)
        if self.Vacio():
            self.cabeza = self.cola = nuevoPiso
        else:
            self.cola.siguiente = nuevoPiso
            self.cola = nuevoPiso
        self.tamaño = self.tamaño +1

    def mostrarLista(self):
        actual = self.cabeza
        while(actual!=None):
            print('Nombre: ',str(actual.data.nombre))
            print('Columna: ',str(actual.data.columna))
            print('Fila: ',str(actual.data.fila))
            print('Costo Voltear: ',str(actual.data.voltear))
            print('Costo Intercambiar: ',str(actual.data.intercambiar))
            print(str(actual.data.patrones.mostrarLista()))
            print('--------------------------------------------------')
            actual = actual.siguiente

    def __len__(self):
        return self.tamaño