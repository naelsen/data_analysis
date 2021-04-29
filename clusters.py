import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import scipy.cluster.hierarchy as sch
import sklearn
from sklearn.cluster import AgglomerativeClustering



df = pd.read_csv (r'data/train.csv')

index = ["Genre", "Fidélité", "Age", "Type.du.vol", \
"Classe", "Distance", "Wifi", "Horaire.pratique", \
"Facilité.resevation", "Emplacement.porte", "Nourriture",\
 "Enregistrement.en.ligne", "Siege.confort", "Loisir", \
 "On.board.service", "Espace.jambe", "Gestion.bagage", \
 "Checkin.service", "Inflight.service", "Propreté", "Retard.depart", \
 "Retard.arrivé", "Satisfaction"]

s = pd.Series(df, index=index)

#with open("data/train.csv","r") as f:
#	tab = f.read()


#print(type(tab))
#Clusters = AgglomerativeClustering(linkage = 'ward')
#datas = CLusters.fit(self.data.tfidf_vectorizer.toarray())
