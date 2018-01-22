import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

incomes={}

with open ("../big_data_project_confidential/BASE_Donnees_Clients.csv") as dataClients:
    readerClients = csv.reader(dataClients, delimiter=";")
    fieldsClients = next(readerClients)
    listClients= list(readerClients)
    dfClients = pd.DataFrame(listClients, columns=fieldsClients)
    dfClients['ï»¿ID_GRC'].replace("NULL", 0, inplace=True)
    dfClients['MT_IARD_2015'].replace("NULL", 0, inplace=True)
    dfClients['MT_IARD_2016'].replace("NULL", 0, inplace=True)
    dfClients['MT_IARD_2017'].replace("NULL", 0, inplace=True)
    dfClients.set_index('ï»¿ID_GRC', inplace=True)
    dfClients = dfClients[['MT_IARD_2015', 'MT_IARD_2016', 'MT_IARD_2017']].astype(str).astype(float)
    
    print(dfClients)
    
    dataClients.close()
with open ("../big_data_project_confidential/BASE_Avantages_clients.csv") as dataClients:
    readerAdv = csv.reader(dataClients, delimiter=";")
    fieldsClients = next(readerAdv)
    listClients= list(readerAdv)
    
    dfAdv = pd.DataFrame(listClients, columns=fieldsClients)
    dfAdv['CODE_AVG'].replace("NULL", 0, inplace=True)
    dfAdv['STATUT'].replace("NULL", 0, inplace=True)
    dfAdv['CLIENT_FIDELE'].replace("NULL", 0, inplace=True)
    dfAdv.set_index('ï»¿ID_GRC', inplace=True)
    
    print(dfAdv)

    dataClients.close()

with open ("../big_data_project_confidential/BASE_Reclamations_clients.csv") as dataClients:
    readerComp = csv.reader(dataClients, delimiter=";")
    fieldsClients = next(readerComp)
    listClients= list(readerComp)
    
    dfComp = pd.DataFrame(listClients, columns=fieldsClients)
    dfComp['DATE_CREATION'].replace("NULL", 0, inplace=True)
    dfComp['STATUT'].replace("NULL", 0, inplace=True)
    dfComp['CLIENT_FIDELE'].replace("NULL", 0, inplace=True)
    dfComp.set_index('ï»¿ID_GRC', inplace=True)
    
    print(dfComp)

    dataClients.close()
