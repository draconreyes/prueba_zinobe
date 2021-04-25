# prueba-zinobe

## Tabajo a resolver

|  Region | City Name |  Languaje | Time  |
|---|---|---|---|
|  Africa | Angola  |  AF4F4762F9BD3F0F4A10CAF5B6E63DC4CE543724 | 0.23 ms  |
|   |   |   |   |
|   |   |   |   |

Desarrolle una aplicacion en python que genere la tabla anterior teniendo las siguientes consideraciones:

1. De https://rapidapi.com/apilayernet/api/rest-countries-v1, obtenga todas las regiones existentes.
2. De https://restcountries.eu/ Obtenga un pais por region apartir de la region optenida del punto 1.
3. De https://restcountries.eu/ obtenga el nombre del idioma que habla el pais y encriptelo con SHA1
4. En la columna Time ponga el tiempo que tardo en armar la fila (debe ser automatico)
5. La tabla debe ser creada en un DataFrame con la libreria PANDAS
6. Con funciones de la libreria pandas muestre el tiempo total, el tiempo promedio, el tiempo minimo y el maximo que tardo en procesar toda las filas de la tabla.
7. Guarde el resultado en sqlite.
8. Genere un Json de la tabla creada y guardelo como data.json
9. La prueba debe ser entregada en un repositorio git.


**Es un plus si:**
* No usa famework
* Entrega Test Unitarios
* Presenta un diseño de su solucion.

## Descargar:
```
git clone https://github.com/draconreyes/prueba_zinobe.git
```
## Correr el siguien comando en la consola:
```
python main.py
```
![image](https://user-images.githubusercontent.com/50085428/115997131-a74e9a80-a5a7-11eb-897c-226ebc2dfedb.png)

## Resultado:
![image](https://user-images.githubusercontent.com/50085428/115997187-e2e96480-a5a7-11eb-8876-7e67fa57fb82.png)
![image](https://user-images.githubusercontent.com/50085428/115997215-f8f72500-a5a7-11eb-8e1c-3869fac428c6.png)

## Ejecutar tests
```
python test_api.py
```

## Diseño de solucion
![image](https://user-images.githubusercontent.com/50085428/115997494-ecbf9780-a5a8-11eb-82b0-0810ab331dde.png)


