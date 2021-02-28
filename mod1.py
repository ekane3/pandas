# -*- coding: utf-8 -*-
"""
@author: EKANE3
Module 1 : Scrapping
"""
import pandas as pd

#Import the csv into a DataFrame
#url:https://cadastre.data.gouv.fr/data/etalab-dvf/latest/csv/2020/full.csv.gz

data = pd.read_csv("D:/full.csv")
df = pd.DataFrame(data)

#Add a column myName using your name.
df['myName'] = 'EKANE3'

#Add a column adresse_string based on existing column
#adresse_string must contain : NUMERO_RUE NOM_RUE NOM_VILLE CODE_POSTAL PAYS

df['adresse_string'] = df['adresse_numero'].map(str) + df['adresse_nom_voie'].map(str) +" "+df['nom_commune'].map(str) +" "+df['code_postal'].map(str) +" FRANCE"
#Delete lines having an empty "longitude" and "latitude" column 
df.dropna(subset = ["longitude","latitude"], inplace=True)
#Print the first ten lines of the dataframe
print(df.head(10))
#Print the dataframe
print(df)



