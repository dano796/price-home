# -*- coding: utf-8 -*-
"""Copia de Copia de NEW_PriceHome.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AWh5TRMW0VKq4XP_5iN4_3y9QopgR1xQ
"""

import json
import pandas as pd
import requests
import re
import time

import numpy as np  # matrices y vectores
import matplotlib.pyplot as plt #gráfica
from sklearn.preprocessing import MinMaxScaler

#Cargamos los datos
data = pd.read_csv("venta.csv")
data.head(900)

data = data[data['rooms'] != 'Sin especificar']
data = data[data['baths'] != 'Sin especificar']
data = data.drop('property_id', axis=1)

data['garages'] = data['garages'].replace('Sin especificar', '0')
data['garages'] = data['garages'].replace('Más de 10', '11')
#Corrección de variables
data['area']=data['area'].astype('int64')
data['rooms']=data['rooms'].astype('int64')
data['garages']=data['garages'].astype('int64')

data['stratum']=data['stratum'].astype('category')
data['baths']=data['baths'].astype('int64')
data['price']=data['price'].astype('int64')
data['neighbourhood']=data['neighbourhood'].astype('category')
data['city']=data['city'].astype('category')

data.info()

data = data[data['price'] < 1300000000]
data = data[data['area'] < 300]

# Si es tipo 'category', conviértela a 'object' o 'string' para un filtrado más directo
if pd.api.types.is_categorical_dtype(data['property_type']):
    data['property_type'] = data['property_type'].astype('object')

# Verifica si la columna es de tipo 'category'
print(data['property_type'].dtype)

opciones_permitidas = ['Apartamento', 'Casa', 'Apartaestudio']
data = data[data['property_type'].isin(opciones_permitidas)]

data['property_type'].unique()

data.info()

#Sklearn sólo analiza variables numéricas
data = pd.get_dummies(data, columns=['is_new','stratum','property_type','neighbourhood','city'], drop_first=False)
data.head()

data = data.drop('stratum_Campestre', axis=1)