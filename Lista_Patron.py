from NodoPatron import NodoPatron
class Lista_Patron:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    def Vacio(self):
        return self.cabeza == self.cola == None

    def InsertaralFinal(self,codigo):
        nuevoPatron = NodoPatron(codigo)
        if self.Vacio():
            self.cabeza = self.cola = nuevoPatron
        elif self.cabeza == self.cola:
            self.cola = nuevoPatron
            self.cabeza.siguiente = self.cola            
        else:
            self.cola.siguiente = nuevoPatron
            self.cola = nuevoPatron
        self.tamaño = self.tamaño+1

    def mostrarLista(self):
        actual = self.cabeza
        for i in range(self.tamaño):
            print('--------------------------------------------------')
            print('Patron No.'+ str(i+1))
            print('Codigo de Patron: ',str(actual.codigo))
            actual.verCelda()
            print('--------------------------------------------------')
            actual = actual.siguiente


    def __len__(self):
        return self.tamaño