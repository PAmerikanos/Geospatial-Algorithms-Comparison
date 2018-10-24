    # -*- coding: utf-8 -*-
    
def vl_ckdtree_Blist_q3(radius, krest, mhotels, hfile, rfile):
    # import libraries and initialize variables
    import numpy as np
    import scipy.spatial as spatial
    import csv
    import time
    from itertools import islice
    
    #radius = 1    #float(input('Enter R radius: '))
    #mHotels = 10     #int(input('Enter M hotels: '))
    #i = 0
    score = 0
    sumScore = 0
    start_time = time.time()
    
    # import coordinates from files to kdtreeσ
    resFile = csv.reader(open(rfile, 'rb'), delimiter="|")
    resCoords = []
    for row in islice(resFile,1,krest):
        resCoords.append((float(row[3]),float(row[4])))
    resTree = spatial.cKDTree(resCoords)
    
    hotFile = csv.reader(open(hfile, 'rb'), delimiter="|")
    hotCoords = []
    for row in islice(hotFile,1,mhotels):
        hotCoords.append((float(row[4]),float(row[5])))
    hotTree = spatial.cKDTree(hotCoords)
    
    # for hotel find rest+
    # put rest in array hotelXrest+
    # find (h1,h2) with dist(h1,h2)<2radius+
    # for (h1,h2) in list find restaurants:
    # put rest in list
    # remove duplicate rest
    # calculate score len(list)
    
    hotresList = []
    for hotel in hotCoords:
        hotres = list(resTree.query_ball_point(hotel, r=radius, p=np.inf))
        hotresList.append(hotres)
        print(hotresList)
    
    hotArray = list(hotTree.query_pairs(r=2*radius, p=np.inf))
    print("Hotel pairs:")
    print(hotArray)
    print("Count of hotel pairs: " + str(len(hotArray)))
    
    hotList = []
    for hotTuple in hotArray:
        hot1res = np.array(hotresList[hotTuple[0]])
        hot2res = np.array(hotresList[hotTuple[1]])
        resList = np.append(hot1res,hot2res)
        resUniqList = np.unique(resList)
        score = resUniqList.size
        hotList.append((hotTuple,score))
        sumScore += score
        print("Hotel pair score: " + str((hotTuple,score)))
    hotList.sort(key=lambda x: x[1], reverse=True)
    
    avgScore = float(sumScore/len(hotArray))
    
    print("--- cKDTree (B List) FINISHED ---")
    print("Time: %s seconds" % ((time.time() - start_time)))
    print("Final hotel pair score: " + str(hotList[0]))
    print("AvScore: %s" % (avgScore))
    return ((time.time() - start_time),avgScore,hotList[0])