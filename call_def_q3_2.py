# -*- coding: utf-8 -*-
from def_vlQ3KDTreeAlist_2 import vl_ckdtree_Alist_q3_2
import numpy as np
import scipy.spatial as spatial
import csv
import pandas as pd

hfile = ".\hotels-ver2.txt"
#rfile = ".\\restaurants-ver2.txt"
rfile = ".\uniform78981.csv"
radRange = np.arange(1.1, 1.5, 0.5)
resRange = np.arange(1, 78981, 1000)    # CAUTION: RANGE MUST START AT 2!
hotRange = np.arange(23002, 25462, 500)    # CAUTION: RANGE MUST START AT 3!
#res: 78981 hot:25462


# import coordinates from files to kdtreeσ
resFile = csv.reader(open(rfile, 'rb'), delimiter="|")
resCoords = []
for row in resFile:
    resCoords.append((float(row[3]),float(row[4])))

hotFile = csv.reader(open(hfile, 'rb'), delimiter="|")
hotCoords = []
for row in hotFile:
    hotCoords.append((float(row[4]),float(row[5])))

f=[]
g=[]
for radius in radRange:
    for mhotels in hotRange[1::]:
        hotTree = spatial.cKDTree(hotCoords[:mhotels])
        resTree = spatial.cKDTree(resCoords)
        f = vl_ckdtree_Alist_q3_2(radius, hotTree, resTree, hotCoords)
        h = [radius,mhotels,f[0], f[1][0], f[1][1], f[2]]
        #h = [radius,krest,mhotels,f[0],f[1],f[2][0][0],f[2][0][1],f[2][1],f[2][2],f[2][3]]
        #print(h)
        g.append(h)
df_hotel_couples = pd.DataFrame(g)
df_hotel_couples = df_hotel_couples.rename(index=str, columns={0: "Radius", 1:"mHotels", 2: "Time", 3:"Hotel Pair", 4:"Max Score", 5: "avScore"})
df_hotel_couples.to_csv('q3_df_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res.csv')

