
"""
tareas:
* la lista guarda todos las caracteristicas de varias herramientas 
    solucionar y poner saltos de linea

"""
from turtle import ScrolledCanvas
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
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

def tituloDetalles():
    for element in titulo:
        titulito = element.find('h1', class_= "product_title entry-title single-post-title").getText('', strip = True)
        return titulito

def crearArchivo():
    with open(f"{rutaCarpetita}/detalles.txt", "a", encoding="UTF-8") as file:
        file.write(f"{tituloEsp}")
        file.write(f"{listaDetallesHerram}")

def leerDatosHerramienta():
    for element in titulo:
        datitos = element.find('p').getText('', strip = True)       
        return datitos


multi_line_string = """\n
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
traducirTitulo = None
datitosHerramienta = None
listaDetallesHerram = []
tituloEsp = None
translator = Translator()

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
    datosHerramienta = soup2.find_all('div', class_ = "woocommerce-product-details__short-description")
    nombresitoCarpeta = nombreCarpeta()
    nombresitoFoto = nombreFoto()
    rutaCarpetita = crearCarpeta(direccionMadre)
    crearFoto()
    titulitoDetalles = tituloDetalles()
    traducirTitulo = translator.translate(f'{titulitoDetalles}', src='en', dest='es')
    tituloEsp = traducirTitulo.text
    datitosHerramienta = leerDatosHerramienta()
    listaDetallesHerram.append(datitosHerramienta)
    crearArchivo()
    print(listaDetallesHerram)

    cont = cont + 1 
    



