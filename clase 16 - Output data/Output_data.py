# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:41:24 2019

@author: Christian
"""

import pandas as pd
import numpy as np
import os
import sqlite3
import xlsxwriter


path_guardado_bin = "C://Users//user//Documents//GitHub//py-benitez-chavez-christian-vinicio//clase 15 - Pandas parte 2//data//artwork_data_completo.pickle"

df5 = pd.read_pickle(path_guardado_bin)
df = df5.iloc[49980:50519,:].copy()



#Tipos de archivos: JSON, EXCEL, SQL
path_guardado = 'C://Users//user//Documents//GitHub//py-benitez-chavez-christian-vinicio//clase 16 - Output data//mi_df_completo.xlsx'
#No mostrar los indices
df.to_excel(path_guardado, index = False)

#columnas que si se quiere mostrar
columnas = ['artist', 'title', 'year']
df.to_excel(path_guardado, columns = columnas)

#Escribir multiples hojas de trabajo
#Crear varias hojas de trabajo
path_multiple = 'C://Users//user//Documents//GitHub//py-benitez-chavez-christian-vinicio//clase 16 - Output data//mi_df_multiple.xlsx'
writer = pd.ExcelWriter(path_multiple, engine = 'xlsxwriter')
#Definir hojas
df.to_excel(writer, sheet_name = 'Primera')
df.to_excel(writer, sheet_name = 'Segunda', index = False)
df.to_excel(writer, sheet_name = 'Tercera', columns = columnas)
#Para crear archivo
writer.save()


#Contar cuantos artistas existen en el dateframe (cuenta por artista)
#Sacar el numero de registrso que existen en la columna
num_artistas = df['artist'].value_counts()

path_colores = 'C://Users//user//Documents//GitHub//py-benitez-chavez-christian-vinicio//clase 16 - Output data//mi_df_colores.xlsx'
#Crear una nueva hoja
writer = pd.ExcelWriter(path_colores, engine = 'xlsxwriter')
num_artistas.to_excel(writer, sheet_name = 'Artistas')
#Seleccionar hojas
hoja_artistas = writer.sheets['Artistas']
#Rango de celdas
#ingresar variable en string
rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)
#Crear el formato que se quiere dar
formato_artistas = {
        "type":"2_color_scale",
        "min_value":"10",
        "min_type":"percentile",
        "max_value":"99",
        "max_type":"percentile"}
#conditional_format recibe el rango de las celdas y el formato de los artistas
hoja_artistas.conditional_format(rango_celdas, formato_artistas)
writer.save()








path_grafico = 'C://Users//user//Documents//GitHub//py-benitez-chavez-christian-vinicio//clase 16 - Output data//mi_df_colores.xlsx'
workbook = xlsxwriter.Workbook(path_grafico)
worksheet = workbook.add_worksheet()
worksheet.write_column('B2', num_artistas)

chart = workbook.add_chart({'type': 'line'})




chart.add_series({
    'values': '=Sheet1!$B$2:$B$85',
    'marker': {
        'type': 'square',
        'size': 8,
        'border': {'color': 'black'},
        'fill':   {'color': 'red'},
    },
})


worksheet.insert_chart('D1', chart)
workbook.close()








workbook = xlsxwriter.Workbook(path_grafico)
worksheet = workbook.add_worksheet()





'''
workbook = xlsxwriter.Workbook(path_colores)
worksheet = workbook.add_worksheet()

# Add the worksheet data to be plotted.
data = num_artistas
worksheet.write_column('B2', data)

# Create a new chart object.
chart = workbook.add_chart({'type': 'line'})

# Add a series to the chart.
chart.add_series({'values': rango_celdas})

# Insert the chart into the worksheet.
worksheet.insert_chart('E1', chart)

workbook.close()

'''





with sqlite3.connect("bdd_artist.db") as conexion:
    df5.to_sql('py_artistas1', conexion)


# with mysql.connect('mysql://user:password@')



##Exportar a JSON
## Muestre tipo tabla
df5.to_json('artistas_tabla.json', orient='table')


