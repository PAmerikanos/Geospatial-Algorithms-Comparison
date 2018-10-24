# -*- coding: utf-8 -*-

# import libraries and initialize variables
import numpy as np
import scipy.spatial.distance as dist
import csv
import time

radius = 1.0    #float(input('Enter R radius: '))
mHotels = 100   #int(input('Enter M hotels: '))
i = 0
score = 0
sumScore = 0
start_time = time.time()

# import coordinates from files to vectors
resFile = csv.reader(open('./INOUT/restaurants-ver1.txt', 'rb'), delimiter="|")
resCoords = []
for row in resFile:
    resCoords.append((float(row[3]),float(row[4])))

hotFile = csv.reader(open('./INOUT/hotels-ver1.txt', 'rb'), delimiter="|")
hotCoords = []
for row in hotFile:
    hotCoords.append((float(row[4]),float(row[5])))

# nested for-loop: calculate distance for all hotel-restaurant pairs
for hotel in hotCoords[:mHotels]:
    score = 0
    for restaurant in resCoords:
        if dist.chebyshev(np.asarray(hotel), np.asarray(restaurant)) <= radius:
            score += 1
    print("Hotel ID: " + str(i+1) +" | Matches: " + str(score))
    i += 1
    sumScore += score

avgScore = float(sumScore/i)

print("--- Simple HxR FINISHED ---")
print("Time: %s seconds | AvScore: %s" % ((time.time() - start_time),avgScore))