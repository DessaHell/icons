from PIL import Image, ImageColor
from werkzeug.security import generate_password_hash
import cv2
import numpy as np
import random as rd

def encriptar_nombre(nombre):
    texto_encriptado=generate_password_hash(nombre, 'sha256', 34)
    texto_encriptado.replace('sha256', '')
    lista_texto=list(texto_encriptado)
    lista_codigo=[]
    
    for item in lista_texto:
        if item.isnumeric():
            lista_codigo.append(int(item))
        else:
            item=rd.randint(0,9)
            lista_codigo.append(item)
        
    return lista_codigo  

def crear_matriz(nombre, color):
    img= np.zeros((10,10,3), dtype=np.uint8)
    img.fill(255)
    lista_numerica=encriptar_nombre(nombre)
    lista_agrupada=[lista_numerica[n:n+2] for n in range(0, len(lista_numerica), 2)]
    rgb_color=ImageColor.getrgb(color)
    for axis in lista_agrupada:
        x = int(axis[0])
        y = int(axis[1])
        img[x, y] = [rgb_color[0],rgb_color[1],rgb_color[2]]
    
    res=cv2.resize(img, dsize=(300,300), interpolation=cv2.INTER_NEAREST)
    img= Image.fromarray(res)
    img.show()

nombre=input("Ingrese su nombre: ")
color=input("ingrese color en ingles: ")
crear_matriz(nombre, color)

