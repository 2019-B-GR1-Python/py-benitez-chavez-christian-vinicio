# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:42:15 2019

@author: Christian
"""

import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,50,6).reshape(2,3)

def1 = pd.DataFrame(arr_pand)

#Conjunto de series
#Cada uno tiene un conjunto de indices
s1 = def1[0]
s2 = def1[1]
s3 = def1[2]

#Guardar una serie en una nueva columna
nueva_serie = ["25", "60"]
s4 = pd.Series(nueva_serie)
def2 = def1.insert(4,4,4)

#Añadir nueva serie en dataframe
def1[5] = s4

#Caluclos con series
def1[6] = s1 * s2

#Crear dataframe - mandar nombre de columndas
datos_fisicos_uno = pd.DataFrame(arr_pand, columns=['Estatura (cm)', 'Peso (gr)', 'Edad (anios)'])
#Nombre de indices
datos_fisicos_dos = pd.DataFrame(arr_pand, columns=['Estatura (cm)', 'Peso (gr)', 'Edad (anios)'], index=['Christian', 'Benitez'])
#Renombrar indices 
def1.index=['Maria','Jose']
#Renombrar columnas
def1.columns = ['A','B','C','D','E','F','G']