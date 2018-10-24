# -*- coding: utf-8 -*-
from def_vlQ1cKDTree import vl_ckdtree_q1
import numpy as np
from scipy.interpolate import griddata
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm

hfile = ".\hotels-ver2.txt"
#rfile = ".\\restaurants-ver2.txt"
rfile = ".\uniform78981.csv"
radRange = np.arange(1.0, 75.0, 2)
hotRange = np.arange(1, 25462, 100)

# 2D scatterplot Time vs mHotels
# Time: b[0] - AvgScore: b[1]
b=[]
for i in hotRange:
    c = vl_ckdtree_q1(0.05, i, hfile, rfile)
    b.append(c)    
df_hotel_50rad = pd.DataFrame(b)
df_hotel_50rad = df_hotel_50rad.rename(index=str, columns={0: "Time", 1: "Score"})
df_hotel_50rad.to_csv('q1_df_uniform_78981_hotel_1_25462_100_005rad_new.csv')

df_hotel_50rad[0].plot()
#plt.scatter(range(1,11), df_hotel[0])
#
# 2D scatterplot Time vs Radius
# Time: d[0] - AvgScore: d[1]
d=[]
for i in radRange:
    e = vl_ckdtree_q1(i, 25462, hfile, rfile)
    d.append(e)
df_radius_25462hot = pd.DataFrame(d)
df_radius_25462hot = df_radius_25462hot.rename(index=str, columns={0: "Time", 1: "Score"})
df_radius_25462hot.to_csv('q1_df_uniform_78981_radius_1_75_2_25462hot_new.csv')



#plt.scatter(range(1,7), df_radius[0])
#
# 3D scatterplot Time vs Radius vs mHotels
# Time: f[0] - AvgScore: f[1]
f=[]
g=[]
for radius in radRange:
    for mhotels in hotRange:
        f = vl_ckdtree_q1(radius, mhotels, hfile, rfile)
        g.append([radius,mhotels,f[0],f[1]])
results = pd.DataFrame(g)
results = results.rename(index=str, columns={0: "Radius", 1: "Hotels", 2: "Time", 3: "Score"})
results.to_csv('df_all_results_.csv')


fig = plt.figure(figsize=(16,9))
ax = fig.add_subplot(111, projection='3d')
x = np.array(g).T[0]
y = np.array(g).T[1]
z = np.array(g).T[2]

#g_pan = pd.DataFrame({ 'Radius' : x,'Hotels' : y, 'Time' : z}, index=range(len(x)))
#ax.plot_trisurf(g_pan.Radius, g_pan.Hotels, g_pan.Time, cmap=cm.jet, linewidth=0.2)
#plt.show()

#ax.scatter(x, y, z)
ax.set_xlabel("Radius")
ax.set_ylabel("Hotels")
ax.set_zlabel("Time")
xi = np.linspace(x.min(), x.max())
yi = np.linspace(y.min(), y.max())
zi = griddata((x, y), z, (xi[None, :], yi[:, None]), method='nearest')    # create a uniform spaced grid
xig, yig = np.meshgrid(xi, yi)
surf = ax.plot_surface(X=xig, Y=yig, Z=zi, cmap=cm.coolwarm, rstride=5, cstride=3, linewidth=0, antialiased=True)   # 3d plot
plt.show()