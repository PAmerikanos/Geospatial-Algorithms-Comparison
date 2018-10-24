    # -*- coding: utf-8 -*-
    
def vl_ckdtree_Apandas_q3(radius, krest, mhotels, hfile, rfile):
    # import libraries and initialize variables
    import numpy as np
    import scipy.spatial as spatial
    import time
    import pandas as pd
    
    #radius = 0.001    #float(input('Enter R radius: '))
    #i = 0
    score = 0
    sumScore = 0
    start_time = time.time()
    
    # import coordinates from files to kdtreeσ
    hotels = pd.read_csv(hfile, sep='|', nrows=mhotels)
    hotels.set_index((hotels['ID']))
    rests = pd.read_csv(rfile, sep='|', nrows=krest)
    rests.set_index((rests['ID']))
    resCoords = rests.loc[:,['LAT','LON']]
    hotCoords = hotels.loc[:,['LAT','LON']]
    resTree = spatial.cKDTree(resCoords)
    hotTree = spatial.cKDTree(hotCoords)
    
    # find (h1,h2) with dist(h1,h2)<2radius
    hotArray = pd.DataFrame.from_records(list(hotTree.query_pairs(r=2*radius, p=np.inf)))
    # for (h1,h2) in list find restaurants
    hot1res = [resTree.query_ball_point(hotCoords.values[x], r=radius, p=np.inf) for x in hotArray.values[:,0]]
    hot2res = [resTree.query_ball_point(hotCoords.values[x], r=radius, p=np.inf) for x in hotArray.values[:,1]]
    # put rest in list
    resList = pd.DataFrame({ 'hot1res' : hot1res,'hot2res' : hot2res})
    # remove duplicate rest
    resUniqList = np.unique(resList)
    # calculate score len(list)
    score = resUniqList.size
    hotDf = pd.DataFrame({ 'hotTuple' : hot1res,'hot2res' : hot2res,'score' : score})
    sumScore = hotDf['score'].sum()
    hotDf.sort_values('score')
    avgScore = float(sumScore/len(hotArray))
    
    print("--- cKDTree (A List) FINISHED ---")
    print("Time: %s seconds" % ((time.time() - start_time)))
    print("Final hotel pair score: " + str(hotDf['score'].iloc[0]))
    print("AvScore: %s" % (avgScore))
    return ((time.time() - start_time),avgScore,hotDf['score'].iloc[0])