#IMPORTAR LA LISTA DE PATRONES
from .Lista_Patron import Lista_Patron

#CLASE DEL NODO DE PISO
class NodoPiso():
    #CONSTRUCTOR
    def __init__(self, nombre, fila, columna,costovoltear, costointercambiar):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna
        self.costovoltear = costovoltear
        self.costointercambiar = costointercambiar
        self.listapatrones = Lista_Patron()
        self.siguiente = None
    
    #METODO PARA INSERTAR UN PATRON A LA LISTA DE PATRONES
    def agregarPatron(self,codigo):
        self.listapatrones.InsertaralFinal(codigo)

    #METODO PARA AGREGAR LAS CELDAS A LA LISTA DE CELDAS
    def agregarCelda(self,id,fila,columna,color):
        self.listapatrones.cola.listaceldas.InsertaralFinal(id,fila,columna,color)

    #METODO PARA MOSTRAR LA LISTA DE PATRONES
    def verPatron(self):
        self.listapatrones.mostrarLista()
