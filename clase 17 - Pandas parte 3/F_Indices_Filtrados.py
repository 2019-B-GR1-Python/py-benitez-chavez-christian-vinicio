# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:53:09 2019

@author: Christian
"""



import pandas as pd
import numpy as np
import os
import sqlite3
import xlsxwriter

path_guardado_bin = "C://Users//user//Documents//GitHub//py-benitez-chavez-christian-vinicio//clase 15 - Pandas parte 2//data//artwork_data_completo.pickle"

df5 = pd.read_pickle(path_guardado_bin)

#Obtener nombre de los artistas
series_artistas_repetidos = df5["artist"]

#Obtener solo una vez cada artista
artistas = pd.unique(series_artistas_repetidos)

artistas.size
len(artistas)

blake = df5["artist"] == "Blake, William"

#Cuantos valores existe de cada uno
blake.value_counts()
df5["artist"].value_counts()

#Obtener solo el dataframe de blake
df_blake = df5[blake]