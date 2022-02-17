from NodoPiso import NodoPiso
class Lista_Pisos:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    def Vacio(self):
        return self.cabeza == self.cola == None

    def InsertaralFinal(self,nombre,fila,columna, f,s):
        nuevoPiso = NodoPiso(nombre,fila,columna,f,s)
        if self.Vacio():
            self.cabeza = self.cola = nuevoPiso
        elif self.cabeza == self.cola:
            self.cola = nuevoPiso
            self.cabeza.siguiente = self.cola                        
        else:
            self.cola.siguiente = nuevoPiso
            self.cola = nuevoPiso
        self.tamaño = self.tamaño +1

    def mostrarLista(self):
        Actual = self.cabeza
        while(Actual != None):
            #print('Piso No. ' + str(i+1))
            print('Nombre: ',str(Actual.nombre))
            print('Fila: ',str(Actual.fila))
            print('Columna: ',str(Actual.columna))
            print('Costo Voltear: ',str(Actual.costovoltear))
            print('Costo Intercambiar: ',str(Actual.costointercambiar))
            print('--------------------------------------------------')
            Actual.verPatron()
            Actual = Actual.siguiente


    def __len__(self):
        return self.tamaño