import requests
from bs4 import BeautifulSoup
import pandas as pd

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
    fichaProductos2 = soup2.find_all('div', class_ = "woocommerce-product-gallery__image")

    cont2 = 0

    for element in fichaProductos2:
        foto = element.find('img', class_ = 'attachment-shop_single size-shop_single wp-post-image').get('src')

        cont2 = cont2 + 1
        img = requests.get(foto, headers = {"User-Agent": "Chrome/50.0.2661.94"})

    cont = cont + 1 
    print(img)


























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