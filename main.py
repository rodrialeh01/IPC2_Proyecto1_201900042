import tkinter as tk
from tkinter import filedialog
from lxml import etree as xp
from xml.etree import ElementTree as et

from Lista_Pisos import Lista_Pisos
from Piso import Piso
from Lista_Patron import Lista_Patron
from Patron import Patron

#ABRIENDO EL ARCHIVO Y VER SU CONTENIDO
def AbrirArchivo(ruta):
    if ruta !="":
        archivo1 =  et.parse(ruta)
        root = archivo1.getroot()
        print(root)

        LP = Lista_Pisos()        
        
        for element in root:
            print(element.attrib)
            nombre = element.attrib.get('nombre')
            r = element[0].text
            c = element[1].text
            f = element[2].text
            s = element[3].text  
            L = Lista_Patron()          
            for subelement in element:
                if subelement.tag == "patrones":
                    for subsubelement in subelement:
                        print(subsubelement.tag, ' ', subsubelement.attrib, ' : ', subsubelement.text)
                        np = subsubelement.attrib.get('codigo')
                        pp = subsubelement.text
                        L.InsertaralFinal(Patron(np,pp))
                else:
                    #fila = subelement.text[0]
                    #columna = subelement.text[1]
                    #f = subelement.text[2]
                    #s = subelement.text[3]
                    #nuevo = Piso(nombre, fila, columna,f,s,'p')
                    #L.InsertaralFinal(nuevo)
                    print(subelement.tag, ' : ',subelement.text)
            LP.InsertaralFinal(Piso(nombre,r,c,f,s,L))

        LP.mostrarLista()

    else:
        print('== NO SE CARGÓ NINGUN ARCHIVO                     ==')

#OBTENER LA RUTA DEL ARCHIVO
def ruta():
    root = tk.Tk()
    root.withdraw()
    ruta =  filedialog.askopenfilename(title='Cargar Archivo', filetypes = (("Text files", "*.xml*"), ("all files", "*.*")))
    return ruta

#MENU PRINCIPAL
def menu():
    opcion = 0
    Ruta = ""
    while opcion!=3:
        print('====================================================')
        print('==                  CERAMICA-BOT                  ==')
        print('== Introducción a la Programación y Computación 2 ==')
        print('==                     MENU                       ==')
        print('== 1. Cargar Archivo XML                          ==')
        print('== 2. Procesar Archivo                            ==')
        print('== 3. Salir                                       ==')
        print('====================================================')
        try:
            opcion = int(input('== Elija una opción:                              ==\n>'))
            if opcion == 1:
                try:
                    Ruta = ruta()
                    if Ruta !="":
                        print('== Ruta: ', str(Ruta))
                        print('== EL ARCHIVO SE CARGO CON EXITO                  ==')
                    else:
                        print('== NO SE CARGÓ NINGUN ARCHIVO                     ==')
                except:
                    print('== NO SE PUDO CARGAR EL ARCHIVO                   ==')
            elif opcion == 2:
                AbrirArchivo(Ruta)
            elif opcion == 3:
                print('== ADIOS, VUELVE PRONTO                           ==')
            else:
                print('\n== OPCION INVALIDA                                ==')
        except:
            print('\n== OPCION INVALIDA                                ==')

menu()