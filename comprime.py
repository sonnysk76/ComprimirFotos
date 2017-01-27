#!/usr/bin/python3.5

'''
Compresion de imagenes personalizado v0.1
Python 3.5x
Sirve para comprimir imagenes .bmp capturadas por sistema de inspeccion
Cada dia se guardan las imagenes en una carpeta con la siguiente estructura
/fecha en numero/nombre de la inspeccion/imagen ext .bmp
/170120/Left Fender Badge/Left_Fender_Badge_170120_023427_GG258425_FAIL.bmp

Va leyendo los archivos de cada directorio, y los guarda comprimidos x10 en el
mismo directorio, agregando "r " al inciio del nombre

Parametros.
direc:
Lee la ubicacion de directorio de seis posiciones
subdirs: (interno)
Lista con los nombres de los subdirectorios de las inspecciones.

'''

import os
from PIL import Image

def lee_archivos(directorio, subdirs):
    file_list = []
    listado = []
    os.chdir(directorio+subdirs)
    curdir = os.getcwd()
    file_list =(os.listdir(curdir))
    for file in file_list:
        if file.endswith('.bmp'):
            listado.append(file)
    return listado

def reducir(imgList):

    for imagen in imgList:
        img = Image.open(imagen)
        nombre = str(imagen)
        img = img.resize((421,322),Image.ANTIALIAS)
        img.save(('r '+ nombre), quality = 100, dpi=(72,72), optimize = True)


# Funcion principal
def Main(subd):
    direc = input('Escribe el directorio de las imagenes ej.(170120): ')
    direc = 'C:/Images/'+str(direc)+'/'
    for i in range (len(subd)):
        archivos = lee_archivos(direc, subd[i])
        print (os.getcwd())
        print(archivos)
        reducir(archivos)



if __name__ == "__main__":
    #Lista de subcarpetas a explorar por imagenes .bmp
    subdirs = [' vision',
               ' archivos',
               ' machine']
    Main(subdirs)



'''
archivos = lee_archivos(direc, subdirs)
print(archivos)

input('Presione una tecla para salir')
    subdirs = ['Bedliner',
           'Center Tailgate',
           'Left B Pillar',
           'Left Body Side Molding',
           'Left Door Badge',
           'Left Fender Badge',
           'Left Front Wheel',
           'Left Head Lamp',
           'Left Mirror',
           'Left Rear Wheel',
           'Left Side Step',
           'Left Tail Lamp',
           'Left Tailgate',
           'Left Tow Hook',
           'Left Wheel Spats',
           'Overview',
           'Rear Glass',
           'Rear Overview',
           'Right B Pillar',
           'Right Body Side Molding',
           'Right Door Badge',
           'Right Fender Badge',
           'Right Front Wheel',
           'Right Head Lamp',
           'Right Mirror',
           'Right Rear Wheel',
           'Right Side Step',
           'Right Tail Lamp',
           'Right Tailgate',
           'Right Tow Hook',
           'Right Wheel Spats']
'''