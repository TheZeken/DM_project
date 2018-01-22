library(tidyr)
library(plyr)
library(dplyr)
library(readr)
library(arules)

#reading the data
path = 'D:/Study/Semester 3/DM for Big Data/Project/big_data_project_confidential/'

client_table = read_csv2(paste(path,"BASE_Donnees_Clients.csv", sep= ''))
complaint_table = read_csv2(paste(path,"BASE_Reclamations_clients.csv",sep = ''))


survey1 = read_csv2(paste(path,"SATISFACTION_AUTO_BDG_2015_2016_2017.csv", sep= ''))
survey2 = read_csv2(paste(path,"SATISFACTION_AUTO_CLASSIQUE_2015_2016_2017.csv",sep = ''))
survey3 = read_csv2(paste(path,"SATISFACTION_AUTO_CLASSIQUE_TMA_2016_2017.csv",sep = ''))
survey4 = read_csv2(paste(path,"SATISFACTION_AUTOPRESTO_2015_2016_2017.csv",sep = ''))
survey5 = read_csv2(paste(path,"SATISFACTION_AUTO_TMA_BDG_2016_2017.csv",sep = ''))
survey6 = read_csv2(paste(path,"SATISFACTION_DAB_2015_2016_2107.csv",sep = ''))
survey7 = read_csv2(paste(path,"SATISFACTION_DEMANDE_2015_2016_2017.csv",sep = ''))
survey8 = read_csv2(paste(path,"SATISFACTION_DENTAIRE_NON_PARTENAIRE_2015_2016_2017.csv",sep = ''))
survey9= read_csv2(paste(path,"SATISFACTION_DENTAIRE_PARTENAIRE_2015_2016_2017.csv",sep = ''))
survey10= read_csv2(paste(path,"SATISFACTION_MODIFICATION_2015_2016_2017.csv",sep = ''))
survey11= read_csv2(paste(path,"SATISFACTION_OPTIQUE_NON_PARTENAIRE_2015_2016_2017.csv",sep = ''))

survey13= read_csv2(paste(path,"SATISFACTION_RECLAMATION_2015_2016_2107.csv",sep = ''))
survey15= read_csv2(paste(path,"SATISFACTION_SOUSCRIPTION_2015_2016_2017.csv",sep = ''))
survey16= read_csv2(paste(path,"SATISFACTION_SUIVI_PROACTIF_2016_2017.csv",sep = ''))


#combining all the survey data t
all_survey = (survey1[2:nrow(survey1),c('Q1','Meta_donnee 3')])
all_survey = rbind(all_survey,survey2[2:nrow(survey2),c('Q1','Meta_donnee 3')])
all_survey = rbind(all_survey,survey3[2:nrow(survey3),c('Q1','Meta_donnee 3')])
all_survey = rbind(all_survey,survey4[2:nrow(survey4),c('Q1','Meta_donnee 3')])
all_survey = rbind(all_survey,survey5[2:nrow(survey5),c('Q1','Meta_donnee 3')])
all_survey = rbind(all_survey,survey6[2:nrow(survey6),c('Q1','Meta_donnee 3')])
all_survey = rbind(all_survey,survey7[2:nrow(survey7),c('Q1','Meta_donnee 3')])
all_survey = rbind(all_survey,survey8[2:nrow(survey8),c('Q1','Meta_donnee 3')])
all_survey = rbind(all_survey,survey9[2:nrow(survey9),c('Q1','Meta_donnee 3')])
all_survey = rbind(all_survey,survey10[2:nrow(survey10),c('Q1','Meta_donnee 3')])
all_survey = rbind(all_survey,survey11[2:nrow(survey11),c('Q1','Meta_donnee 3')])
all_survey = rbind(all_survey,survey13[2:nrow(survey13),c('Q1','Meta_donnee 3')])
all_survey = rbind(all_survey,survey15[2:nrow(survey15),c('Q1','Meta_donnee 3')])
all_survey = rbind(all_survey,survey16[2:nrow(survey16),c('Q1','Meta_donnee 3')])

#categorizing surveys


all_survey[,'score'] = all_survey$Q1
all_survey = drop_na(all_survey,'Q1')
temp1=all_survey$Q1<=7
temp2=all_survey$Q1>=7
all_survey$score[temp1]='not statisfied'
all_survey$score[temp2]='statisfied'


#Discarding the value of Q1 column

all_survey = all_survey[,c('score','Meta_donnee 3')]
colnames(all_survey) = c('flag','ID_GRC')


#Combining all the needed information for Q2.1
all_survey=drop_na(all_survey,'ID_GRC')
all_survey=drop_na(all_survey,'flag')

'''clients=client_table$ID_GRC==all_survey$ID_GRC
r=list()
for( i in 0:length(all_survey$ID_GRC)){
a=all_survey[i,]
b=client_table[client_table$ID_GRC==a,]
c(r,b)
}
'''



all_information = client_table[,c('ID_GRC','TRANCHE_AGE','SEXE','NATURE_PERSONNE',
                                  'MARCHE_PSO','TYPOLOGIE')]



all_information = merge(x=all_information, y=all_survey, by='ID_GRC', all.x=TRUE )
formatted = drop_na(all_information,'flag')
formatted=formatted[formatted$flag=='not statisfied',]

#sort
formatted = formatted[order(formatted$ID_GRC),]
#numeric id
formatted$id = as.numeric(formatted$ID_GRC)
#Remove duplicates
formatted = distinct(formatted)

#Dropping Rows with null values
formatted[grepl('NULL', formatted$TRANCHE_AGE),] = NA
formatted1=formatted[complete.cases(formatted), ]
#formatted1=na.omit(formatted,cols=c("TRANCHE_AGE", "SEXE","NATURE_PERSONNE","MARCHE_PSO","TYPOLOGIE"))

formatted1=formatted1[,c(1,2,3,4,5,6,7)]







formatted1 = formatted1[order(formatted1$ID_GRC),]
#numeric id
formatted1$ID_GRC = as.numeric(formatted1$ID_GRC)
#Remove duplicates
formatted1 = distinct(formatted1)

#formatted1[,2]=as.numeric(as.factor(formatted1[,2]))
#formatted1[,3]=as.numeric(as.factor(formatted1[,3]))
#formatted1[,4]=as.numeric(as.factor(formatted1[,4]))
#formatted1[,5]=as.numeric(as.factor(formatted1[,5]))
#formatted1[,6]=as.numeric(as.factor(formatted1[,6]))

#Removing the flag column
formatted1=formatted1[,c(1,2,3,4,5,6)]



write.csv2(formatted1,'D:/apriori_table.csv',row.names = FALSE)
#dis=data.frame()
#dis[,1]=discretize(formatted1[,1])

formatted1= read.transactions(file="D:/apriori_table.csv",
                               rm.duplicates = TRUE, format="basket",
                               sep=";", cols = NULL)



#for (i in 2:6){formatted1[,i]=discretize(formatted1[,i])}
complaint_rules = apriori(formatted1,parameter = list(supp = 0.01,conf = 0.5, target="rules"))
complaint_rules = as(complaint_rules,"data.frame")
View(complaint_rules)





#Q2



library(tm)


docs=VCorpus(VectorSource(complaint_table$COMMENTAIRE_DEMANDE))
summary(docs)

inspect(docs[1])
writeLines(as.character(docs[1])) #To read the file on console

#Removing Punctuation
docs=tm_map(docs,removePunctuation)

#Removing Numbers
docs=tm_map(docs,removeNumbers)

#Converting to lowercase
docs=tm_map(docs,tolower)
docs=tm_map(docs,PlainTextDocument)
DocsCopy=docs

#Removing Stopwords
docs=tm_map(docs,removeWords,stopwords("french"))
docs=tm_map(docs,PlainTextDocument)


#Removing Particular Words
docs=tm_map(docs,removeWords,c("bonjour","xxx","mme"))



#Stemming/Removing the common word endings
docs_st <- tm_map(docs, stemDocument)   
docs <- tm_map(docs_st, PlainTextDocument)

#Following lines not working properly
#docs_stc <- tm_map(docs_st, stemCompletion, dictionary = DocsCopy, lazy=TRUE)
#docs_stc <- tm_map(docs_stc, PlainTextDocument)
#writeLines(as.character(docs_stc[1]))


#docs=docs_stc

#Stripping unnecessary whitespace
docs=tm_map(docs,stripWhitespace)
docs=tm_map(docs,PlainTextDocument)


#Stage the Data
dtm=DocumentTermMatrix(docs)
inspect(dtm)

#taking transpose of the matrix
tdm=TermDocumentMatrix(docs)

#Organize terms by frequency
freq=colSums(as.matrix(dtm))
freq
ord=order(freq)


#removing sparse terms
dtms=removeSparseTerms(dtm,0.99)
dtms

#frequency of remaining terms
freq <- colSums(as.matrix(dtm))


freq <- colSums(as.matrix(dtms))   
freq



#All terms that appear frequently 50 or more times
wf=findFreqTerms(dtm,lowfreq = 50)
wf

#Another way to do it
wf <- data.frame(word=names(freq), freq=freq)   
head(wf) 


#Plotting word frequencies
library(ggplot2)

p = ggplot(subset(wf, freq>50), aes(x = reorder(word, -freq), y = freq)) +
  geom_bar(stat = "identity") + 
  theme(axis.text.x=element_text(angle=45, hjust=1))
p

#Finding correalted terms
findAssocs(dtm,c("country","american"), corlimit = 0.85)


wordcloud::wordcloud(names(freq),freq,min.freq = 25)
