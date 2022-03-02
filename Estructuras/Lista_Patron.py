from .NodoPatron import NodoPatron
from .Lista_Celdas import Lista_Celdas
import os

contenido = ''
contenidoh = ''
CostoT = 0
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

    #GRAFICA EL PRIMER PATRON
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

    def graficarprimero2(self):
        texto = ''
        try:
            os.mkdir('Images/'+str(self.cabeza.codigo))
        except:
            pass
        file = open('Images/'+str(self.cabeza.codigo)+'/_'+str(0)+'.dot','w')
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
        os.system('dot -Tpng Images/'+str(self.cabeza.codigo)+'/_'+str(0)+'.dot -o Images/'+str(self.cabeza.codigo)+'/_'+str(0)+'.png')


    #GRAFICAR EL PATRON RESULTADO
    def graficarpatronfinal(self,lista):
        texto = ''
        file = open('PatronesGraficados/PatronResultado_'+str(self.cabeza.codigo)+'.dot','w')
        texto += '''digraph structs {
	node [shape=plaintext]
	patron [label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="20">\n'''
        contx = 0
        actual1 = lista.cabeza
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
        os.system('dot -Tpng PatronesGraficados/PatronResultado_'+str(self.cabeza.codigo)+'.dot -o PatronesGraficados/PatronResultado_'+str(self.cabeza.codigo)+'.png')
        rutaa = 'PatronesGraficados\PatronResultado_'+str(self.cabeza.codigo)+'.png'
        os.startfile(rutaa)
        print('Se genero el resultado gráfico del patron')

    def graficarextra(self, lista,n):
        texto = ''
        file = open('Images/'+str(self.cabeza.codigo)+'/_'+str(n)+'.dot','w')
        texto += '''digraph structs {
	node [shape=plaintext]
	patron [label=<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="20">\n'''
        contx = 0
        actual1 = lista.cabeza
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
        os.system('dot -Tpng Images/'+str(self.cabeza.codigo)+'/_'+str(n)+'.dot -o Images/'+str(self.cabeza.codigo)+'/_'+str(n)+'.png')

    def operarPatron(self, puntero,costoi, costov):
        global CostoT
        global contenido
        global contenidoh
        contenido = ''
        destino = self.retornarPatron(puntero).listaceldas
        listaaux = Lista_Celdas()
        nactual = self.cabeza.listaceldas.cabeza 
        #asignando los valores de la lista de celdas inicial a la lista auxiliar
        while nactual != None:
            listaaux.InsertaralFinal(nactual.id,nactual.fila,nactual.columna,nactual.color)
            nactual = nactual.siguiente
        contador = 1
        CostoT = 0
        auxactual = destino.cabeza
        aux2actual = listaaux.cabeza 
        self.graficarprimero2()
        contenidoh = ''
        contenido = ''
        contenidoh+='''<h3><center>Patron Inicial<center></h3>\n'''
        contenidoh+='''<h3><center><img src="Images/'''+ str(self.cabeza.codigo) +'''/_0.png"/><center></h3>\n'''       
        if str(aux2actual.color) != str(auxactual.color):
            if str(aux2actual.siguiente.color) == str(auxactual.color):
                aux = listaaux.cabeza
                listaaux.cabeza = listaaux.cabeza.siguiente
                aux.anterior = listaaux.cabeza
                aux.siguiente = listaaux.cabeza.siguiente
                listaaux.cabeza.siguiente.anterior = aux
                listaaux.cabeza.siguiente = aux
                listaaux.cabeza.anterior = None
                CostoT += costoi
                contenido += str(contador) + '. Se intercambiaron de posicion la celda ID ' +str(aux.id)+ ' con la celda ID ' + str(listaaux.cabeza.id) +'. Costo: Q'+ str(float(costoi)) + '\n'
                contenidoh += '<h3>' + str(contador) + '. Se intercambiaron de posicion la celda ID ' +str(aux.id)+ ' con la celda ID ' + str(listaaux.cabeza.id) +'. Costo: Q'+ str(float(costoi)) + '</h3>\n'
                self.graficarextra(listaaux,contador)
                contenidoh += '<h3><center><img src="Images/'+ str(self.cabeza.codigo) +'/_'+str(contador)+'.png"/><center></h3>\n'
                contador += 1
            else:
                listaaux.cabeza.color = auxactual.color
                CostoT += costov
                if str(listaaux.cabeza.color) == 'W':
                    contenido += str(contador) + '. Se volteó la celda ID ' +str(listaaux.cabeza.id)+ ' de color negro al color blanco' + '. Costo: Q'+ str(float(costov)) + '\n'
                    contenidoh += '<h3>' + str(contador) + '. Se volteó la celda ID ' +str(listaaux.cabeza.id)+ ' de color negro al color blanco' + '. Costo: Q'+ str(float(costov)) + '</h3>\n'
                elif str(listaaux.cabeza.color) ==  'B':
                    contenido += str(contador) + '. Se volteó la celda ID ' +str(listaaux.cabeza.id)+ ' de color blanco al color negro' + '. Costo: Q'+ str(float(costov)) + '\n'
                    contenidoh += '<h3>' + str(contador) + '. Se volteó la celda ID ' +str(listaaux.cabeza.id)+ ' de color blanco al color negro' + '. Costo: Q'+ str(float(costov)) + '</h3>\n'
                self.graficarextra(listaaux,contador)
                contenidoh += '<h3><center><img src="Images/'+ str(self.cabeza.codigo) +'/_'+str(contador)+'.png"/><center></h3>\n'
                contador += 1
        auxactual = auxactual.siguiente
        actual = listaaux.cabeza
        actual = actual.siguiente  
        while actual != None and auxactual != None:
            if str(actual.color) != str(auxactual.color):
                if actual.siguiente != None or auxactual.siguiente != None:
                    if str(actual.siguiente.color) == str(auxactual.color):
                        aux = actual
                        actual = actual.siguiente
                        actual.anterior = aux.anterior
                        aux.anterior.siguiente = actual                        
                        aux.anterior = actual
                        aux.siguiente = actual.siguiente
                        if actual.siguiente != None:
                            actual.siguiente.anterior = aux   
                        actual.siguiente = aux                                             
                        CostoT += costoi
                        contenido += str(contador) + '. Se intercambiaron de posicion la celda ID ' +str(aux.id)+ ' con la celda ID ' + str(actual.id) +'. Costo: Q'+ str(float(costoi)) + '\n'
                        contenidoh += '<h3>' + str(contador) + '. Se intercambiaron de posicion la celda ID ' +str(aux.id)+ ' con la celda ID ' + str(actual.id) + '. Costo: Q'+ str(float(costoi)) + '</h3>\n'
                        self.graficarextra(listaaux,contador)
                        contenidoh += '<h3><center><img src="Images/'+ str(self.cabeza.codigo) +'/_'+str(contador)+'.png"/><center></h3>\n'
                    else:
                        actual.color = str(auxactual.color)
                        CostoT += costov
                        if str(actual.color) == 'W':
                            contenido += str(contador) + '. Se volteó la celda ID ' +str(actual.id)+ ' de color negro al color blanco' + '. Costo: Q'+ str(float(costov)) + '\n'
                            contenidoh += '<h3>' + str(contador) + '. Se volteó la celda ID ' +str(actual.id)+ ' de color negro al color blanco' + '. Costo: Q'+ str(float(costov)) + '</h3>\n'
                            self.graficarextra(listaaux,contador)
                            contenidoh += '<h3><center><img src="Images/'+ str(self.cabeza.codigo) +'/_'+str(contador)+'.png"/><center></h3>\n'
                        elif str(actual.color) ==  'B':
                            contenido += str(contador) + '. Se volteó la celda ID ' +str(actual.id)+ ' de color blanco al color negro' + '. Costo: Q'+ str(float(costov)) + '\n'
                            contenidoh += '<h3>' + str(contador) + '. Se volteó la celda ID ' +str(actual.id)+ ' de color blanco al color negro' + '. Costo: Q'+ str(float(costov)) + '</h3>\n'
                            self.graficarextra(listaaux,contador)
                            contenidoh += '<h3><center><img src="Images/'+ str(self.cabeza.codigo) +'/_'+str(contador)+'.png"/><center></h3>\n'
                    contador += 1
                else:
                    actual.color = str(auxactual.color)
                    CostoT += costov
                    if str(actual.color) == 'W':
                        contenido += str(contador) + '. Se volteó la celda ID ' +str(actual.id)+ ' de color negro al color blanco' + '. Costo: Q'+ str(float(costov)) + '\n'
                        contenidoh += '<h3>' + str(contador) + '. Se volteó la celda ID ' +str(actual.id)+ ' de color negro al color blanco' + '. Costo: Q'+ str(float(costov)) + '</h3>\n'
                        self.graficarextra(listaaux,contador)
                        contenidoh += '<h3><center><img src="Images/'+ str(self.cabeza.codigo) +'/_'+str(contador)+'.png"/><center></h3>\n'
                    elif str(actual.color) ==  'B':
                        contenido += str(contador) + '. Se volteó la celda ID ' +str(actual.id)+ ' de color blanco al color negro' + '. Costo: Q'+ str(float(costov)) + '\n'
                        contenidoh += '<h3>' + str(contador) + '. Se volteó la celda ID ' +str(actual.id)+ ' de color blanco al color negro' + '. Costo: Q'+ str(float(costov)) + '</h3>\n'
                        self.graficarextra(listaaux,contador)
                        contenidoh += '<h3><center><img src="Images/'+ str(self.cabeza.codigo) +'/_'+str(contador)+'.png"/><center></h3>\n'
                    contador += 1
            auxactual = auxactual.siguiente
            actual= actual.siguiente
        print('****************************************************')
        print('**            PATRON RESULTADO DEL PISO           **')
        print('****************************************************')
        listaaux.mostrarLista()
        self.graficarpatronfinal(listaaux)
        #print(self.contenido)        
        
    def mostrarPatrones(self):
        actual = self.cabeza
        while(actual != None):
            print('\t\t>>Código del Patron: ' + str(actual.codigo))
            print('\t\t>>CONTIENE LAS SIGUIENTES CELDAS: ')
            actual.listaceldas.mostrarCeldas()
            print('\t\t*********************************************')
            actual = actual.siguiente

    def ordenamiento(self):
        actual = self.cabeza
        aux = self.cabeza
        if actual.siguiente != None and aux != None:
            i = self.cabeza
            while i != None:
                j = i.siguiente
                while j != None:
                    if(int(ord(i.codigo[0].upper())) > int(ord(j.codigo[0].upper()))):
                        temporal1 = i.codigo
                        temporal2 = i.listaceldas
                        i.codigo = j.codigo
                        i.listaceldas = j.listaceldas
                        j.codigo = temporal1
                        j.listaceldas = temporal2
                    j =j.siguiente
                i = i.siguiente

    def __len__(self):
        return self.tamaño

def obtenerInstrucciones():
    global contenido
    return contenido

def ObtenerTotal():
    global CostoT
    return CostoT

def ObtenerInstruccioneshtml():
    global contenidoh
    return contenidoh