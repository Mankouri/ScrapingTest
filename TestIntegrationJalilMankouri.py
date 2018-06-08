# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 16:30:04 2018

@author: jalil Test integration Deepki
"""

import pandas as pd
import numpy as np

# On lit le csv et on sauvegarde le résultat dans un dataframe
df_dju = pd.read_csv('df_dju.csv')
df_conso = pd.read_csv('df_conso.csv')

# Dénormalisation de df_conso 6795 lignes
# Utilisation d'un pivot tableau croisé dynamique + groupeBy
print(len(df_conso))
print(df_conso.head())

#df_conso_final = pd.DataFrame(raw_data , columns = ['id_site', 'date', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9'])

#print(df)

#resultat = df_conso.pivot(index="date", columns= ['id_bat'])


resultat = df_conso.pivot(index=['date','id_bat'], columns='id_bat', values='conso')
print(resultat.head(1))


# Deuxieme partie groupeby du résultat avec df_dju sur la colonne en commun

