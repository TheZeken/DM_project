# Load CSV files using the function read.csv
#AUTO
auto_bdg_15_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_AUTO_BDG_2015_2016_2017.csv",sep = ";")
auto_class_15_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_AUTO_CLASSIQUE_2015_2016_2017.csv",sep = ";")
auto_class_tma_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_AUTO_CLASSIQUE_TMA_2016_2017.csv",sep = ";")
auto_tma_bdg_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_AUTO_TMA_BDG_2016_2017.csv",sep = ";")
auto_presto_15_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_AUTOPRESTO_2015_2016_2017.csv",sep = ";")

#DAB
dab_15_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_DAB_2015_2016_2107.csv",sep = ";")

#Dentaire
dent_non_part_15_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_DENTAIRE_NON_PARTENAIRE_2015_2016_2017.csv",sep = ";")
dent_part_15_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_DENTAIRE_PARTENAIRE_2015_2016_2017.csv",sep = ";")

#Modification
mod_15_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_MODIFICATION_2015_2016_2017.csv",sep = ";")

#Optique
opt_non_part_15_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_OPTIQUE_NON_PARTENAIRE_2015_2016_2017.csv",sep = ";")
opt_part_15_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_OPTIQUE_PARTENAIRE_2015_2016_2017.csv",sep = ";")

#Reclamation
reclam_15_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_RECLAMATION_2015_2016_2107.csv",sep = ";")

#resilation
resil_15_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_RESILIATION_2015_2016_2017.csv",sep = ";")

#Souscription
sous_15_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_SOUSCRIPTION_2015_2016_2017.csv",sep = ";")

#suivi proacif
suiv_15_16_17 <- read.csv("C:/Users/jerem/Desktop/M2/DM_project/big_data_project_confidential/satisfaction/SATISFACTION_SUIVI_PROACTIF_2016_2017.csv",sep = ";")

#First experimentation
library(ggplot2)     # Implementation of the Grammar of Graphics

dataset_grades_glob <- suiv_15_16_17[-c(1),'Q1',drop=FALSE]
dataset_grades_glob <- rbind(dataset_grades_glob,sous_15_16_17[-c(1),'Q1',drop=FALSE])
dataset_grades_glob <- rbind(dataset_grades_glob,reclam_15_16_17[-c(1),'Q1',drop=FALSE])
dataset_grades_glob <- rbind(dataset_grades_glob,opt_non_part_15_16_17[-c(1),'Q1',drop=FALSE])
dataset_grades_glob <- rbind(dataset_grades_glob,dent_part_15_16_17[-c(1),'Q1',drop=FALSE])
dataset_grades_glob <- rbind(dataset_grades_glob,dent_non_part_15_16_17[-c(1),'Q1',drop=FALSE])
dataset_grades_glob <- rbind(dataset_grades_glob,dab_15_16_17[-c(1),'Q1',drop=FALSE])
dataset_grades_glob <- rbind(dataset_grades_glob,auto_presto_15_16_17[-c(1),'Q1',drop=FALSE])
dataset_grades_glob <- rbind(dataset_grades_glob,auto_tma_bdg_16_17[-c(1),'Q1',drop=FALSE])
dataset_grades_glob <- rbind(dataset_grades_glob,auto_class_tma_16_17[-c(1),'Q1',drop=FALSE])
dataset_grades_glob <- rbind(dataset_grades_glob,auto_class_15_16_17[-c(1),'Q1',drop=FALSE])
dataset_grades_glob <- rbind(dataset_grades_glob,auto_bdg_15_16_17[-c(1),'Q1',drop=FALSE])

#We plot the repartition of the grades
qplot(dataset_grades_glob$Q1, xlab= "Grades", main= "Grades for years 2015/2016/2017") + 
  scale_y_continuous("Occurences")+
  scale_x_discrete(limits=c(1:10))

#Mean of the whole dataset
mean(as.numeric(dataset_grades_glob$Q1))

#Mean per category
#Suivies
dataset_grades <- suiv_15_16_17[-c(1),'Q1',drop=FALSE]
mean(as.numeric(dataset_grades$Q1))

#Souscriptions
dataset_grades <- sous_15_16_17[-c(1),'Q1',drop=FALSE]
mean(as.numeric(dataset_grades$Q1))

#reclamation
dataset_grades <- reclam_15_16_17[-c(1),'Q1',drop=FALSE]
mean(as.numeric(dataset_grades$Q1))

#Optique
dataset_grades <- opt_non_part_15_16_17[-c(1),'Q1',drop=FALSE]
dataset_grades <- rbind(dataset_grades,opt_part_15_16_17[-c(1),'Q1',drop=FALSE])
mean(as.numeric(dataset_grades$Q1))

#Dentaire
dataset_grades <- dent_non_part_15_16_17[-c(1),'Q1',drop=FALSE]
dataset_grades <- rbind(dataset_grades,dent_part_15_16_17[-c(1),'Q1',drop=FALSE])
mean(as.numeric(dataset_grades$Q1))

#Modification
dataset_grades <- mod_15_16_17[-c(1),'Q1',drop=FALSE]
mean(as.numeric(dataset_grades$Q1))

#Auto
dataset_grades <- auto_presto_15_16_17[-c(1),'Q1',drop=FALSE]
dataset_grades <- rbind(dataset_grades,auto_tma_bdg_16_17[-c(1),'Q1',drop=FALSE])
dataset_grades <- rbind(dataset_grades,auto_class_tma_16_17[-c(1),'Q1',drop=FALSE])
dataset_grades <- rbind(dataset_grades,auto_class_15_16_17[-c(1),'Q1',drop=FALSE])
dataset_grades <- rbind(dataset_grades,auto_bdg_15_16_17[-c(1),'Q1',drop=FALSE])
mean(as.numeric(dataset_grades$Q1))

dataset_grades <- auto_presto_15_16_17[-c(1),'Q1',drop=FALSE]
mean(as.numeric(dataset_grades$Q1))

dataset_grades <- auto_tma_bdg_16_17[-c(1),'Q1',drop=FALSE]
mean(as.numeric(dataset_grades$Q1))

dataset_grades <- auto_class_tma_16_17[-c(1),'Q1',drop=FALSE]
mean(as.numeric(dataset_grades$Q1))

dataset_grades <- auto_bdg_15_16_17[-c(1),'Q1',drop=FALSE]
mean(as.numeric(dataset_grades$Q1))

dataset_grades <- auto_class_15_16_17[-c(1),'Q1',drop=FALSE]
mean(as.numeric(dataset_grades$Q1))

#Evolution grades years
#2015
dataset_grades_glob_15 <- subset(sous_15_16_17, as.Date(sous_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)
dataset_grades_glob_15 <- rbind(dataset_grades_glob_15,(subset(suiv_15_16_17, as.Date(suiv_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_15 <- rbind(dataset_grades_glob_15,(subset(reclam_15_16_17, as.Date(reclam_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_15 <- rbind(dataset_grades_glob_15,(subset(opt_non_part_15_16_17, as.Date(opt_non_part_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_15 <- rbind(dataset_grades_glob_15,(subset(opt_part_15_16_17, as.Date(opt_part_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_15 <- rbind(dataset_grades_glob_15,(subset(dent_part_15_16_17, as.Date(dent_part_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_15 <- rbind(dataset_grades_glob_15,(subset(dent_non_part_15_16_17, as.Date(dent_non_part_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_15 <- rbind(dataset_grades_glob_15,(subset(dab_15_16_17, as.Date(dab_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_15 <- rbind(dataset_grades_glob_15,(subset(auto_presto_15_16_17, as.Date(auto_presto_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_15 <- rbind(dataset_grades_glob_15,(subset(auto_tma_bdg_16_17, as.Date(auto_tma_bdg_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_15 <- rbind(dataset_grades_glob_15,(subset(auto_class_tma_16_17, as.Date(auto_class_tma_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_15 <- rbind(dataset_grades_glob_15,(subset(auto_class_15_16_17, as.Date(auto_class_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_15 <- rbind(dataset_grades_glob_15,(subset(auto_bdg_15_16_17, as.Date(auto_bdg_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)))

mean(as.numeric(dataset_grades_glob_15$Q1))

#2016
dataset_grades_glob_15_16 <- subset(sous_15_16_17, as.Date(sous_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2017", format = "%d/%m/%Y") , select = Date.de.rÃ.ponse:Q1)
dataset_grades_glob_15_16 <- rbind(dataset_grades_glob_15_16,(subset(suiv_15_16_17, as.Date(suiv_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2017", format = "%d/%m/%Y") , select = Date.de.rÃ.ponse:Q1)))
dataset_grades_glob_15_16 <- rbind(dataset_grades_glob_15_16,(subset(reclam_15_16_17, as.Date(reclam_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2017", format = "%d/%m/%Y") , select = Date.de.rÃ.ponse:Q1)))
dataset_grades_glob_15_16 <- rbind(dataset_grades_glob_15_16,(subset(opt_non_part_15_16_17, as.Date(opt_non_part_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2017", format = "%d/%m/%Y") , select = Date.de.rÃ.ponse:Q1)))
dataset_grades_glob_15_16 <- rbind(dataset_grades_glob_15_16,(subset(opt_part_15_16_17, as.Date(opt_part_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2017", format = "%d/%m/%Y") , select = Date.de.rÃ.ponse:Q1)))
dataset_grades_glob_15_16 <- rbind(dataset_grades_glob_15_16,(subset(dent_part_15_16_17, as.Date(dent_part_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2017", format = "%d/%m/%Y") , select = Date.de.rÃ.ponse:Q1)))
dataset_grades_glob_15_16 <- rbind(dataset_grades_glob_15_16,(subset(dent_non_part_15_16_17, as.Date(dent_non_part_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2017", format = "%d/%m/%Y") , select = Date.de.rÃ.ponse:Q1)))
dataset_grades_glob_15_16 <- rbind(dataset_grades_glob_15_16,(subset(dab_15_16_17, as.Date(dab_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2017", format = "%d/%m/%Y") , select = Date.de.rÃ.ponse:Q1)))
dataset_grades_glob_15_16 <- rbind(dataset_grades_glob_15_16,(subset(auto_presto_15_16_17, as.Date(auto_presto_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2017", format = "%d/%m/%Y") , select = Date.de.rÃ.ponse:Q1)))
dataset_grades_glob_15_16 <- rbind(dataset_grades_glob_15_16,(subset(auto_tma_bdg_16_17, as.Date(auto_tma_bdg_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2017", format = "%d/%m/%Y") , select = Date.de.rÃ.ponse:Q1)))
dataset_grades_glob_15_16 <- rbind(dataset_grades_glob_15_16,(subset(auto_class_tma_16_17, as.Date(auto_class_tma_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2017", format = "%d/%m/%Y") , select = Date.de.rÃ.ponse:Q1)))
dataset_grades_glob_15_16 <- rbind(dataset_grades_glob_15_16,(subset(auto_class_15_16_17, as.Date(auto_class_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2017", format = "%d/%m/%Y") , select = Date.de.rÃ.ponse:Q1)))
dataset_grades_glob_15_16 <- rbind(dataset_grades_glob_15_16,(subset(auto_bdg_15_16_17, as.Date(auto_bdg_15_16_17[,1], format = "%d/%m/%Y") < as.Date("01/01/2017", format = "%d/%m/%Y") , select = Date.de.rÃ.ponse:Q1)))

dataset_grades_glob_16 <- subset(dataset_grades_glob_15_16, as.Date(dataset_grades_glob_15_16[,1], format = "%d/%m/%Y") >= as.Date("01/01/2016", format = "%d/%m/%Y"), select = Q1)

mean(as.numeric(dataset_grades_glob_16$Q1))

#2017
dataset_grades_glob_17 <- subset(sous_15_16_17, as.Date(sous_15_16_17[,1], format = "%d/%m/%Y") > as.Date("31/12/2016", format = "%d/%m/%Y"), select = Q1)
dataset_grades_glob_17 <- rbind(dataset_grades_glob_17,(subset(suiv_15_16_17, as.Date(suiv_15_16_17[,1], format = "%d/%m/%Y") > as.Date("31/12/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_17 <- rbind(dataset_grades_glob_17,(subset(reclam_15_16_17, as.Date(reclam_15_16_17[,1], format = "%d/%m/%Y") > as.Date("31/12/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_17 <- rbind(dataset_grades_glob_17,(subset(opt_non_part_15_16_17, as.Date(opt_non_part_15_16_17[,1], format = "%d/%m/%Y") > as.Date("31/12/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_17 <- rbind(dataset_grades_glob_17,(subset(opt_part_15_16_17, as.Date(opt_part_15_16_17[,1], format = "%d/%m/%Y") > as.Date("31/12/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_17 <- rbind(dataset_grades_glob_17,(subset(dent_part_15_16_17, as.Date(dent_part_15_16_17[,1], format = "%d/%m/%Y") > as.Date("31/12/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_17 <- rbind(dataset_grades_glob_17,(subset(dent_non_part_15_16_17, as.Date(dent_non_part_15_16_17[,1], format = "%d/%m/%Y") > as.Date("31/12/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_17 <- rbind(dataset_grades_glob_17,(subset(dab_15_16_17, as.Date(dab_15_16_17[,1], format = "%d/%m/%Y") > as.Date("31/12/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_17 <- rbind(dataset_grades_glob_17,(subset(auto_presto_15_16_17, as.Date(auto_presto_15_16_17[,1], format = "%d/%m/%Y") > as.Date("31/12/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_17 <- rbind(dataset_grades_glob_17,(subset(auto_tma_bdg_16_17, as.Date(auto_tma_bdg_16_17[,1], format = "%d/%m/%Y") > as.Date("31/12/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_17 <- rbind(dataset_grades_glob_17,(subset(auto_class_tma_16_17, as.Date(auto_class_tma_16_17[,1], format = "%d/%m/%Y") > as.Date("31/12/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_17 <- rbind(dataset_grades_glob_17,(subset(auto_class_15_16_17, as.Date(auto_class_15_16_17[,1], format = "%d/%m/%Y") > as.Date("31/12/2016", format = "%d/%m/%Y"), select = Q1)))
dataset_grades_glob_17 <- rbind(dataset_grades_glob_17,(subset(auto_bdg_15_16_17, as.Date(auto_bdg_15_16_17[,1], format = "%d/%m/%Y") > as.Date("31/12/2016", format = "%d/%m/%Y"), select = Q1)))

mean(as.numeric(dataset_grades_glob_17$Q1))
