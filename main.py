import hashlib
import time
from api.service_api import getAll,getCountry,getLanguage
import pandas as pd
import traceback
from db.service_db import ConexionDB

####Punto 1 obtener todas las regiones existentes

#Se obtiene toda la informacion obtenida de la api en un json
json_all=getAll()
#Se lee el json con pandas para convertirlo en un data frame  el cual se asigna ala variable df
df=pd.read_json(json_all)
#Se agrupa el df en por region
df=df.groupby("region").sum()
#Se obtiene los nombres de las regiones como una lista
regiones=df.index.values.tolist()
#Se eliminar valores vacios de la lista de regiones ['', 'Africa', 'Americas', 'Asia', 'Europe', 'Oceania', 'Polar']
regiones.remove("")

###Punto 2 obtenga un pais por region apartir de la region optenida del punto 1
###Punto 3 obtenga el nombre del idioma que habla el pais y encriptelo con SHA1

#Se crea un diccionario vacio donde se van almacenar Region,pais,idioman y tiempo
diccionario={}
#Se empieza a iterar cada region
for region in regiones:
    try:
        #Se inicializa una variable con el tiempo actual
        start_time = time.time()
        #Se obtiene un pais al azar dependiendo de la region
        country=getCountry(region)
        #Se ingresa al diccionario los valores de region,pais,idioma y tiempo
        diccionario[region]={
                'Country':country,
                'Languaje': hashlib.sha1(getLanguage(country).encode('UTF-8')).hexdigest(),
                #Punto 4 en la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
                'Time':time.time()-start_time
        }
    except Exception as e:
        print(f"Error en region {region}:{e}")
        print(f"Detalle de error", traceback.format_exc())


#Punto 5 la tabla debe ser creada en un DataFrame con la libreria PANDAS
#Se convierte el diccionario en un Data Frame

df = pd.DataFrame([key for key in diccionario.keys()], columns=['Region'])
df['Country'] = [value['Country'] for value in diccionario.values()]
df['Languaje'] = [value['Languaje'] for value in diccionario.values()]
df['Time'] = [value['Time'] for value in diccionario.values()]
print("#################### Tabla Data Frame ####################")
print(df)
#Punto 6 Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio,
# el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla
print(f"Tiempo total: {df['Time'].sum()} segundos")
print(f"Tiempo promedio: {df['Time'].mean()} segundos")
print(f"Tiempo minimo: {df['Time'].min()} segundos")
print(f"Tiempo maximo: {df['Time'].max()} segundos")
#Se convierte el dataframe en un arreglo

dataTable=df.to_numpy()
db = ConexionDB()
db.createTable()
#Punto 7 Guarde el resultado en sqlite.
#Se agrega cada fila del arreglo ala base de datos

for data in dataTable:
    db.addRow(data)

#Se muestra la tabla de la base de datos

print("#################### Tabla SQlite ####################")
for row in db.showRow():
    print(row)

#Punto 8 Genere un Json de la tabla creada y guardelo como data.jsone
df.to_json("json/table.json")

#Se inprime el contenido del Json anteriormente creado
print("#################### Tabla Json ####################")
print(pd.read_json('json/table.json'))