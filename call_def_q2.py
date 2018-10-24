# -*- coding: utf-8 -*-
from def_vlQ2KDTree import vl_kdtree_q2
#from def_vlQ2Simple import vl_simple_q2
#import matplotlib.pyplot as plt
#from matplotlib import cm
import numpy as np
#from scipy.interpolate import griddata
import pandas as pd
#from mpl_toolkits.mplot3d import Axes3D

hfile = ".\hotels-ver2.txt"
rfile = ".\\restaurants-ver2.txt"
#rfile = ".\uniform78981.csv"
resRange = range(2, 78981, 500)    # CAUTION: RANGE MUST START AT 2!
hotRange = np.arange(1, 25462, 100)

# 2D scatterplot Time vs mHotels
# Time: b[0] - AvgScore: b[1]
b=[]
for i in hotRange:
    c = vl_kdtree_q2(78981, i, hfile, rfile)
    b.append(c)    
df_hotel = pd.DataFrame(b)
df_hotel = df_hotel.rename(index=str, columns={0: "Time", 1: "Score"})
#df_hotel.to_csv('q2_df_hotel_1_25462_100_78981res.csv')
df_hotel.to_csv('q2_df_uniform_78981_hotel_1_25462_100_78981res.csv')

df_hotel[0].plot()
#plt.scatter(range(1,11), df_hotel[0])

# 2D scatterplot Time vs kRest
# Time: d[0] - AvgScore: d[1]
d=[]
for r in resRange:
    e = vl_kdtree_q2(r, 5000, hfile, rfile)
    d.append(e)
df_restaurants = pd.DataFrame(d)
df_restaurants = df_restaurants.rename(index=str, columns={0: "Time", 1: "Score"})
#df_restaurants.to_csv('q2_df_restaurants_2_78981_500_25462hot.csv')
df_restaurants.to_csv('q2_df_restaurants_2_78981_5000_25462hot.csv')

#df_radius[0].plot()
#plt.scatter(range(1,7), df_radius[0])

# 3D scatterplot Time vs kRest vs mHotels
# Time: f[0] - AvgScore: f[1]
#f=[]
#g=[]
#for krest in resRange:
#    for mhotels in hotRange:
#        f = vl_kdtree_q2(krest, mhotels, hfile, rfile)
#        g.append([krest,mhotels,f[0],f[1]])
#
#
#fig = plt.figure(figsize=(16,9))
#ax = fig.add_subplot(111, projection='3d')
#x = np.array(g).T[0]
#y = np.array(g).T[1]
#z = np.array(g).T[2]
##ax.scatter(x, y, z)
#ax.set_xlabel("Restaurants")
#ax.set_ylabel("Hotels")
#ax.set_zlabel("Time")
#xi = np.linspace(x.min(), x.max())
#yi = np.linspace(y.min(), y.max())
#zi = griddata((x, y), z, (xi[None, :], yi[:, None]), method='nearest')    # create a uniform spaced grid
#xig, yig = np.meshgrid(xi, yi)
#surf = ax.plot_surface(X=xig, Y=yig, Z=zi, cmap=cm.coolwarm, rstride=5, cstride=3, linewidth=0, antialiased=True)   # 3d plot
#plt.show()