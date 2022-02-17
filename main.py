import tkinter as tk
from tkinter import filedialog
from xml.etree import ElementTree as et

from Lista_Pisos import Lista_Pisos
LP = Lista_Pisos()

#ABRIENDO EL ARCHIVO Y VER SU CONTENIDO
def AbrirArchivo(ruta):
    global LP
    if ruta !="":
        archivo1 =  et.parse(ruta)
        root = archivo1.getroot()
        #print(root)    
        
        for element in root:
            #print(element.attrib)
            nombre = element.attrib.get('nombre')
            r = element[0].text.strip()
            c = element[1].text.strip()
            f = element[2].text.strip()
            s = element[3].text.strip()
            LP.InsertaralFinal(nombre,r,c,f,s)      
            for subelement in element:
                if subelement.tag == "patrones":
                    for subsubelement in subelement:
                        np = subsubelement.attrib.get('codigo').strip()
                        pp = subsubelement.text.strip()
                        LP.cola.agregarPatron(np)
                        for i in range(int(r)):
                            for j in range(int(c)):
                                LP.cola.agregarCelda(i,j,pp[j+(i*int(c))])      
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