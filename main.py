
"""
tareas:
* Insertar detalles a txt

"""

from email import header
import os
from urllib import request
from wsgiref import headers
import requests
from bs4 import BeautifulSoup
import pandas as pd

multi_line_string = """TITULO\n
Precio:\n
Caracateristicas:\n
🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠🛠
📌Para mayor información, consulta por whatsapp:
Catalogo: 
https://wa.me/c/59162722006
https://wa.me/c/59174810534
📲Llamanos al whatsapp: 74810534-62722006\n
Enlaces:\n
Etiquetas herramientas:\n
Tolsen, Herramientas, Construccion, Mecanico, taller, Drywall\n
"""

categoriaProducto = 'tool-set'
contadorPagina = 1
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

    
    #print(type(nombreProducto))
    cont = cont + 1

    img = requests.get(imagenProducto, headers = {"User-Agent": "Chrome/50.0.2661.94"})
    recortarCaracteres = str(imagenProducto)
    recortarCaracteres2 = str(nombreProducto)
    
    
    
    caracteres = "http://www.tolsentools.com/wp-content/uploads/jpg"
    caracteres2 = "/″"

    recortarNombre2 = ''.join(x for x in recortarCaracteres2 if x not in caracteres2)
    recortarNombre = ''.join(x for x in recortarCaracteres if x not in caracteres)
    nombreImagen = recortarNombre[6:] + " - " + recortarNombre2 + ".jpg"

    NombreCarpeta = recortarNombre[6:] + " - " + recortarNombre2

    print(imagenProducto)
    print(recortarNombre2)

    try:
        os.mkdir(f"C:/Users/Victor/OneDrive/ventas/Tolsen/Set de herramientas/{NombreCarpeta}")

        with open(f"C:/Users/Victor/OneDrive/ventas/Tolsen/Set de herramientas/{NombreCarpeta}/{nombreImagen}", 'wb') as imagen:
            imagen.write(img.content)

        with open(f"C:/Users/Victor/OneDrive/ventas/Tolsen/Set de herramientas/{NombreCarpeta}/Detalles.txt", 'w', encoding = 'utf-8') as file:            
            file.write(multi_line_string)

        

    except OSError:
        print('fallo')

    else:
        print('okis')




    
    #with open(nombreImagen, 'wb') as imagen:
      #  imagen.write(img.content)

#crearDirectorio = f'C:/Users/Victor/OneDrive/Proyectos/Programacion/webscraping whit python/{nombreCarpeta}'



