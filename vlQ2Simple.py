# -*- coding: utf-8 -*-

# import libraries and initialize variables
import numpy as np
import scipy.spatial.distance as dist
import csv
import time

kRest = 100       #int(input('Enter K nearest restaurants: '))
mHotels = 10    #int(input('Enter M hotels: '))
i = 0
score = 0.0
sumScore = 0.0
start_time = time.time()

# import coordinates from files to vectors
resFile = csv.reader(open('./INOUT/restaurants-ver1.txt', 'rb'), delimiter="|")
resCoords = []
for row in resFile:
    resCoords.append((float(row[3]),float(row[4])))

hotFile = resFile = csv.reader(open('./INOUT/hotels-ver1.txt', 'rb'), delimiter="|")
hotCoords = []
for row in hotFile:
    hotCoords.append((float(row[4]),float(row[5])))

# nested for-loop: calculate distance for all hotel-restaurant pairs
for hotel in hotCoords[:mHotels]:
    score = 0.0
    resHotList = []
    for restaurant in resCoords:
        resHotList.append(dist.chebyshev(np.asarray(hotel), np.asarray(restaurant)))
    resHotList.sort()
    score = resHotList[kRest-1]
    print("Hotel ID: " + str(i+1) +" | Min Radius: " + str(score))
    i += 1
    sumScore += score

avgScore = float(sumScore/i)

print("--- Simple HxR FINISHED ---")
print("Time: %s seconds | AvScore: %s" % ((time.time() - start_time),avgScore))