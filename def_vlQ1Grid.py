    # -*- coding: utf-8 -*-
    
def vl_grid_q1(radius, mHotels, hfile, rfile):
    # import libraries and initialize variables
    import numpy as np
    import scipy.spatial.distance as dist
    import csv
    import time
    
    #radius = 1.0
    #mHotels = 1
    i = 1
    score = 0
    sumScore = 0
    grid = []
    latS = -43.0
    latN = 50.0
    lonW = -125.0
    lonE = 48.0
    div = 2     # div>=1 -> grid length 111km
    step = float(1.0/div)
    
    # Generate MBR - Grid Partitioning
    for lat in np.arange(latS, latN, step):
        for lon in np.arange(lonW, lonE, step):
            grid.append([lon, lat, lon + step, lat + step])
    
    # locate restaurants in MBR cell and check for neighbors
    def resLocate(item):
        slon = float(item[1])
        slat = float(item[0])
        srad = radius
        cellLocate = []
        for cell in grid:
            if  cell[0] <= slon and cell[1] <= slat and slon <= cell[2] and slat <= cell[3]:
                cellLocate.append(tuple(cell))
                if abs(slon-cell[0]) <= srad:
                        for adjCellW in grid:
                            if adjCellW[1] ==  cell[1] and adjCellW[2] == cell[0] and adjCellW[3] == cell[3]:
                                cellLocate.append(tuple(adjCellW))
                if abs(slat-cell[1]) <= srad:
                        for adjCellS in grid:
                            if adjCellS[0] ==  cell[0] and adjCellS[2] == cell[2] and adjCellS[3] == cell[1]:
                                cellLocate.append(tuple(adjCellS))
                if abs(slon-cell[2]) <= srad:
                        for adjCellE in grid:
                            if adjCellE[0] ==  cell[2] and adjCellE[1] == cell[1] and adjCellE[3] == cell[3]:
                                cellLocate.append(tuple(adjCellE))
                if abs(slat-cell[3]) <= srad:
                        for adjCellN in grid:
                            if adjCellN[0] ==  cell[0] and adjCellN[1] == cell[3] and adjCellN[2] == cell[2]:
                                cellLocate.append(tuple(adjCellN))
        return (cellLocate)
    
    # locate hotels in MBR cell
    def hotLocate(item):
        slon = float(item[1])
        slat = float(item[0])
        cellLocate = []
        for cell in grid:
            if  cell[0] <= slon and cell[1] <= slat and slon <= cell[2] and slat <= cell[3]:
                cellLocate.append(tuple(cell))
                break
        return (cellLocate)
    
    start_time = time.time()
    
    # import coordinates from files to vectors
    resFile = csv.reader(open(rfile, 'rb'), delimiter="|")
    resCoords = []
    for row in resFile:
        resCoords.append((float(row[3]),float(row[4])))
    
    hotFile = csv.reader(open(hfile, 'rb'), delimiter="|")
    hotCoords = []
    for row in hotFile:
        hotCoords.append((float(row[4]),float(row[5])))
    
    # nested for-loop: calculate distance for hotel-restaurant pairs located in same cells
    for hotel in hotCoords[:mHotels]:
        score = 0
        for restaurant in resCoords:
            if hotLocate(hotel) in resLocate(restaurant):
                if dist.chebyshev(np.asarray(hotel), np.asarray(restaurant)) <= radius:
                    score += 1
        #print("Hotel ID: " + str(i) +" | Matches: " + str(score))
        i += 1
        sumScore += score

    avgScore = float(sumScore/i)
    
    #print("--- Grid Partition FINISHED ---")
    #print("Time: %s seconds | AvScore: %s" % ((time.time() - start_time),avgScore))
    return ((time.time() - start_time),avgScore)