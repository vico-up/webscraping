
"""
tareas:
* ver como crear el archivo imagen dentro la carpeta

"""

from email import header
import os
from urllib import request
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
import pandas as pd

#nombreCarpeta = '32323'
#nombreArchivo = nombreCarpeta

categoriaProducto = 'tool-set'
listaImagen = list()
listaProducto = list()

urlCategoria = (f'http://www.tolsentools.com/product-catagories/{categoriaProducto}/page/2/')
r = requests.get(urlCategoria, headers = {'User-Agent': "Chrome/50.0.2661.94"})
html = r.content
soup = BeautifulSoup(html, 'html.parser')
fichaProductos = soup.find_all('div', class_ = 'product-inner clr')

cont = 0

for element in fichaProductos:
    imagenProducto = element.find('img', class_ = 'woo-entry-image-main').get('src')
    nombreProducto = element.find('div', class_ = 'product-details match-height-content').getText('', strip = True)

    #print(imagenProducto)
    #print(nombreProducto)
    #print(type(nombreProducto))
    cont = cont + 1

    img = requests.get(imagenProducto, headers = {"User-Agent": "Chrome/50.0.2661.94"})
    recortarNombre = str(imagenProducto) 
    
    

    caracteres = "http://www.tolsentools.com/wp-content/uploads/jpg"

    recortarNombre = ''.join(x for x in recortarNombre if x not in caracteres)
    nombreImagen = recortarNombre[6:] + " - " + nombreProducto + ".jpg"

    NombreCarpeta = recortarNombre[6:] + " - " + nombreProducto

    try:
        os.mkdir(NombreCarpeta)

        with open(f"{NombreCarpeta}/{nombreImagen}", 'wb') as imagen:
            imagen.write(img.content)


    except OSError:
        print('fallo')

    else:
        print('okis')




    
    #with open(nombreImagen, 'wb') as imagen:
      #  imagen.write(img.content)

#crearDirectorio = f'C:/Users/Victor/OneDrive/Proyectos/Programacion/webscraping whit python/{nombreCarpeta}'



