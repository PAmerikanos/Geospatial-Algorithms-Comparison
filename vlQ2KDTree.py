# -*- coding: utf-8 -*-

# import libraries and initialize variables
import numpy as np
import scipy.spatial as spatial
import csv
import time

kRest = 100       #int(input('Enter K nearest restaurants: '))
mHotels = 10     #int(input('Enter M hotels: '))
i = 0
score = 0.0
sumScore = 0.0
start_time = time.time()

# import coordinates from files to kdtree and vector
resFile = csv.reader(open('./INOUT/restaurants-ver1.txt', 'rb'), delimiter="|")
resCoords = []
for row in resFile:
    resCoords.append((float(row[3]),float(row[4])))
resTree = spatial.cKDTree(resCoords)

hotFile = resFile = csv.reader(open('./INOUT/hotels-ver1.txt', 'rb'), delimiter="|")
hotCoords = []
for row in hotFile:
    hotCoords.append((float(row[4]),float(row[5])))

# query restaurant kdtree for each hotel
for hotel in hotCoords[:mHotels]:
    score = 0.0
    resHotList, resHotInd = resTree.query(hotel, k=kRest, p=np.inf)
    score = resHotList[kRest-1]
    print("Hotel ID: " + str(i+1) +" | Min Radius: " + str(score))
    i += 1
    sumScore += score

avgScore = float(sumScore/i)

print("--- cKDTree FINISHED ---")
print("Time: %s seconds | AvScore: %s" % ((time.time() - start_time),avgScore))