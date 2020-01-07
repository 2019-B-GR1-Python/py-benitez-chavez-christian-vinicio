# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:06:01 2019

@author: Christian
"""

import pandas as pd
import numpy as np
import os
import sqlite3
import xlsxwriter

path_guardado_bin = "C://Users//user//Documents//GitHub//py-benitez-chavez-christian-vinicio//clase 15 - Pandas parte 2//data//artwork_data_completo.pickle"

df = pd.read_pickle(path_guardado_bin)

#Obtener el primer valor
primero = df.loc[0]
primero = df.iloc[0]

df2 = df.set_index('id')

datos = {
        'nota1':{
                'Pepito':7,
                'Juan':6,
                'Maria':9
                },
        
        'disciplina':{
                'Pepito':5,
                'Juan':8,
                'Maria':9
                }
        }
        
notas = pd.DataFrame(datos)

notas.loc["Pepito"]
notas.iloc[0]

#Filtrar datos
notas.loc[["Pepito","Juan"],["disciplina","nota1"]]

notas.loc[[True, False, True]]

condicion_nota = notas["nota1"] > 7
discplina = notas["disciplina"] > 7

#Obtener  valores por dos condiciones
notas.loc[condicion_nota][discplina]

mayores_siete = notas.loc[condicion_nota,["nota1"]]

notas.loc["Maria", "disciplina"] = 7


#Estudiantes menores a 7 en Disciplina poner 7
condicion_siete = notas["disciplina"] < 7


notas.loc[condicion_siete] = 7


#Solo a pepito se le va a poner 10 en todo
notas.loc["Pepito"] = 10


#Disciplina de todos los estudiantes se le baje a 7
notas.loc[:, "disciplina"] = 7

#Añadir columna promedio entre nota 1 y disciplina
nota1 = notas["nota1"]
disciplina = notas["disciplina"]

promedio = (nota1+disciplina)/2

notas.loc[:,"promedio"] = promedio
