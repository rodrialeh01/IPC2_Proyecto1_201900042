from .NodoPatron import NodoPatron
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

    def MenuPatrones(self):
        Actual = self.cabeza.siguiente
        contador = 1
        while(Actual != None):
            print(str(contador)+'. Patron Código ' +str(Actual.codigo))
            Actual = Actual.siguiente
            contador +=1

    def retornarInfoPatron(self, puntero):
        actual = self.cabeza
        datos = ''
        for i in range(self.tamaño):
            if ((i+1) == puntero):
                datos += 'Patron Codigo: '+ str(actual.codigo)
                return datos
            actual = actual.siguiente
        return None

    def retornarPatron(self, puntero):
        actual = self.cabeza
        for i in range(self.tamaño):
            if((i+1) == puntero):
                return actual
            actual = actual.siguiente
        return None

    def __len__(self):
        return self.tamaño