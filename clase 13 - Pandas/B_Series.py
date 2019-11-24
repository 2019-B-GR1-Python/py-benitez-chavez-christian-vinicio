# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:57:36 2019

@author: Christian
"""

import numpy as np
import pandas as pd

lista_numeros = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

#crear instancia de serie
#Se debe de mandar un iterable
#se tiene una columna index

#listas
serie_a = pd.Series(lista_numeros)

#tuplas
serie_b = pd.Series(np_numeros)

#Todo tipo de datos
serie_c = pd.Series([
        True,
        False,
        12,
        12.14,
        "Christian",
        None,
        (),
        [],
        {"nombre":"Chris"}
        ])

#Acceder al dato de la serie
serie_c[3]


lista_ciudades = ["Ambato", "Cuenca", "Loja", "Quito"]


#se manda la lista y el indice, para cambiar el indice
serie_ciudad = pd.Series(lista_ciudades,index = ["A","C", "L", "Q"])
#Se puede usar cualquier tipo de indice 
serie_ciudad["Q"]
serie_ciudad[3]

#Simplificado
valores_ciudad = {
        "Ibarra":9500,
        "Guayaquil":10000,
        "Cuenca":7000,
        "Quito":8000,
        "Loja":3000
        }


serie_valor_ciudad = pd.Series(valores_ciudad)

serie_valor_ciudad["Quito"]
serie_valor_ciudad[3]

#Ver ciudaddes con valores menores a 5000
#Devuelve una serie de booleanos
ciudades_menores_a_5000 = serie_valor_ciudad < 5000
menor_5000 = serie_valor_ciudad[ciudades_menores_a_5000]

#Incrementar valores en el 10%
aumento_10_porciento = serie_valor_ciudad * 1.10

#Decrementar valores a Quito
serie_valor_ciudad[3] = serie_valor_ciudad[3] - 50
serie_valor_ciudad["Quito"] = serie_valor_ciudad["Quito"] - 50

#Buscar un valor
print("Lima" in serie_valor_ciudad)
print("Loja" in serie_valor_ciudad)

#Elevar al cuadrado los valores de la serie
#Deveulve una serie
rsquare = np.square(serie_valor_ciudad)

#Sacar el seno
rsen = np.sin(serie_valor_ciudad)

ciudades_uno = pd.Series({
        "Montañita":300,
        "Guayaquil":1000,
        "Quito":2000
        })

ciudades_dos = pd.Series({
        "Loja":300,
        "Guayaquil":1000
        })

#Solo se puede hacer operaciones cuando tiene los mismos indices
suma_total = ciudades_uno + ciudades_dos


#Crear nuevos registros
ciudades_uno["Loja"] = 0
ciudades_dos["Montañita"] = 0
ciudades_dos["Quito"] = 0
#Sumar
ciudad_add = ciudades_uno.add(ciudades_dos)

#Concatenar dos series
#Se une todo
ciu_concatenadas = pd.concat([ciudades_uno, ciudades_dos])

#Ver valores repetidos
ciu_concatenadas_v = pd.concat([
        ciudades_uno, 
        ciudades_dos], verify_integrity = True)



#Concatenar dos o mas series
#Se mostrarán los valores repetidos en cas de existir
ciu_append = ciudades_uno.append(ciudades_dos, verify_integrity = True)

#Maximo valor
max(ciudades_uno)
pd.Series.max(ciudades_uno)
np.max(ciudades_uno)

#Minimo valor
pd.Series.min(ciudades_uno)
np.min(ciudades_uno)

#ESTADISTICA
#Media y mediana
ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)

#Los primeros o ultimos valores
ciudades_uno.head(2)
ciudades_uno.tail(2)


#Ordenar los valores
#Ordena de menor a mayor de por defecto
ciudades_uno.sort_values().head(2)
#Para cambiar el tipo de ordenamiento
ciudades_uno.sort_values(ascending = False).head(2)
ciudades_uno.sort_values().tail(2)





















