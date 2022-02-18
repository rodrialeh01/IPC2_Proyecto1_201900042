from ast import Break, Return
from .NodoPiso import NodoPiso
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

    def menuPisos(self):
        Actual = self.cabeza
        contador = 1
        print('====================================================')
        print('==                   MENÚ PISOS                   ==')
        print('====================================================')
        while(Actual != None):
            print(str(contador)+'. Piso '+str(Actual.nombre))
            Actual = Actual.siguiente
            contador +=1

    def retornarInfoPiso(self, puntero):
        actual = self.cabeza
        datos = ''
        for i in range(self.tamaño):
            if ((i+1) == puntero):
                datos += 'Fila: '+ str(actual.fila) + '\n'+ 'Columna: '+ str(actual.columna) + '\n' + 'Costo Voltear: '+ str(actual.costovoltear) + '\n' + 'Costo Intercambiar: '+str(actual.costointercambiar)
                return datos
            actual = actual.siguiente
        return None
        
    def retornarPiso(self, puntero):
        actual = self.cabeza
        for i in range(self.tamaño):
            if((i+1) == puntero):
                return actual
            actual = actual.siguiente
        return None

    def __len__(self):
        return self.tamaño