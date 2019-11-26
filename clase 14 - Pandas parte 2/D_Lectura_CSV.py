# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:20:36 2019

@author: Christian
"""

import pandas as pd
import os

# Tipos de archivos que se pueden leer
#  1) Se puede importar un JSON, CSV, HTML, XML...
#  2) Archivos binarios
#  3) Bases de datos relacionales

path = "C://Users//user//Documents//GitHub//py-benitez-chavez-christian-vinicio//clase 14 - Pandas parte 2//data//artwork_data.csv"

df1 = pd.read_csv(path, nrows = 10)

#Definir las columnas que se necesita
columnas = ['id','artist','title','medium','year','acquisitionYear','height','width','units']
df2 = pd.read_csv(path, nrows = 10, usecols = columnas)


#Utilizar sierta columna como indice
df3 = pd.read_csv(path, nrows = 10, usecols = columnas, index_col = 'id')

# Guardar dataframes
path_guardado = "C://Users//user//Documents//GitHub//py-benitez-chavez-christian-vinicio//clase 14 - Pandas parte 2//data//artwork_data.pickle"
df3.to_pickle(path_guardado)


# Guardar dataframe completo
df4 = pd.read_csv(path)
path_guardado_2 = "C://Users//user//Documents//GitHub//py-benitez-chavez-christian-vinicio//clase 14 - Pandas parte 2//data//artwork_data_completo.pickle"
df4.to_pickle(path_guardado_2)


#Leer pickle
df5 = pd.read_pickle(path_guardado_2)