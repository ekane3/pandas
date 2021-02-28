# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 14:32:46 2021

@author: EKANE EMILE
Module 1 : Scrapping
"""
import pandas as pd

#Importer le csv dans un DataFrame pandas.
#url:https://cadastre.data.gouv.fr/data/etalab-dvf/latest/csv/2020/full.csv.gz
data = pd.read_csv("D:/full.csv")
df = pd.DataFrame(data)
#Ajouter une colonne contenant votre nom.
df['myName'] = 'EKANE'
#Ajouter une colonne portant le nom « adresse_string 
#NUMERO_RUE NOM_RUE NOM_VILLE CODE_POSTAL PAYS
df['adresse_string'] = df['adresse_numero'].map(str) + df['adresse_nom_voie'].map(str) +" "+df['nom_commune'].map(str) +" "+df['code_postal'].map(str) +" FRANCE"
#Supprimer les lignes ayant les colonnes « longitude » et « latitude » à vide
df.dropna(subset = ["longitude","latitude"], inplace=True)
print(df.head(10))



