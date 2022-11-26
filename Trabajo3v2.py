# Cargando BeautifulSoap
from bs4 import BeautifulSoup

# Abriendo el archivo index.html alojado en la carpeta docs
with open(r"C:/Users/JaquiChan/Desktop/Ing.Comercial/BIGDATA/Trabajo_Nro1/index.html","r") as doc_html:
    page = BeautifulSoup(doc_html.read(), 'html.parser')

    # revisando el contenido del archivo file
print(f'page: \n{page.prettify()}')

## Ahora vamos a realizar la obtenci+on de datos

############# 1 POR TAG


# Obteniendo el primer elemento de un tag definido
h2_tag = page.h2

# Viendo que tiene la variable h1_tag
print(f'h1_tag:\n{h2_tag}')

# Obteniendo el texto que contiene el tag h1 agregamos a la variable que contiene la informacion la palabra .string
print(f"viendo texto de h1_tag:\n{h2_tag.string}")

############# FORMA FIND 

# buscando por tag usando el find, este devuelve el primer elemento que encuentra
first_h2 = page.find('h2')
print(first_h2)

# obteniendo sólo el texto
print(first_h2.string)


################ CLASS ##################
# Buscando la clase seccion con find
class_seccion = page.find(class_='seccion')
print(class_seccion)


################ ID ##################
# Buscando id header con find
id_header = page.find(id='header')
print(id_header)



########### PARA OBTENER LOS LINKS O ENLACES

all_a = page.find_all('a',href=True)

for a in all_a:
    print(a['href'])

## Obtención de datos por busqueda

import re 

#### Tabla a pandas DataFrame

# Importando Pandas
import pandas as pd


# Busca todos los tag tables contenidos en la página
table = page.find_all('table')

# con read_html lee un texto que este en html
# str() convierte en texto lo que este en table[0]
df = pd.read_html(str(table[0]))[0]



####Abriendo una pagina web

# importando request
import requests

# se define variable con url sólo por orden
url = 'https://www.falabella.com/falabella-cl/category/cat7090034/Tecnologia'

# obtención de la página que se va a analizar
page = requests.get(url)

# Si el codigo es 200 significa que descargo bien
print(f"Codigo: {page.status_code}")

# el contenido de la pagina se encuentra en page.content, y con esto se lee con BeautifulSoap
from bs4 import BeautifulSoup
page = BeautifulSoup(page.content, 'html.parser')
print(page.prettify())



## Analizamos otra pagina web, RIPLEY

# se define variable con url sólo por orden
url = 'https://simple.ripley.cl/zapatos-y-zapatillas/zapatillas/zapatillas-hombre?source=menu&s=mdco'

# obtención de la página que se va a analizar
page = requests.get(url)

# Si el codigo es 200 significa que descargo bien
print(f"Codigo: {page.status_code}")

# el contenido de la pagina se encuentra en page.content, y con esto se lee con BeautifulSoap
from bs4 import BeautifulSoup
page = BeautifulSoup(page.content, 'html.parser')
print(page.prettify())

