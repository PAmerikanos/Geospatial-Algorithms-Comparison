# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from numpy import genfromtxt
from scipy.interpolate import griddata
from mpl_toolkits.mplot3d import axes3d
import sys

que = input("Question #1-3:")
if que == 1:
    ylabel = 'R Radius'
elif que == 2:
    ylabel = 'K Restaurants'
elif que == 3:
    ylabel = 'Something'
else:
    print('Please insert Integer 1-3')


fig = plt.figure(figsize=(16.0, 9.0))
inFile = 'INOUT/outputFileQ' + str(que) + '.csv'
outFile = 'INOUT/HotelRestPlotQ' + str(que) + '.png'
my_data = genfromtxt(inFile, delimiter=',')
x = (my_data[:,0])
y = (my_data[:,1])
z = (my_data[:,2])
a = (my_data[:,3])
t = (my_data[:,4])


axS = fig.add_subplot(321, projection='3d')
axS.scatter(x,y,z, c=z, cmap=cm.coolwarm, marker='o')
axS.set_xlabel('M Hotels')
axS.set_ylabel(ylabel)
axS.set_zlabel('S Score')

axT = fig.add_subplot(222, projection='3d')
axT.scatter(x,y,t, c=t, cmap=cm.coolwarm, marker='o')
axT.set_xlabel('M Hotels')
axT.set_ylabel(ylabel)
axT.set_zlabel('T Time')



axSc = fig.add_subplot(323, projection='3d')
xi = np.linspace(x.min(), x.max(), 250)
yi = np.linspace(y.min(), y.max(), 15)
zi = griddata((x, y), z, (xi[None, :], yi[:, None]), method='nearest')    # create a uniform spaced grid
xig, yig = np.meshgrid(xi, yi)
surf = axSc.plot_surface(X=xig, Y=yig, Z=zi, cmap=cm.coolwarm, rstride=5, cstride=3, linewidth=0, antialiased=False)   # 3d plot
axSc.set_xlabel('M Hotels')
axSc.set_ylabel(ylabel)
axSc.set_zlabel('S Score')

axTc = fig.add_subplot(324, projection='3d')
xi = np.linspace(x.min(), x.max(), 250)
yi = np.linspace(y.min(), y.max(), 15)
ti = griddata((x, y), t, (xi[None, :], yi[:, None]), method='nearest')    # create a uniform spaced grid
xig, yig = np.meshgrid(xi, yi)
surf = axTc.plot_surface(X=xig, Y=yig, Z=ti, cmap=cm.coolwarm, rstride=5, cstride=3, linewidth=0, antialiased=False)   # 3d plot
axTc.set_xlabel('M Hotels')
axTc.set_ylabel(ylabel)
axTc.set_zlabel('T Time')


axAv = fig.add_subplot(325, projection='3d')
xi = np.linspace(x.min(), x.max(), 250)
yi = np.linspace(y.min(), y.max(), 15)
zi = griddata((x, y), a, (xi[None, :], yi[:, None]), method='nearest')    # create a uniform spaced grid
xig, yig = np.meshgrid(xi, yi)
surf = axAv.plot_surface(X=xig, Y=yig, Z=zi, cmap=cm.coolwarm, rstride=5, cstride=3, linewidth=0, antialiased=False)   # 3d plot
axAv.set_xlabel('M Hotels')
axAv.set_ylabel(ylabel)
axAv.set_zlabel('A AvgScore')



#plt.plot(y, a)
#plt.xlabel(ylabel)
#plt.ylabel('Average Score')
#plt.show()
#print()

plt.savefig(outFile)
plt.show()