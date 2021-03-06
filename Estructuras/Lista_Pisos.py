#IMPORTANDO EL NODO PISO
from .NodoPiso import NodoPiso

#CLASE DE LISTA DE PISO
class Lista_Pisos:
    #CONSTRUCTOR
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    #FUNCION PARA VERIFICAR SI ESTA VACIA LA LISTA
    def Vacio(self):
        return self.cabeza == self.cola == None

    #METODO PARA INSERTAR UN NUEVO NODO A LA LISTA
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

    #METODO PARA MOSTRAR LA LISTA DE PISOS
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

    #METODO PARA MOSTRAR EL MENU DE PISOS
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

    #FUNCION PARA RETORNAR LOS DATOS DEL PISO
    def retornarInfoPiso(self, puntero):
        actual = self.cabeza
        datos = ''
        for i in range(self.tamaño):
            if ((i+1) == puntero):
                datos += 'Fila: '+ str(actual.fila) + '\n'+ 'Columna: '+ str(actual.columna) + '\n' + 'Costo Voltear: '+ str(actual.costovoltear) + '\n' + 'Costo Intercambiar: '+str(actual.costointercambiar)
                return datos
            actual = actual.siguiente
        return None

    #FUNCION PARA RETORNAR EL NODO        
    def retornarPiso(self, puntero):
        actual = self.cabeza
        for i in range(self.tamaño):
            if((i+1) == puntero):
                return actual
            actual = actual.siguiente
        return None

    #METODO PARA ORDENAR LA LISTA EN ORDEN ALFABETICO POR MEDIO DEL ORDENAMIENTO BURBUJA
    def ordenamiento(self):
        actual = self.cabeza
        aux = self.cabeza
        if actual.siguiente != None and aux != None:
            i = self.cabeza
            while i != None:
                j = i.siguiente
                while(j != None):
                    if int(ord(i.nombre[0].upper())) > int(ord(j.nombre[0].upper())):
                        temporal1 = i.nombre
                        temporal2 = i.fila
                        temporal3 = i.columna
                        temporal4 = i.costointercambiar
                        temporal5 = i.costovoltear
                        temporal6 = i.listapatrones
                        i.nombre = j.nombre
                        i.fila = j.fila
                        i.columna = j.columna
                        i.costointercambiar = j.costointercambiar
                        i.costovoltear = j.costovoltear
                        i.listapatrones = j.listapatrones
                        j.nombre = temporal1
                        j.fila = temporal2
                        j.columna = temporal3
                        j.costointercambiar = temporal4
                        j.costovoltear = temporal5
                        j.listapatrones = temporal6
                    j = j.siguiente
                i = i.siguiente

    #METODO PARA ORDENAR LOS PATRONES EN ORDEN ALFABETICO
    def ordenarlistapatrones(self, puntero):
        actual = self.retornarPiso(puntero)
        actual.listapatrones.ordenamiento()

    #METODO PARA MOSTRAR LOS PISOS
    def mostrarPisos(self):
        actual = self.cabeza
        while(actual != None):
            print('========================================================================')
            print('>Nombre del Piso: ' + str(actual.nombre))
            print('\t>Cantidad de Filas: ' + str(actual.fila))
            print('\t>Cantidad de columnas: ' + str(actual.columna))
            print('\t>Costo de Intercambio de celdas: Q'+ str(float(actual.costointercambiar)))
            print('\t>Costo de volteo de celdas: Q' + str(float(actual.costovoltear)))
            print('\t>CONTIENE LOS SIGUIENTES PATRONES:')
            actual.listapatrones.mostrarPatrones()
            actual = actual.siguiente

    #FUNCION PARA MOSTRAR LA LONGITUD DE LA LISTA
    def __len__(self):
        return self.tamaño