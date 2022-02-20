from .NodoPatron import NodoPatron
import os
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
            print(str(contador)+'. Realizar las operaciones al Patron Código ' +str(Actual.codigo))
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

    def graficarprimero(self):
        texto = ''
        file = open('PatronesGraficados/Patron_'+str(self.cabeza.codigo)+'.dot','w')
        texto += '''digraph structs {
	node [shape=plaintext]
	patron [label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="20">\n'''
        contx = 0
        actual1 = self.cabeza.listaceldas.cabeza
        while(contx <=self.cabeza.listaceldas.tamañofilas()):
            texto += '''<TR>\n'''
            conty = 0
            while(conty <=self.cabeza.listaceldas.tamañocolumnas()):
                if actual1.color == 'W':
                    texto += '''<TD></TD>\n'''
                elif actual1.color == 'B':
                    texto += '''<TD bgcolor="black"></TD>\n'''
                conty += 1
                actual1 = actual1.siguiente
            texto += '''</TR>'''
            contx +=1
        texto += '''</TABLE>>]
}'''
        file.write(texto)
        file.close()
        os.system('dot -Tpng PatronesGraficados/Patron_'+str(self.cabeza.codigo)+'.dot -o PatronesGraficados/Patron_'+str(self.cabeza.codigo)+'.png')
        rutaa = 'PatronesGraficados\Patron_'+str(self.cabeza.codigo)+'.png'
        os.startfile(rutaa)
        print('Grafica del patron inicial generada con exito')

    def __len__(self):
        return self.tamaño