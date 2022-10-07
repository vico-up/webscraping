#Creo que la clave esta en que 2 funciones me devuelvav los nombre y otras que me creen las rutas


import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def nombreCarpeta():
    for element in titulo:
        titulito = element.find('h1', class_= "product_title entry-title single-post-title").getText('', strip = True)
    
        recortarCaracteres =  str(titulito)
        eliminarCaracteres = "/″"
        nombreCarpeta = ''.join(x for x in recortarCaracteres if x not in eliminarCaracteres)
        return nombreCarpeta

def nombreFoto():
    for element in fichaProductos2:
        foto = element.find('img', class_ = 'attachment-shop_single size-shop_single wp-post-image').get('src')
        recortarCaracteres = str(foto)
        caracteres = "http://www.tolsentools.com/wp-content/uploads/jpg"
        recortarNombre = ''.join(x for x in recortarCaracteres if x not in caracteres)
        nombreImagen = recortarNombre[6:]
        return nombreImagen

def crearCarpeta(nueva_ruta):
    rutaFoto = f"{nueva_ruta}/{nombresitoFoto} - {nombresitoCarpeta}"
    try:
        os.mkdir(rutaFoto, mode=0o777)
    except OSError:
        print('fallo')   
    else:
        print('okis')
    return rutaFoto

        
def crearFoto():
    for element in fichaProductos2:
        foto = element.find('img', class_ = 'attachment-shop_single size-shop_single wp-post-image').get('src')
        img = requests.get(foto, headers = {"User-Agent": "Chrome/50.0.2661.94"})
    
    with open(f"{rutaCarpetita}/{nombresitoFoto}.jpg", 'wb') as imagen:
        imagen.write(img.content)

def leerDatosHerramienta():
    for element in leerDatosHe:
        datitos = element.find('p').getText('', strip = True)       
        datosStr = str(datitos)
        return datosStr
        



direccionMadre = "C:/Users/Victor/OneDrive/ventas/Tolsen/Set de herramientas"
categoriaProducto = 'tool-set'

urlCategoria = (f'http://www.tolsentools.com/product-catagories/{categoriaProducto}/page/2/')
r = requests.get(urlCategoria, headers = {'User-Agent': "Chrome/50.0.2661.94"})
html = r.content
soup = BeautifulSoup(html, 'html.parser')
fichaProductos = soup.find_all('div', class_ = 'product-inner clr')

cont = 0

for element in fichaProductos:
    enlace = element.find('a', class_ = 'woocommerce-LoopProduct-link woocommerce-loop-product__link').get('href')
    r2 = requests.get(enlace, headers={'User-Agent': "Chrome/50.0.2661.94"})
    html2 = r2.content
    soup2 = BeautifulSoup(html2, 'html.parser')
    titulo = soup2.find_all("div", class_= "summary entry-summary")
    fichaProductos2 = soup2.find_all('div', class_ = "woocommerce-product-gallery__image")
    
    enlace2 = element.find('div', class_ = 'woocommerce-LoopProduct-link woocommerce-loop-product__link')
    r3 = requests.get(enlace, headers={'User-Agent': "Chrome/50.0.2661.94"})
    html3 = r3.content
    soup3 = BeautifulSoup(html3, 'html.parser')
    leerDatosHe = soup3.find_all('div', class_ = "woocommerce-product-details__short-description")
    
    nombresitoCarpeta = nombreCarpeta()
    nombresitoFoto = nombreFoto()
    #rutaCarpetita = crearCarpeta(direccionMadre)
    #crearFoto()
    datitosHerramientas = leerDatosHerramienta()
    print(type(datitosHerramientas))
    
    
    cont = cont + 1 
    






























'''from msilib.schema import File

import os
from statistics import mode
import emoji
import unicodedata

categoria = "set-electricos3"

nombresito = "pruebita32"
rutaMadre = f"C:/Users/Victor/OneDrive/ventas/Tolsen/{categoria}"

emojiw = "🛠🛠"

try:
    os.mkdir(f"{rutaMadre}", mode=0o777)
    os.mkdir(f"{rutaMadre}/{nombresito}", mode=0o777)
    #with open(f"C:/Users/Victor/OneDrive/ventas/Tolsen/{categoria}/{nombresito}/detallitos.txt", "w", encoding = 'utf-8') as file:
     #   file.write(emojiw)

except OSError:
    print('fail')

else:
    print("okiii")

'''