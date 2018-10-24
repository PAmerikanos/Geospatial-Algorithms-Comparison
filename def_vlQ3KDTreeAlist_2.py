    # -*- coding: utf-8 -*-
    
def vl_ckdtree_Alist_q3_2(radius, hotTree, resTree, hotCoords):
    # import libraries and initialize variables
    import numpy as np
    import time
    score = 0
    sumScore = 0
    start_time = time.time()

    #print("--- STARTED ---")    
    
    hotArray = list(hotTree.query_pairs(r=2*radius, p=np.inf))
    
    hotList = []
    for hotTuple in hotArray:
        hot1res = np.array(resTree.query_ball_point(hotCoords[hotTuple[0]], r=radius, p=np.inf))
        hot2res = np.array(resTree.query_ball_point(hotCoords[hotTuple[1]], r=radius, p=np.inf))
        resList = np.append(hot1res,hot2res)
        resUniqList = np.unique(resList)
        score = resUniqList.size
        sumScore += score
        hotList.append((hotTuple,score))
        #hotList.append((hotTuple,score))
        #print("Hotel pair/score/time/avgScore: " + str((hotTuple,score,(time.time() - start_time),avgScore)))
    hotList.sort(key=lambda x: x[1], reverse=True)
    
    avgScore = float(sumScore/len(hotArray))
    
#    print("--- cKDTree (A List) FINISHED ---")
#    print("Time: %s seconds" % ((time.time() - start_time)))
#    print("Final hotel pair score: " + str(hotList[0]))
#    print("AvScore: %s" % (avgScore))
    return ((time.time() - start_time), hotList[0], avgScore)