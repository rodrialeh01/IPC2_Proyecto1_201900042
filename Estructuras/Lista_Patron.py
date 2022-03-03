#IMPORTANDO EL NODO DE LOS PATRONES Y LA CLASE DE LA LISTA DE CELDAS
from .NodoPatron import NodoPatron
from .Lista_Celdas import Lista_Celdas

#IMPORTANDO LA LIBRERIA OS PARA LAS GRAFICAS DE GRAPHVIZ
import os

#CREANDO VARIABLES GLOBALES PARA LOS REPORTES:
#ESTA VARIABLE ES PARA ALMACENAR EL TEXTO DE LAS INSTRUCCIONES EN EL TXT
contenido = ''
#ESTA VARIABLE ES PARA ALMACENAR EL TEXTO DE LAS INSTRUCCIONES EN EL HTML
contenidoh = ''
#ESTA VARIABLE ES EL COSTO TOTAL DE LA PRODUCCION
CostoT = 0

#CLASE DE LA LISTA DE PATRONES
class Lista_Patron:
    #CONSTRUCTOR
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamaño = 0

    #FUNCION PARA VERIFICAR SI LA LISTA ESTA VACIA
    def Vacio(self):
        return self.cabeza == self.cola == None

    #METODO PARA INSERTAR NODOS POR MEDIO DE LA INSERCION AL FINAL
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

    #METODO PARA MOSTRAR LA LISTA DE PATRONES
    def mostrarLista(self):
        actual = self.cabeza
        for i in range(self.tamaño):
            print('--------------------------------------------------')
            print('Patron No.'+ str(i+1))
            print('Codigo de Patron: ',str(actual.codigo))
            actual.verCelda()
            print('--------------------------------------------------')
            actual = actual.siguiente

    #METODO PARA MOSTRAR EL MENU DE PATRONES
    def MenuPatrones(self):
        Actual = self.cabeza.siguiente
        contador = 1
        while(Actual != None):
            print(str(contador)+'. Realizar las operaciones al Patron Código ' +str(Actual.codigo))
            Actual = Actual.siguiente
            contador +=1

    #METODO PARA RETORNAR LA INFORMACION DEL PATRON POR MEDIO DEL CODIGO
    def retornarInfoPatron(self, puntero):
        actual = self.cabeza
        datos = ''
        for i in range(self.tamaño):
            if ((i+1) == puntero):
                datos += 'Patron Codigo: '+ str(actual.codigo)
                return datos
            actual = actual.siguiente
        return None

    #METODO PARA RETORNAR EL NODO PATRON
    def retornarPatron(self, puntero):
        actual = self.cabeza
        for i in range(self.tamaño):
            if((i+1) == puntero):
                return actual
            actual = actual.siguiente
        return None

    #METODO PARA GRAFICAR EL PRIMER PATRON
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

    #METODO PARA VOLVER A GRAFICAR EL PRIMER PATRON PERO PARA EL REPORTE DE HTML
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


    #METODO PARA GRAFICAR EL RESULTADO DE LAS OPERACIONES DEL PATRON
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

    #METODO PARA GRAFICAR CADA PASO DE LAS OPERACION HECHA CON LOS PATRONES Y ALMACENARLO EN UNA CARPETA PARA EL REPORTE DE HTML
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

    #METODO PARA REALIZAR LAS OPERACIONES DE MOVIMIENTOS DE LAS CELDAS
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
            #MOVIMIENTO A LA DERECHA
            if str(aux2actual.siguiente.color) == str(auxactual.color):
                if str(listaaux.cabeza.color) != str(listaaux.cabeza.siguiente.color):
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
            #MOVIMIENTO HACIA ABAJO
            elif (int(listaaux.cola.fila) > 0 and int(listaaux.cola.columna)> 0):
                aux2 = listaaux.retornarcelda(1,0)
                comparacion = destino.retornarcelda(1,0)
                if str(aux2.color) == str(comparacion.color):                    
                    aux = listaaux.cabeza
                    listaaux.cabeza = aux2
                    aux.anterior = listaaux.cabeza.anterior
                    listaaux.cabeza.anterior.siguiente = aux
                    aux3 = listaaux.cabeza.siguiente
                    listaaux.cabeza.siguiente = aux.siguiente
                    listaaux.cabeza.siguiente.anterior = listaaux.cabeza
                    aux.siguiente = aux3
                    aux3.anterior = aux
                    listaaux.cabeza.anterior = None
                    CostoT += costoi
                    contenido += str(contador) + '. Se intercambiaron de posicion la celda ID ' +str(aux.id)+ ' con la celda ID ' + str(listaaux.cabeza.id) +'. Costo: Q'+ str(float(costoi)) + '\n'
                    contenidoh += '<h3>' + str(contador) + '. Se intercambiaron de posicion la celda ID ' +str(aux.id)+ ' con la celda ID ' + str(listaaux.cabeza.id) +'. Costo: Q'+ str(float(costoi)) + '</h3>\n'
                    self.graficarextra(listaaux,contador)
                    contenidoh += '<h3><center><img src="Images/'+ str(self.cabeza.codigo) +'/_'+str(contador)+'.png"/><center></h3>\n'
                    contador += 1
            #VOLTEAR
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
                    #MOVIMIENTO A LA DERECHA
                    if str(actual.siguiente.color) == str(auxactual.color) and int(actual.siguiente.columna) != 0 and str(actual.color) != str(actual.siguiente.color):
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
                    #MOVIMIENTO HACIA ABAJO
                    elif(str(actual.color) == str(destino.retornarcelda(int(auxactual.fila)+1,int(auxactual.columna)).color)):
                        auxi = actual
                        auxc = listaaux.retornarcelda(int(actual.fila) + 1, int(actual.columna))
                        aux1c = listaaux.retornarcelda(int(actual.fila) + 1, int(actual.columna)).anterior
                        aux2c = listaaux.retornarcelda(int(actual.fila) + 1, int(actual.columna)).siguiente
                        actual = auxc
                        actual.anterior = auxi.anterior
                        actual.siguiente = auxi.siguiente
                        auxi.anterior.siguiente = actual
                        auxi.siguiente.anterior = actual
                        auxi.anterior = aux1c
                        aux1c.siguiente = auxi
                        auxi.siguiente = aux2c
                        if aux2c != None:
                            aux2c.anterior = auxi
                        auxc = auxi
                        CostoT += costoi
                        contenido += str(contador) + '. Se intercambiaron de posicion la celda ID ' +str(auxi.id)+ ' con la celda ID ' + str(actual.id) +'. Costo: Q'+ str(float(costoi)) + '\n'
                        contenidoh += '<h3>' + str(contador) + '. Se intercambiaron de posicion la celda ID ' +str(auxi.id)+ ' con la celda ID ' + str(actual.id) + '. Costo: Q'+ str(float(costoi)) + '</h3>\n'
                        self.graficarextra(listaaux,contador)
                        contenidoh += '<h3><center><img src="Images/'+ str(self.cabeza.codigo) +'/_'+str(contador)+'.png"/><center></h3>\n'
                    #VOLTEAR CELDA
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
                #VOLTEAR CELDA
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
        #MUESTRA LAS CELDAS DEL RESULTADO DEL PATRON DEL PISO
        print('****************************************************')
        print('**            PATRON RESULTADO DEL PISO           **')
        print('****************************************************')
        listaaux.mostrarLista()
        self.graficarpatronfinal(listaaux)   
        
    #METODO PARA MOSTRAR EL LISTADO DE PATRONES
    def mostrarPatrones(self):
        actual = self.cabeza
        while(actual != None):
            print('\t\t>>Código del Patron: ' + str(actual.codigo))
            print('\t\t>>CONTIENE LAS SIGUIENTES CELDAS: ')
            actual.listaceldas.mostrarCeldas()
            print('\t\t*********************************************')
            actual = actual.siguiente

    #METODO PARA EL ORDENAMIENTO DE INSERCION DE PATRONES
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

    #FUNCION PARA EL TAMAÑO DE LA LISTA
    def __len__(self):
        return self.tamaño

#FUNCION PARA RETORNAR EL TEXTO DE LAS INSTRUCCIONES EN TXT
def obtenerInstrucciones():
    global contenido
    return contenido

#FUNCION PARA RETORNAR EL COSTO TOTAL DE LA PRODUCCION
def ObtenerTotal():
    global CostoT
    return CostoT

#FUNCION PARA RETORNAR EL TEXTO DE LAS INSTRUCCIONES EN HTML
def ObtenerInstruccioneshtml():
    global contenidoh
    return contenidoh