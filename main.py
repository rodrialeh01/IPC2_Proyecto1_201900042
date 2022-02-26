import tkinter as tk
from tkinter import filedialog
from xml.etree import ElementTree as et

from Estructuras.Lista_Pisos import Lista_Pisos
ListaPisos = Lista_Pisos()

#ABRIENDO EL ARCHIVO Y VER SU CONTENIDO
def AbrirArchivo(ruta):
    global ListaPisos
    if ruta !="":
        try:
            #USAMOS ELEMENT-TREE PARA ANALIZAR EL ARCHIVO Y SACAR SUS DATOS
            archivo1 =  et.parse(ruta)
            root = archivo1.getroot()            
            for element in root:
                nombre = element.attrib.get('nombre')
                r = element[0].text.strip()
                c = element[1].text.strip()
                f = element[2].text.strip()
                s = element[3].text.strip()
                ListaPisos.InsertaralFinal(nombre,r,c,f,s)      
                for subelement in element:
                    if subelement.tag == "patrones":
                        for subsubelement in subelement:
                            np = subsubelement.attrib.get('codigo').strip()
                            pp = subsubelement.text.strip().upper()
                            ListaPisos.cola.agregarPatron(np)
                            for i in range(int(r)):
                                for j in range(int(c)):
                                    ListaPisos.cola.agregarCelda(i,j,pp[j+(i*int(c))].strip())      
            MenuPisos()
        except:
            print('== ERROR EN EL ARCHIVO                            ==')
    else:
        print('== NO SE CARGÓ NINGUN ARCHIVO                     ==')

#METODO PARA MOSTRAR EL MENU DE PISOS
def MenuPisos():
    global ListaPisos
    opcion = 0
    while opcion != (len(ListaPisos)+1):
        try:
            ListaPisos.menuPisos()
            print(str(len(ListaPisos)+1)+'. Salir al Menú Principal')
            opcionp = int(input('== Elija una opción:                              ==\n>'))
            if ListaPisos.retornarInfoPiso(opcionp) != None:
                MenuPatrones(opcionp)
            elif opcionp == (len(ListaPisos)+1):
                break
            else:
                print('\n== OPCION INVALIDA                                ==')
        except:
            print('\n== OPCION INVALIDA                                ==')

#METODO PARA EL MENÚ DE PATRONES
def MenuPatrones(npiso):
    global ListaPisos
    opcionp = 0
    patroni = None
    while(opcionp != (len(ListaPisos.retornarPiso(npiso).listapatrones)+1)):
        try:
            if ListaPisos.retornarPiso(npiso) != None:
                print('====================================================')
                print('==             PATRON INICIAL DEL PISO            ==')
                print('====================================================')
                patroni = ListaPisos.retornarPiso(npiso).listapatrones.retornarPatron(1)
                MostrarCeldas(patroni)
                print('====================================================')
                print('==        MENÚ DE OPERACIONES DE PATRONES         ==')
                print('====================================================')
                ListaPisos.retornarPiso(npiso).listapatrones.MenuPatrones()
                print(str(len(ListaPisos.retornarPiso(npiso).listapatrones))+'. Graficar el patrón inicial')
                print(str(len(ListaPisos.retornarPiso(npiso).listapatrones)+1)+'. Salir al Menú de Pisos')
                opcionp2 = int(input('== Elige tu patrón destino o una opcion:          ==\n>'))
                if ListaPisos.retornarPiso(npiso).listapatrones.retornarPatron(opcionp2+1) != None:
                    patronf = ListaPisos.retornarPiso(npiso).listapatrones.retornarPatron(opcionp2+1)
                    MostrarCeldas(patronf)
                    MenuOperaciones(npiso,opcionp2+1)
                elif opcionp2 == len(ListaPisos.retornarPiso(npiso).listapatrones):
                    ListaPisos.retornarPiso(npiso).listapatrones.graficarprimero()
                elif opcionp2 ==(len(ListaPisos.retornarPiso(npiso).listapatrones)+1):
                    break
                else:
                    print('\n== OPCION INVALIDA                                ==')
            elif opcionp == (len(ListaPisos.retornarPiso(npiso).listapatrones)):
                break
            else:
                print('\n== OPCION INVALIDA                                ==')
        except:
            print('\n== OPCION INVALIDA                                ==')

#METODO PARA MOSTRAR EL PATRON DE CELDAS
def MostrarCeldas(patron):
    patron.verCelda()

#MENU DE OPERACIONES
def MenuOperaciones(npiso,of):
    global ListaPisos
    opcion = 0
    while opcion != 3:
        print('====================================================')
        print('== 1. Mostrar graficamente el patron inicial      ==')
        print('== 2. Cambiar el patron inicial al patron destino ==')
        print('== 3. Salir                                       ==')
        print('====================================================')
        opcion = int(input('== Elija una opción:                              ==\n>'))
        if opcion == 1:
            ListaPisos.retornarPiso(npiso).listapatrones.graficarprimero()
        elif opcion == 2:
            ListaPisos.retornarPiso(npiso).listapatrones.operarPatron(of)
        elif opcion == 3:
            break
        else:
            print('\n== OPCION INVALIDA                                ==')


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