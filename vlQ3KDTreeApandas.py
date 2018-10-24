# -*- coding: utf-8 -*-
#Point indices within R of [lat,lon].

import numpy as np
import scipy.spatial as spatial
import time
import pandas as pd


radius = 0.001    #float(input('Enter R radius: '))
i = 0
score = 0
sumScore = 0
start_time = time.time()

path_hotels = "./NewAlexaUpload/hotels-ver1.txt"
path_rest = "./NewAlexaUpload/restaurants-ver1.txt"
hotels = pd.read_csv(path_hotels, sep='|')
hotels.set_index((hotels['ID']))
rests = pd.read_csv(path_rest, sep='|')
rests.set_index((rests['ID']))
resCoords = rests.loc[:,['LAT','LON']]
hotCoords = hotels.loc[:,['LAT','LON']]

resTree = spatial.cKDTree(resCoords)
hotTree = spatial.cKDTree(hotCoords)






#hotArray = list(hotTree.query_pairs(r=2*radius, p=np.inf))

hotArray = pd.DataFrame.from_records(list(hotTree.query_pairs(r=2*radius, p=np.inf)))

#print("Hotel pairs:")
#print(hotArray)
#print("Count of hotel pairs: " + str(len(hotArray)))

hot1res = [resTree.query_ball_point(hotCoords.values[x], r=radius, p=np.inf) \
for x in hotArray.values[:,0]]
hot2res = [resTree.query_ball_point(hotCoords.values[x], r=radius, p=np.inf) \
for x in hotArray.values[:,1]]

resList = pd.DataFrame({ 'hot1res' : hot1res,'hot2res' : hot2res})

resUniqList = np.unique(resList)
score = resUniqList.size
hotDf = pd.DataFrame({ 'hotTuple' : hot1res,'hot2res' : hot2res,'score' : score})
#hotArray.add(other, axis='columns', level=None, fill_value=None)

sumScore = hotDf['score'].sum()
hotDf.sort_values('score')

avgScore = float(sumScore/len(hotArray))

print("--- cKDTree (A List) FINISHED ---")
print("Time: %s seconds" % ((time.time() - start_time)))
print("Final hotel pair score: " + str(hotDf['score'].iloc[0]))
print("AvScore: %s" % (avgScore))