#IMPORTANDO LA LISTA DE CELDAS
from .Lista_Celdas import Lista_Celdas

#CLASE NODO PATRON
class NodoPatron():
    #CONSTRUCTOR
    def __init__(self, codigo):
        self.codigo = codigo
        self.listaceldas = Lista_Celdas()
        self.siguiente = None

    #METODO PARA AGREGAR LAS CELDAS A LA LISTA DE CELDAS
    def agregarCeldas(self,id,fila,columna,color):
        self.listaceldas.InsertaralFinal(id,fila,columna,color)

    #METODO PARA CER LA LISTA DE CELDAS
    def verCelda(self):
        self.listaceldas.mostrarLista()