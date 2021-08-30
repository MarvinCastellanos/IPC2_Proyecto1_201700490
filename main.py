from matriz import matrizD
from nodo import punto
from nodoLista import puntoLista
from lista import listaT

import xml.etree.ElementTree as ET


listaTerrenos=listaT()

def cargaXML():
    link=input('Ingrese la ruta del archivo: ')

    tree=ET.parse(link)
    root=tree.getroot()

    for terreno in root:
        matrizTerreno=matrizD()
        nombre=terreno.attrib['nombre']
        for nodo in terreno.findall('posicion'):
            y=nodo.attrib['x']
            x=nodo.attrib['y']
            valor=nodo.text
            matrizTerreno.agregaNodo(punto(int(x),int(y),valor))
        listaTerrenos.agregaTerreno(puntoLista(nombre,matrizTerreno))
        print('Se cargo con exito el terreno :'+nombre+'.')
    print('Terrenos cargados con exito.')

def graficaTerreno():
    print('****************************************')
    print('Ingrese el nombre del terreno: ')
    i=1
    aux=listaTerrenos.getHead()
    if(aux==None):
        print('No hay terrenos cargados')
    else:
        while(True):
            print(str(i)+'. '+aux.getNombre())
            i+=1
            if aux.getSiguiente()==None:
                break
            else:
                aux=aux.getSiguiente()
        txt=input()
        terrenoG=listaTerrenos.buscaTerreno(txt)
        if terrenoG != 0:
            terrenoG.generaGraphviz()

def menu():
    while(True):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('Menu Principal:')
        print('1. Cargar archivo')
        print('2. Procesar archivo')
        print('3. Escribir archivo salida')
        print('4. Mostrar datos del estudiante')
        print('5. Generar Grafica')
        print('6. Salida')

        op=input('Ingrese una opcion: ')

        if op=='1':
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            cargaXML()
        elif op=='2':
            pass
        elif op=='3':
            pass
        elif op=='4':
            print('--------------------------------------------')
            print('Marvin Daniel Castellanos Castillo')
            print('201700490')
            print('Introduccón a la programación y computacion 2 seccion D')
            print('Ingenieria en ciencias y sistemas')
            print('Cuarto semestre')
        elif op=='5':
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            graficaTerreno()
        elif op=='6':
            break
        else:
            print('Opcion invalida, intente de nuevo')

menu()