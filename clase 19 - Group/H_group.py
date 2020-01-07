# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:19:24 2020

@author: Christian
"""

import pandas as pd
import numpy as np
import os
import sqlite3
import xlsxwriter
import math


path_guardado_bin = "C://Users//user//Documents//GitHub//py-benitez-chavez-christian-vinicio//clase 15 - Pandas parte 2//data//artwork_data_completo.pickle"

df5 = pd.read_pickle(path_guardado_bin)

#sacar una seccion de un datafrem
seccion_df = df5.iloc[49980:50019,:].copy()

#agrupar por artista
df_agrupado = seccion_df.groupby('artist')
type(df_agrupado)
#a = es la columna agrupada
#b = data frame completo
for columna_agrupada, df_completo in df_agrupado:
    print(type(columna_agrupada))
    print(type(df_completo))
    
    print(columna_agrupada)
    print(df_completo)
    
#Obtener valores de una sola columna
a = seccion_df['units'].value_counts()
#Verificar si la columna esta vacia. Devuelve True o False
a.empty


#Llenar valores vacíos de algun campo
def llenar_valores_vacios(series, tipo):
    lista_valores = series.value_counts()
    if(lista_valores.empty == True):
        return series
    else:
        if tipo == 'promedio':
            suma = 0
            numero_valores = 0
            for valor_serie in series:
                
                
                if(isinstance(valor_serie,str)):
                    valor = int(valor_serie)
                    numero_valores = numero_valores + 1
                    suma = suma + valor
                
                else:
                    pass
                    
                
            promedio = suma / numero_valores
            #llenar espacios vacios con el promedio obtenido
            series_valores_llenos = series.fillna(promedio)
            
            return series_valores_llenos
        
        
        if tipo == 'value_counts':
            valor_repetido = series["units"]
            for valor_serie in series:
                if (isinstance(valor_serie,str)):
                    
                    series.loc[:, "units"] = valor_repetido
            
            
                
        
        
        


def transormar_df(df):
    df_artist = df.groupby('artist')
    lista_df = []
    
    for artista, df in df_artist:
        copia = df.copy()
        serie_w = copia['width']
        serie_h = copia['height']
        serie_u = copia['units']
        serie_i = copia['inscription']
        copia.loc[:,'width'] = llenar_valores_vacios(serie_w, 'promedio')
        copia.loc[:,'height'] = llenar_valores_vacios(serie_h, 'promedio')
        copia.loc[:,'units'] = llenar_valores_vacios(serie_u, 'value_counts')
        copia.loc[:,'inscription'] = llenar_valores_vacios(serie_i, 'value_counts')
        lista_df.append(copia)
    
    df_completo_con_valores = pd.concat(lista_df)
    return df_completo_con_valores


de_valores_llenos = transormar_df(seccion_df)
        
                    
                






