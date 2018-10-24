# -*- coding: utf-8 -*-
from def_vlQ3KDTreeAlist import vl_ckdtree_Alist_q3
from def_vlQ3KDTreeBlist import vl_ckdtree_Blist_q3
from def_vlQ3KDTreeAnparray import vl_ckdtree_Aarray_q3
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from scipy.interpolate import griddata
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

hfile = "C:\Users\user\Qsync\ergasies_2ou_ex\IV\Vlachou\code\hotels-ver2.txt"
rfile = "C:\\Users\\user\\Qsync\\ergasies_2ou_ex\\IV\\Vlachou\\code\\restaurants-ver2.txt"
radRange = np.linspace(0.01, 0.7, 5)
resRange = list(np.arange(0, 78981, 10000))    # CAUTION: RANGE MUST START AT 2!
hotRange = np.arange(0, 25462, 5000)    # CAUTION: RANGE MUST START AT 3!
#res: 78981 hot:25462

## 2D scatterplot Time vs mHotels
## Time: b[0] - AvgScore: b[1]
#b=[]
#for i in hotRange:
#    c = vl_ckdtree_Alist_q3(2.0, 10, i, hfile, rfile)
#    b.append(c)    
#df_hotel = pd.DataFrame(b)
#df_hotel[0].plot()
##plt.scatter(range(1,11), df_hotel[0])
#
## 2D scatterplot Time vs kRest
## Time: d[0] - AvgScore: d[1]
#d=[]
#for r in resRange:
#    e = vl_ckdtree_Alist_q3(2.0, r, 10, hfile, rfile)
#    d.append(e)
#df_radius = pd.DataFrame(d)
#df_radius[0].plot()
##plt.scatter(range(1,7), df_radius[0])

# 3D scatterplot Time vs kRest vs mHotels
# Time: f[0] - AvgScore: f[1]
f=[]
g=[]
for radius in radRange[0::]:
    for krest in resRange[1::]:
        for mhotels in hotRange[1::]:
            f = vl_ckdtree_Alist_q3(radius, krest, mhotels, hfile, rfile)
            g.append([radius,krest,mhotels,f[0],f[1],f[2][0][0],f[2][0][1],f[2][1]])
df_hotel_couples = pd.DataFrame(g)
df_hotel_couples = df_hotel_couples.rename(index=str, columns={0: "Radius", 1:"kRests", 2:"mHotels", 3: "Time", 4: "avScore", 5: "Hotel1", 6: "Hotel2", 7:"Hotel_Couple_Score"})
df_hotel_couples.to_csv('q3_df_hotel_couples_rad_001_0.7_5_res_0_78981_10000_hot_0_25462_5000.csv')

fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot(111, projection='3d')
x = np.array(g).T[1]
y = np.array(g).T[2]
z = np.array(g).T[3]
#ax.scatter(x, y, z)
ax.set_xlabel("Restaurants")
ax.set_ylabel("Hotels")
ax.set_zlabel("Time")
xi = np.linspace(x.min(), x.max())
yi = np.linspace(y.min(), y.max())
zi = griddata((x, y), z, (xi[None, :], yi[:, None]), method='nearest')    # create a uniform spaced grid
xig, yig = np.meshgrid(xi, yi)
surf = ax.plot_surface(X=xig, Y=yig, Z=zi, cmap=cm.coolwarm, rstride=5, cstride=3, linewidth=0, antialiased=True)   # 3d plot
plt.show()