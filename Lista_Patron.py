from Nodo import Nodo
class Lista_Patron:
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
        self.tamaño = self.tamaño+1

    def mostrarLista(self):
        actual = self.cabeza
        print('Hay ', self.tamaño, ' patrones')
        for i in range(self.tamaño):
            print('Nombre Patron: ',str(actual.data.nombre))
            print('Patron: ',str(actual.data.patron))
            print('--------------------------------------------------')
            actual = actual.siguiente

    def __len__(self):
        return self.tamaño