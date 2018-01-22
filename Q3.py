# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 03:15:25 2018

@author: GAZOUZI
"""

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
    dfClients.replace("NULL", 0, inplace=True)
    dfClients['ï»¿ID_GRC'].replace("NULL", 0, inplace=True)
    dfClients['CD_COMMERCIAL_CHARGE'].replace("NULL", 0, inplace=True)
    dfClients['MT_IARD_2015'].replace("NULL", 0, inplace=True)
    dfClients['MT_IARD_2016'].replace("NULL", 0, inplace=True)
    dfClients['MT_IARD_2017'].replace("NULL", 0, inplace=True)
    dfClients = dfClients[['ï»¿ID_GRC', 'CD_COMMERCIAL_CHARGE','MT_IARD_2015', 'MT_IARD_2016', 'MT_IARD_2017']].astype(str).astype(float)
    #print(dfClients)
    dfClients.loc['Total'] = dfClients.sum()
    incomes['2015']=dfClients.at['Total', 'MT_IARD_2015']
    incomes['2016']=dfClients.at['Total', 'MT_IARD_2016']
    incomes['2017']=dfClients.at['Total', 'MT_IARD_2017']
    '''plot=plt.plot(incomes.keys(), incomes.values(),color='b')
    plt.title('income of Groupama')
    plt.xlabel('Years')
    plt.ylabel('income (Euro)')  
    plt.savefig('plots/income.png')
    #plt.show()
    print(incomes)
    '''
    dataClients.close()
goodRate= ['6','7','8','9','10']
badRate= ['0','1','2','3','4','5']
satisfactionRequestsYears={}
df = pd.DataFrame([])
with open ("../big_data_project_confidential/SATISFACTION_DEMANDE_2015_2016_2017.csv") as satisfactionRequests:
    readerSatisfactionRequests = csv.reader(satisfactionRequests, delimiter=";")
    fieldsSatisfactionRequests = next(readerSatisfactionRequests)
    fieldsSatisfactionRequests = next(readerSatisfactionRequests)
    listSatisfactionRequests= list(readerSatisfactionRequests)
    dflistSatisfactionRequests = pd.DataFrame(listSatisfactionRequests, columns=fieldsSatisfactionRequests)
    dflistSatisfactionRequests.rename(columns={'Suite Ã\xa0 cette expÃ©rience et sur une Ã©chelle de 0 Ã\xa0 10, dans quelle mesure recommanderiez-vous Groupama Ã\xa0 un proche ou Ã\xa0 un collÃ¨gue ? Â\xa00 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistSatisfactionRequests2015=dflistSatisfactionRequests[dflistSatisfactionRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numberSatisfaction2015=len(dflistSatisfactionRequests2015.index)
    dflistSatisfactionRequests2015.loc[dflistSatisfactionRequests2015['note'].isin(goodRate)]
    satisfied=dflistSatisfactionRequests2015.loc[dflistSatisfactionRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistSatisfactionRequests2015.loc[dflistSatisfactionRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberSatisfaction2015),"unsatisfied":float(len(unsatisfied.index)/numberSatisfaction2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistSatisfactionRequests2016=dflistSatisfactionRequests[dflistSatisfactionRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberSatisfaction2016=len(dflistSatisfactionRequests2016.index)
    satisfied=dflistSatisfactionRequests2016.loc[dflistSatisfactionRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistSatisfactionRequests2016.loc[dflistSatisfactionRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberSatisfaction2016),"unsatisfied":float(len(unsatisfied.index)/numberSatisfaction2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistSatisfactionRequests2017=dflistSatisfactionRequests[dflistSatisfactionRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberSatisfaction2017=len(dflistSatisfactionRequests2017.index)
    print(numberSatisfaction2017)
    satisfied=dflistSatisfactionRequests2017.loc[dflistSatisfactionRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistSatisfactionRequests2017.loc[dflistSatisfactionRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberSatisfaction2017),"unsatisfied":float(len(unsatisfied.index)/numberSatisfaction2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    print(df)
    satisfactionRequestsYears['2015']=df.at['2015', 'satisfied']
    satisfactionRequestsYears['2016']=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']=df.at['2017', 'satisfied']
    x =['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('SATISFACTION_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_satisfaction.png')
    
df = pd.DataFrame([])
with open ("../big_data_project_confidential/SATISFACTION_RECLAMATION_2015_2016_2107.csv") as reclamationRequests:
    readerreclamationRequests = csv.reader(reclamationRequests, delimiter=";")
    fieldsreclamationRequests = next(readerreclamationRequests)
    fieldsreclamationRequests = next(readerreclamationRequests)
    listreclamationRequests= list(readerreclamationRequests)
    
    dflistreclamationRequests = pd.DataFrame(listreclamationRequests, columns=fieldsreclamationRequests)
    dflistreclamationRequests.rename(columns={'Suite Ã  cette expÃ©rience et sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistreclamationRequests2015=dflistreclamationRequests[dflistreclamationRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numberreclamation2015=len(dflistreclamationRequests2015.index)
    
    dflistreclamationRequests2015.loc[dflistreclamationRequests2015['note'].isin(goodRate)]
    satisfied=dflistreclamationRequests2015.loc[dflistreclamationRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistreclamationRequests2015.loc[dflistreclamationRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberreclamation2015),"unsatisfied":float(len(unsatisfied.index)/numberreclamation2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistreclamationRequests2016=dflistreclamationRequests[dflistreclamationRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberreclamation2016=len(dflistreclamationRequests2016.index)
    
    satisfied=dflistreclamationRequests2016.loc[dflistreclamationRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistreclamationRequests2016.loc[dflistreclamationRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberreclamation2016),"unsatisfied":float(len(unsatisfied.index)/numberreclamation2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistreclamationRequests2017=dflistreclamationRequests[dflistreclamationRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberreclamation2017=len(dflistreclamationRequests2017.index)
    
    satisfied=dflistreclamationRequests2017.loc[dflistreclamationRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistreclamationRequests2017.loc[dflistreclamationRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberreclamation2017),"unsatisfied":float(len(unsatisfied.index)/numberreclamation2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=df.at['2015', 'satisfied']
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('reclamation_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_reclamation.png')
    
df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_DENTAIRE_PARTENAIRE_2015_2016_2017.csv")  as partenaireRequests:
    readerpartenaireRequests = csv.reader(partenaireRequests, delimiter=";")
    fieldspartenaireRequests = next(readerpartenaireRequests)
    fieldspartenaireRequests = next(readerpartenaireRequests)
    listpartenaireRequests= list(readerpartenaireRequests)
    
    dflistpartenaireRequests = pd.DataFrame(listpartenaireRequests, columns=fieldspartenaireRequests)
    dflistpartenaireRequests.rename(columns={'Suite Ã  cette expÃ©rience, sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistpartenaireRequests2015=dflistpartenaireRequests[dflistpartenaireRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numberpartenaire2015=len(dflistpartenaireRequests2015.index)
    
    dflistpartenaireRequests2015.loc[dflistpartenaireRequests2015['note'].isin(goodRate)]
    satisfied=dflistpartenaireRequests2015.loc[dflistpartenaireRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistpartenaireRequests2015.loc[dflistpartenaireRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberpartenaire2015),"unsatisfied":float(len(unsatisfied.index)/numberpartenaire2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistpartenaireRequests2016=dflistpartenaireRequests[dflistpartenaireRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberpartenaire2016=len(dflistpartenaireRequests2016.index)
    
    satisfied=dflistpartenaireRequests2016.loc[dflistpartenaireRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistpartenaireRequests2016.loc[dflistpartenaireRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberpartenaire2016),"unsatisfied":float(len(unsatisfied.index)/numberpartenaire2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistpartenaireRequests2017=dflistpartenaireRequests[dflistpartenaireRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberpartenaire2017=len(dflistpartenaireRequests2017.index)
    
    satisfied=dflistpartenaireRequests2017.loc[dflistpartenaireRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistpartenaireRequests2017.loc[dflistpartenaireRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberpartenaire2017),"unsatisfied":float(len(unsatisfied.index)/numberpartenaire2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=df.at['2015', 'satisfied']
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('partenaire_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_partenaire.png')
    
df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_DENTAIRE_NON_PARTENAIRE_2015_2016_2017.csv")  as nonPartenaireRequests:
    readernonPartenaireRequests = csv.reader(nonPartenaireRequests, delimiter=";")
    fieldsnonPartenaireRequests = next(readernonPartenaireRequests)
    fieldsnonPartenaireRequests = next(readernonPartenaireRequests)
    listnonPartenaireRequests= list(readernonPartenaireRequests)
    
    dflistnonPartenaireRequests = pd.DataFrame(listnonPartenaireRequests, columns=fieldsnonPartenaireRequests)
    dflistnonPartenaireRequests.rename(columns={'Suite Ã  cette expÃ©rience, sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistnonPartenaireRequests2015=dflistnonPartenaireRequests[dflistnonPartenaireRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numbernonPartenaire2015=len(dflistnonPartenaireRequests2015.index)
    
    dflistnonPartenaireRequests2015.loc[dflistnonPartenaireRequests2015['note'].isin(goodRate)]
    satisfied=dflistnonPartenaireRequests2015.loc[dflistnonPartenaireRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistnonPartenaireRequests2015.loc[dflistnonPartenaireRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numbernonPartenaire2015),"unsatisfied":float(len(unsatisfied.index)/numbernonPartenaire2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistnonPartenaireRequests2016=dflistnonPartenaireRequests[dflistnonPartenaireRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numbernonPartenaire2016=len(dflistnonPartenaireRequests2016.index)
    
    satisfied=dflistnonPartenaireRequests2016.loc[dflistnonPartenaireRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistnonPartenaireRequests2016.loc[dflistnonPartenaireRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numbernonPartenaire2016),"unsatisfied":float(len(unsatisfied.index)/numbernonPartenaire2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistnonPartenaireRequests2017=dflistnonPartenaireRequests[dflistnonPartenaireRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numbernonPartenaire2017=len(dflistnonPartenaireRequests2017.index)
    
    satisfied=dflistnonPartenaireRequests2017.loc[dflistnonPartenaireRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistnonPartenaireRequests2017.loc[dflistnonPartenaireRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numbernonPartenaire2017),"unsatisfied":float(len(unsatisfied.index)/numbernonPartenaire2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=df.at['2015', 'satisfied']
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('nonPartenaire_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_nonPartenaire.png')
    
df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_DENTAIRE_PARTENAIRE_2015_2016_2017.csv")  as partenaireRequests:
    readerpartenaireRequests = csv.reader(partenaireRequests, delimiter=";")
    fieldspartenaireRequests = next(readerpartenaireRequests)
    fieldspartenaireRequests = next(readerpartenaireRequests)
    listpartenaireRequests= list(readerpartenaireRequests)
    
    dflistpartenaireRequests = pd.DataFrame(listpartenaireRequests, columns=fieldspartenaireRequests)
    dflistpartenaireRequests.rename(columns={'Suite Ã  cette expÃ©rience, sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistpartenaireRequests2015=dflistpartenaireRequests[dflistpartenaireRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numberpartenaire2015=len(dflistpartenaireRequests2015.index)
    
    dflistpartenaireRequests2015.loc[dflistpartenaireRequests2015['note'].isin(goodRate)]
    satisfied=dflistpartenaireRequests2015.loc[dflistpartenaireRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistpartenaireRequests2015.loc[dflistpartenaireRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberpartenaire2015),"unsatisfied":float(len(unsatisfied.index)/numberpartenaire2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistpartenaireRequests2016=dflistpartenaireRequests[dflistpartenaireRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberpartenaire2016=len(dflistpartenaireRequests2016.index)
    
    satisfied=dflistpartenaireRequests2016.loc[dflistpartenaireRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistpartenaireRequests2016.loc[dflistpartenaireRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberpartenaire2016),"unsatisfied":float(len(unsatisfied.index)/numberpartenaire2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistpartenaireRequests2017=dflistpartenaireRequests[dflistpartenaireRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberpartenaire2017=len(dflistpartenaireRequests2017.index)
    
    satisfied=dflistpartenaireRequests2017.loc[dflistpartenaireRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistpartenaireRequests2017.loc[dflistpartenaireRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberpartenaire2017),"unsatisfied":float(len(unsatisfied.index)/numberpartenaire2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=df.at['2015', 'satisfied']
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('partenaire_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_partenaire.png')
    
df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_DENTAIRE_NON_PARTENAIRE_2015_2016_2017.csv")  as nonPartenaireRequests:
    readernonPartenaireRequests = csv.reader(nonPartenaireRequests, delimiter=";")
    fieldsnonPartenaireRequests = next(readernonPartenaireRequests)
    fieldsnonPartenaireRequests = next(readernonPartenaireRequests)
    listnonPartenaireRequests= list(readernonPartenaireRequests)
    
    dflistnonPartenaireRequests = pd.DataFrame(listnonPartenaireRequests, columns=fieldsnonPartenaireRequests)
    dflistnonPartenaireRequests.rename(columns={'Suite Ã  cette expÃ©rience, sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistnonPartenaireRequests2015=dflistnonPartenaireRequests[dflistnonPartenaireRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numbernonPartenaire2015=len(dflistnonPartenaireRequests2015.index)
    
    dflistnonPartenaireRequests2015.loc[dflistnonPartenaireRequests2015['note'].isin(goodRate)]
    satisfied=dflistnonPartenaireRequests2015.loc[dflistnonPartenaireRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistnonPartenaireRequests2015.loc[dflistnonPartenaireRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numbernonPartenaire2015),"unsatisfied":float(len(unsatisfied.index)/numbernonPartenaire2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistnonPartenaireRequests2016=dflistnonPartenaireRequests[dflistnonPartenaireRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numbernonPartenaire2016=len(dflistnonPartenaireRequests2016.index)
    
    satisfied=dflistnonPartenaireRequests2016.loc[dflistnonPartenaireRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistnonPartenaireRequests2016.loc[dflistnonPartenaireRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numbernonPartenaire2016),"unsatisfied":float(len(unsatisfied.index)/numbernonPartenaire2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistnonPartenaireRequests2017=dflistnonPartenaireRequests[dflistnonPartenaireRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numbernonPartenaire2017=len(dflistnonPartenaireRequests2017.index)
    
    satisfied=dflistnonPartenaireRequests2017.loc[dflistnonPartenaireRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistnonPartenaireRequests2017.loc[dflistnonPartenaireRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numbernonPartenaire2017),"unsatisfied":float(len(unsatisfied.index)/numbernonPartenaire2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=df.at['2015', 'satisfied']
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('nonPartenaire_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_nonPartenaire.png')


df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_OPTIQUE_PARTENAIRE_2015_2016_2017.csv")  as optiqueRequests:
    readeroptiqueRequests = csv.reader(optiqueRequests, delimiter=";")
    fieldsoptiqueRequests = next(readeroptiqueRequests)
    fieldsoptiqueRequests = next(readeroptiqueRequests)
    listoptiqueRequests= list(readeroptiqueRequests)
    
    dflistoptiqueRequests = pd.DataFrame(listoptiqueRequests, columns=fieldsoptiqueRequests)
    dflistoptiqueRequests.rename(columns={'Suite Ã  cette expÃ©rience, sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistoptiqueRequests2015=dflistoptiqueRequests[dflistoptiqueRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numberoptique2015=len(dflistoptiqueRequests2015.index)
    
    dflistoptiqueRequests2015.loc[dflistoptiqueRequests2015['note'].isin(goodRate)]
    satisfied=dflistoptiqueRequests2015.loc[dflistoptiqueRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistoptiqueRequests2015.loc[dflistoptiqueRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberoptique2015),"unsatisfied":float(len(unsatisfied.index)/numberoptique2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistoptiqueRequests2016=dflistoptiqueRequests[dflistoptiqueRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberoptique2016=len(dflistoptiqueRequests2016.index)
    
    satisfied=dflistoptiqueRequests2016.loc[dflistoptiqueRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistoptiqueRequests2016.loc[dflistoptiqueRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberoptique2016),"unsatisfied":float(len(unsatisfied.index)/numberoptique2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistoptiqueRequests2017=dflistoptiqueRequests[dflistoptiqueRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberoptique2017=len(dflistoptiqueRequests2017.index)
    
    satisfied=dflistoptiqueRequests2017.loc[dflistoptiqueRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistoptiqueRequests2017.loc[dflistoptiqueRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberoptique2017),"unsatisfied":float(len(unsatisfied.index)/numberoptique2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=df.at['2015', 'satisfied']
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('optique_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_optique.png')
    
df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_OPTIQUE_NON_PARTENAIRE_2015_2016_2017.csv")  as nonoptiqueRequests:
    readernonoptiqueRequests = csv.reader(nonoptiqueRequests, delimiter=";")
    fieldsnonoptiqueRequests = next(readernonoptiqueRequests)
    fieldsnonoptiqueRequests = next(readernonoptiqueRequests)
    listnonoptiqueRequests= list(readernonoptiqueRequests)
    
    dflistnonoptiqueRequests = pd.DataFrame(listnonoptiqueRequests, columns=fieldsnonoptiqueRequests)
    dflistnonoptiqueRequests.rename(columns={'Suite Ã  cette expÃ©rience, sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistnonoptiqueRequests2015=dflistnonoptiqueRequests[dflistnonoptiqueRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numbernonoptique2015=len(dflistnonoptiqueRequests2015.index)
    
    dflistnonoptiqueRequests2015.loc[dflistnonoptiqueRequests2015['note'].isin(goodRate)]
    satisfied=dflistnonoptiqueRequests2015.loc[dflistnonoptiqueRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistnonoptiqueRequests2015.loc[dflistnonoptiqueRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numbernonoptique2015),"unsatisfied":float(len(unsatisfied.index)/numbernonoptique2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistnonoptiqueRequests2016=dflistnonoptiqueRequests[dflistnonoptiqueRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numbernonoptique2016=len(dflistnonoptiqueRequests2016.index)
    
    satisfied=dflistnonoptiqueRequests2016.loc[dflistnonoptiqueRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistnonoptiqueRequests2016.loc[dflistnonoptiqueRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numbernonoptique2016),"unsatisfied":float(len(unsatisfied.index)/numbernonoptique2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistnonoptiqueRequests2017=dflistnonoptiqueRequests[dflistnonoptiqueRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numbernonoptique2017=len(dflistnonoptiqueRequests2017.index)
    
    satisfied=dflistnonoptiqueRequests2017.loc[dflistnonoptiqueRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistnonoptiqueRequests2017.loc[dflistnonoptiqueRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numbernonoptique2017),"unsatisfied":float(len(unsatisfied.index)/numbernonoptique2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=df.at['2015', 'satisfied']
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('nonoptique_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_nonoptique.png')

df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_DAB_2015_2016_2107.csv")  as dabRequests:
    readerdabRequests = csv.reader(dabRequests, delimiter=";")
    fieldsdabRequests = next(readerdabRequests)
    fieldsdabRequests = next(readerdabRequests)
    listdabRequests= list(readerdabRequests)
    
    dflistdabRequests = pd.DataFrame(listdabRequests, columns=fieldsdabRequests)
    dflistdabRequests.rename(columns={'Suite Ã  cette expÃ©rience et sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistdabRequests2015=dflistdabRequests[dflistdabRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numberdab2015=len(dflistdabRequests2015.index)
    
    dflistdabRequests2015.loc[dflistdabRequests2015['note'].isin(goodRate)]
    satisfied=dflistdabRequests2015.loc[dflistdabRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistdabRequests2015.loc[dflistdabRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberdab2015),"unsatisfied":float(len(unsatisfied.index)/numberdab2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistdabRequests2016=dflistdabRequests[dflistdabRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberdab2016=len(dflistdabRequests2016.index)
    
    satisfied=dflistdabRequests2016.loc[dflistdabRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistdabRequests2016.loc[dflistdabRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberdab2016),"unsatisfied":float(len(unsatisfied.index)/numberdab2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistdabRequests2017=dflistdabRequests[dflistdabRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberdab2017=len(dflistdabRequests2017.index)
    
    satisfied=dflistdabRequests2017.loc[dflistdabRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistdabRequests2017.loc[dflistdabRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberdab2017),"unsatisfied":float(len(unsatisfied.index)/numberdab2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=df.at['2015', 'satisfied']
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('dab_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_dab.png')
    
df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_SOUSCRIPTION_2015_2016_2017.csv")  as souscriptionRequests:
    readersouscriptionRequests = csv.reader(souscriptionRequests, delimiter=";")
    fieldssouscriptionRequests = next(readersouscriptionRequests)
    fieldssouscriptionRequests = next(readersouscriptionRequests)
    listsouscriptionRequests= list(readersouscriptionRequests)
    
    dflistsouscriptionRequests = pd.DataFrame(listsouscriptionRequests, columns=fieldssouscriptionRequests)
    dflistsouscriptionRequests.rename(columns={'Suite Ã  cette expÃ©rience et sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistsouscriptionRequests2015=dflistsouscriptionRequests[dflistsouscriptionRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numbersouscription2015=len(dflistsouscriptionRequests2015.index)
    
    dflistsouscriptionRequests2015.loc[dflistsouscriptionRequests2015['note'].isin(goodRate)]
    satisfied=dflistsouscriptionRequests2015.loc[dflistsouscriptionRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistsouscriptionRequests2015.loc[dflistsouscriptionRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numbersouscription2015),"unsatisfied":float(len(unsatisfied.index)/numbersouscription2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistsouscriptionRequests2016=dflistsouscriptionRequests[dflistsouscriptionRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numbersouscription2016=len(dflistsouscriptionRequests2016.index)
    
    satisfied=dflistsouscriptionRequests2016.loc[dflistsouscriptionRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistsouscriptionRequests2016.loc[dflistsouscriptionRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numbersouscription2016),"unsatisfied":float(len(unsatisfied.index)/numbersouscription2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistsouscriptionRequests2017=dflistsouscriptionRequests[dflistsouscriptionRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numbersouscription2017=len(dflistsouscriptionRequests2017.index)
    
    satisfied=dflistsouscriptionRequests2017.loc[dflistsouscriptionRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistsouscriptionRequests2017.loc[dflistsouscriptionRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numbersouscription2017),"unsatisfied":float(len(unsatisfied.index)/numbersouscription2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=df.at['2015', 'satisfied']
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('souscription_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_souscription.png')
    
'''df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_RESILIATION_2015_2016_2017.csv")  as resiliationRequests:
    readerresiliationRequests = csv.reader(resiliationRequests, delimiter=";")
    fieldsresiliationRequests = next(readerresiliationRequests)
    fieldsresiliationRequests = next(readerresiliationRequests)
    listresiliationRequests= list(readerresiliationRequests)
    
    dflistresiliationRequests = pd.DataFrame(listresiliationRequests, columns=fieldsresiliationRequests)
    dflistresiliationRequests.rename(columns={'Suite Ã  cette expÃ©rience et sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistresiliationRequests2015=dflistresiliationRequests[dflistresiliationRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numberresiliation2015=len(dflistresiliationRequests2015.index)
    
    dflistresiliationRequests2015.loc[dflistresiliationRequests2015['note'].isin(goodRate)]
    satisfied=dflistresiliationRequests2015.loc[dflistresiliationRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistresiliationRequests2015.loc[dflistresiliationRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberresiliation2015),"unsatisfied":float(len(unsatisfied.index)/numberresiliation2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistresiliationRequests2016=dflistresiliationRequests[dflistresiliationRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberresiliation2016=len(dflistresiliationRequests2016.index)
    
    satisfied=dflistresiliationRequests2016.loc[dflistresiliationRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistresiliationRequests2016.loc[dflistresiliationRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberresiliation2016),"unsatisfied":float(len(unsatisfied.index)/numberresiliation2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistresiliationRequests2017=dflistresiliationRequests[dflistresiliationRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberresiliation2017=len(dflistresiliationRequests2017.index)
    
    satisfied=dflistresiliationRequests2017.loc[dflistresiliationRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistresiliationRequests2017.loc[dflistresiliationRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberresiliation2017),"unsatisfied":float(len(unsatisfied.index)/numberresiliation2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('resiliation_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_resiliation.png')
'''

df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_SUIVI_PROACTIF_2016_2017.csv")  as ProactifRequests:
    readerProactifRequests = csv.reader(ProactifRequests, delimiter=";")
    fieldsProactifRequests = next(readerProactifRequests)
    fieldsProactifRequests = next(readerProactifRequests)
    listProactifRequests= list(readerProactifRequests)
    
    dflistProactifRequests = pd.DataFrame(listProactifRequests, columns=fieldsProactifRequests)
    dflistProactifRequests.rename(columns={'Suite Ã  cette expÃ©rience et sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
  
    
    dflistProactifRequests2016=dflistProactifRequests[dflistProactifRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberProactif2016=len(dflistProactifRequests2016.index)
    
    satisfied=dflistProactifRequests2016.loc[dflistProactifRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistProactifRequests2016.loc[dflistProactifRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberProactif2016),"unsatisfied":float(len(unsatisfied.index)/numberProactif2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistProactifRequests2017=dflistProactifRequests[dflistProactifRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberProactif2017=len(dflistProactifRequests2017.index)
    
    satisfied=dflistProactifRequests2017.loc[dflistProactifRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistProactifRequests2017.loc[dflistProactifRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberProactif2017),"unsatisfied":float(len(unsatisfied.index)/numberProactif2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=0
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('Proactif_DEMANDE_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_Proactif.png')
        

df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_AUTO_BDG_2015_2016_2017.csv")  as autoBDGRequests:
    readerautoBDGRequests = csv.reader(autoBDGRequests, delimiter=";")
    fieldsautoBDGRequests = next(readerautoBDGRequests)
    fieldsautoBDGRequests = next(readerautoBDGRequests)
    listautoBDGRequests= list(readerautoBDGRequests)
    
    dflistautoBDGRequests = pd.DataFrame(listautoBDGRequests, columns=fieldsautoBDGRequests)
    dflistautoBDGRequests.rename(columns={'Suite Ã  cette expÃ©rience et sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistautoBDGRequests2015=dflistautoBDGRequests[dflistautoBDGRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numberautoBDG2015=len(dflistautoBDGRequests2015.index)
    
    dflistautoBDGRequests2015.loc[dflistautoBDGRequests2015['note'].isin(goodRate)]
    satisfied=dflistautoBDGRequests2015.loc[dflistautoBDGRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistautoBDGRequests2015.loc[dflistautoBDGRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberautoBDG2015),"unsatisfied":float(len(unsatisfied.index)/numberautoBDG2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistautoBDGRequests2016=dflistautoBDGRequests[dflistautoBDGRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberautoBDG2016=len(dflistautoBDGRequests2016.index)
    
    satisfied=dflistautoBDGRequests2016.loc[dflistautoBDGRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistautoBDGRequests2016.loc[dflistautoBDGRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberautoBDG2016),"unsatisfied":float(len(unsatisfied.index)/numberautoBDG2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistautoBDGRequests2017=dflistautoBDGRequests[dflistautoBDGRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberautoBDG2017=len(dflistautoBDGRequests2017.index)
    
    satisfied=dflistautoBDGRequests2017.loc[dflistautoBDGRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistautoBDGRequests2017.loc[dflistautoBDGRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberautoBDG2017),"unsatisfied":float(len(unsatisfied.index)/numberautoBDG2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=df.at['2015', 'satisfied']
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('autoBDG_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_autoBDG.png')


df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_AUTO_CLASSIQUE_2015_2016_2017.csv")  as autoClassiqueRequests:
    readerautoClassiqueRequests = csv.reader(autoClassiqueRequests, delimiter=";")
    fieldsautoClassiqueRequests = next(readerautoClassiqueRequests)
    fieldsautoClassiqueRequests = next(readerautoClassiqueRequests)
    listautoClassiqueRequests= list(readerautoClassiqueRequests)
    
    dflistautoClassiqueRequests = pd.DataFrame(listautoClassiqueRequests, columns=fieldsautoClassiqueRequests)
    dflistautoClassiqueRequests.rename(columns={'Suite Ã  cette expÃ©rience et sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistautoClassiqueRequests2015=dflistautoClassiqueRequests[dflistautoClassiqueRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numberautoClassique2015=len(dflistautoClassiqueRequests2015.index)
    
    dflistautoClassiqueRequests2015.loc[dflistautoClassiqueRequests2015['note'].isin(goodRate)]
    satisfied=dflistautoClassiqueRequests2015.loc[dflistautoClassiqueRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistautoClassiqueRequests2015.loc[dflistautoClassiqueRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberautoClassique2015),"unsatisfied":float(len(unsatisfied.index)/numberautoClassique2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistautoClassiqueRequests2016=dflistautoClassiqueRequests[dflistautoClassiqueRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberautoClassique2016=len(dflistautoClassiqueRequests2016.index)
    
    satisfied=dflistautoClassiqueRequests2016.loc[dflistautoClassiqueRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistautoClassiqueRequests2016.loc[dflistautoClassiqueRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberautoClassique2016),"unsatisfied":float(len(unsatisfied.index)/numberautoClassique2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistautoClassiqueRequests2017=dflistautoClassiqueRequests[dflistautoClassiqueRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberautoClassique2017=len(dflistautoClassiqueRequests2017.index)
    
    satisfied=dflistautoClassiqueRequests2017.loc[dflistautoClassiqueRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistautoClassiqueRequests2017.loc[dflistautoClassiqueRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberautoClassique2017),"unsatisfied":float(len(unsatisfied.index)/numberautoClassique2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=df.at['2015', 'satisfied']
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('autoClassique_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_autoClassique.png')


        

df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_AUTOPRESTO_2015_2016_2017.csv")  as autoPrestoRequests:
    readerautoPrestoRequests = csv.reader(autoPrestoRequests, delimiter=";")
    fieldsautoPrestoRequests = next(readerautoPrestoRequests)
    fieldsautoPrestoRequests = next(readerautoPrestoRequests)
    listautoPrestoRequests= list(readerautoPrestoRequests)
    
    dflistautoPrestoRequests = pd.DataFrame(listautoPrestoRequests, columns=fieldsautoPrestoRequests)
    dflistautoPrestoRequests.rename(columns={'Suite Ã  cette expÃ©rience et sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistautoPrestoRequests2015=dflistautoPrestoRequests[dflistautoPrestoRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numberautoPresto2015=len(dflistautoPrestoRequests2015.index)
    
    dflistautoPrestoRequests2015.loc[dflistautoPrestoRequests2015['note'].isin(goodRate)]
    satisfied=dflistautoPrestoRequests2015.loc[dflistautoPrestoRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistautoPrestoRequests2015.loc[dflistautoPrestoRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberautoPresto2015),"unsatisfied":float(len(unsatisfied.index)/numberautoPresto2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistautoPrestoRequests2016=dflistautoPrestoRequests[dflistautoPrestoRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberautoPresto2016=len(dflistautoPrestoRequests2016.index)
    
    satisfied=dflistautoPrestoRequests2016.loc[dflistautoPrestoRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistautoPrestoRequests2016.loc[dflistautoPrestoRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberautoPresto2016),"unsatisfied":float(len(unsatisfied.index)/numberautoPresto2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistautoPrestoRequests2017=dflistautoPrestoRequests[dflistautoPrestoRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberautoPresto2017=len(dflistautoPrestoRequests2017.index)
    
    satisfied=dflistautoPrestoRequests2017.loc[dflistautoPrestoRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistautoPrestoRequests2017.loc[dflistautoPrestoRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberautoPresto2017),"unsatisfied":float(len(unsatisfied.index)/numberautoPresto2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=df.at['2015', 'satisfied']
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('autoPresto_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_autoPresto.png')
    
df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_AUTO_CLASSIQUE_TMA_2016_2017.csv")  as autoClassiqueTMARequests:
    readerautoClassiqueTMARequests = csv.reader(autoClassiqueTMARequests, delimiter=";")
    fieldsautoClassiqueTMARequests = next(readerautoClassiqueTMARequests)
    fieldsautoClassiqueTMARequests = next(readerautoClassiqueTMARequests)
    listautoClassiqueTMARequests= list(readerautoClassiqueTMARequests)
    
    dflistautoClassiqueTMARequests = pd.DataFrame(listautoClassiqueTMARequests, columns=fieldsautoClassiqueTMARequests)
    dflistautoClassiqueTMARequests.rename(columns={'Suite Ã  cette expÃ©rience et sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
  
    
    dflistautoClassiqueTMARequests2016=dflistautoClassiqueTMARequests[dflistautoClassiqueTMARequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberautoClassiqueTMA2016=len(dflistautoClassiqueTMARequests2016.index)
    
    satisfied=dflistautoClassiqueTMARequests2016.loc[dflistautoClassiqueTMARequests2016['note'].isin(goodRate)]
    unsatisfied=dflistautoClassiqueTMARequests2016.loc[dflistautoClassiqueTMARequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberautoClassiqueTMA2016),"unsatisfied":float(len(unsatisfied.index)/numberautoClassiqueTMA2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistautoClassiqueTMARequests2017=dflistautoClassiqueTMARequests[dflistautoClassiqueTMARequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberautoClassiqueTMA2017=len(dflistautoClassiqueTMARequests2017.index)
    
    satisfied=dflistautoClassiqueTMARequests2017.loc[dflistautoClassiqueTMARequests2017['note'].isin(goodRate)]
    unsatisfied=dflistautoClassiqueTMARequests2017.loc[dflistautoClassiqueTMARequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberautoClassiqueTMA2017),"unsatisfied":float(len(unsatisfied.index)/numberautoClassiqueTMA2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=0
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('autoClassiqueTMA_DEMANDE_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_autoClassiqueTMA.png')

df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_AUTO_TMA_BDG_2016_2017.csv")  as autoTMABDGRequests:
    readerautoTMABDGRequests = csv.reader(autoTMABDGRequests, delimiter=";")
    fieldsautoTMABDGRequests = next(readerautoTMABDGRequests)
    fieldsautoTMABDGRequests = next(readerautoTMABDGRequests)
    listautoTMABDGRequests= list(readerautoTMABDGRequests)
    
    dflistautoTMABDGRequests = pd.DataFrame(listautoTMABDGRequests, columns=fieldsautoTMABDGRequests)
    dflistautoTMABDGRequests.rename(columns={'Suite Ã  cette expÃ©rience et sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
  
    
    dflistautoTMABDGRequests2016=dflistautoTMABDGRequests[dflistautoTMABDGRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberautoTMABDG2016=len(dflistautoTMABDGRequests2016.index)
    
    satisfied=dflistautoTMABDGRequests2016.loc[dflistautoTMABDGRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistautoTMABDGRequests2016.loc[dflistautoTMABDGRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberautoTMABDG2016),"unsatisfied":float(len(unsatisfied.index)/numberautoTMABDG2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistautoTMABDGRequests2017=dflistautoTMABDGRequests[dflistautoTMABDGRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberautoTMABDG2017=len(dflistautoTMABDGRequests2017.index)
    
    satisfied=dflistautoTMABDGRequests2017.loc[dflistautoTMABDGRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistautoTMABDGRequests2017.loc[dflistautoTMABDGRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberautoTMABDG2017),"unsatisfied":float(len(unsatisfied.index)/numberautoTMABDG2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=0
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('autoTMABDG_DEMANDE_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_autoTMABDG.png')
    
df = pd.DataFrame([])  
with open ("../big_data_project_confidential/SATISFACTION_MODIFICATION_2015_2016_2017.csv")  as ModificationRequests:
    readerModificationRequests = csv.reader(ModificationRequests, delimiter=";")
    fieldsModificationRequests = next(readerModificationRequests)
    fieldsModificationRequests = next(readerModificationRequests)
    listModificationRequests= list(readerModificationRequests)
    
    dflistModificationRequests = pd.DataFrame(listModificationRequests, columns=fieldsModificationRequests)
    dflistModificationRequests.rename(columns={'Suite Ã  cette expÃ©rience et sur une Ã©chelle de 0 Ã  10, dans quelle mesure recommanderiez-vous Groupama Ã  un proche ou Ã  un collÃ¨gue ? Â 0 signifie Â« certainement pas Â» et 10 signifie Â« sans hÃ©sitation Â»': "note"},inplace=True)
    
    dflistModificationRequests2015=dflistModificationRequests[dflistModificationRequests['Date de rÃ©ponse'].str.contains("2015") == True]
    numberModification2015=len(dflistModificationRequests2015.index)
    
    dflistModificationRequests2015.loc[dflistModificationRequests2015['note'].isin(goodRate)]
    satisfied=dflistModificationRequests2015.loc[dflistModificationRequests2015['note'].isin(goodRate)]
    unsatisfied=dflistModificationRequests2015.loc[dflistModificationRequests2015['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberModification2015),"unsatisfied":float(len(unsatisfied.index)/numberModification2015)},index=['2015'], columns=["satisfied","unsatisfied"]))
    
    
    dflistModificationRequests2016=dflistModificationRequests[dflistModificationRequests['Date de rÃ©ponse'].str.contains("2016") == True]
    numberModification2016=len(dflistModificationRequests2016.index)
    
    satisfied=dflistModificationRequests2016.loc[dflistModificationRequests2016['note'].isin(goodRate)]
    unsatisfied=dflistModificationRequests2016.loc[dflistModificationRequests2016['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberModification2016),"unsatisfied":float(len(unsatisfied.index)/numberModification2016)},index=['2016'], columns=["satisfied","unsatisfied"]))
    
    dflistModificationRequests2017=dflistModificationRequests[dflistModificationRequests['Date de rÃ©ponse'].str.contains("2017") == True]
    numberModification2017=len(dflistModificationRequests2017.index)
    
    satisfied=dflistModificationRequests2017.loc[dflistModificationRequests2017['note'].isin(goodRate)]
    unsatisfied=dflistModificationRequests2017.loc[dflistModificationRequests2017['note'].isin(badRate)]
    df=df.append(pd.DataFrame({"satisfied":float(len(satisfied.index)/numberModification2017),"unsatisfied":float(len(unsatisfied.index)/numberModification2017)},index=['2017'], columns=["satisfied","unsatisfied"]))
    satisfactionRequestsYears['2015']+=0
    satisfactionRequestsYears['2016']+=df.at['2016', 'satisfied']
    satisfactionRequestsYears['2017']+=df.at['2017', 'satisfied']
    x=['2015','2016','2017']
    plt.ylabel('Pourcentages')
    plt.title('Modification_DEMANDE_2015_2016_2017 Evolution')
    ax = plt.subplot(111)
    ax.bar(x,df['satisfied'],color = 'b', width = 0.25,align='center')
    ax.bar(x,df['unsatisfied'],color = 'g', width = 0.25,align='center')
    ax.legend(["satisfaction","dissatisfaction"])
    
    #plt.show()
    plt.savefig('plots/demande_Modification.png')
satisfactionRequestsYears['2015']=satisfactionRequestsYears['2015']*100/12
satisfactionRequestsYears['2016']=satisfactionRequestsYears['2016']*100/15
satisfactionRequestsYears['2017']=satisfactionRequestsYears['2017']*100/15

print(satisfactionRequestsYears)
plot=plt.plot(satisfactionRequestsYears.keys(), satisfactionRequestsYears.values(),color='b')
#plot=plt.plot(incomes.keys(), incomes.values(),color='r')
plt.title('global satisfaction')
plt.xlabel('Years')
plt.ylabel('satisfaction(\%)')  
plt.savefig('plots/globalsatisfaction.png')
#plt.show()
print(incomes)
plot=plt.plot(satisfactionRequestsYears.keys(), satisfactionRequestsYears.values(),color='b')
plot=plt.plot(incomes.keys(), incomes.values(),color='r')
plt.title('global satisfaction')
plt.xlabel('Years')
plt.ylabel('satisfaction(\%)')  
plt.savefig('plots/globalsatisfactionIncome.png')
