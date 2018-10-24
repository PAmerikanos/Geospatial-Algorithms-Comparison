# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:16:15 2018

@author: user
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from textwrap import wrap

######################################################        QUESTION 1      ###############################################################################


######################################################       EXPERIMENT 1     #####################################################################


#import regular data for varius radius
q1_df_hotel_1_25462_100_1rad = pd.read_csv(".\q1_df_hotel_1_25462_100_1rad.csv", sep=",", delimiter=None, header=0)
q1_df_hotel_1_25462_100_5rad = pd.read_csv(".\q1_df_hotel_1_25462_100_5rad.csv", sep=",", delimiter=None, header=0)
q1_df_hotel_1_25462_100_10rad = pd.read_csv(".\q1_df_hotel_1_25462_100_10rad.csv", sep=",", delimiter=None, header=0)
q1_df_hotel_1_25462_100_25rad = pd.read_csv(".\q1_df_hotel_1_25462_100_25rad.csv", sep=",", delimiter=None, header=0)
q1_df_hotel_1_25462_100_50rad = pd.read_csv(".\q1_df_hotel_1_25462_100_50rad.csv", sep=",", delimiter=None, header=0)
q1_df_hotel_1_25462_100_75rad = pd.read_csv(".\q1_df_hotel_1_25462_100_75rad.csv", sep=",", delimiter=None, header=0)


#import uniform data for varius radius
q1_df_uniform_78981_hotel_1_25462_100_1rad = pd.read_csv(".\q1_df_uniform_78981_hotel_1_25462_100_1rad.csv", sep=",", delimiter=None, header=0)
q1_df_uniform_78981_hotel_1_25462_100_5rad = pd.read_csv(".\q1_df_uniform_78981_hotel_1_25462_100_5rad.csv", sep=",", delimiter=None, header=0)
q1_df_uniform_78981_hotel_1_25462_100_10rad = pd.read_csv(".\q1_df_uniform_78981_hotel_1_25462_100_10rad.csv", sep=",", delimiter=None, header=0)
q1_df_uniform_78981_hotel_1_25462_100_25rad = pd.read_csv(".\q1_df_uniform_78981_hotel_1_25462_100_25rad.csv", sep=",", delimiter=None, header=0)
q1_df_uniform_78981_hotel_1_25462_100_50rad = pd.read_csv(".\q1_df_uniform_78981_hotel_1_25462_100_50rad.csv", sep=",", delimiter=None, header=0)
q1_df_uniform_78981_hotel_1_25462_100_75rad = pd.read_csv(".\q1_df_uniform_78981_hotel_1_25462_100_75rad.csv", sep=",", delimiter=None, header=0)


#function to plot Time vs Hotel range
def plot_time_vs_hotel_range(df_fromcsv):
    df_fromcsv = df_fromcsv.drop(["Unnamed: 0"], axis=1)
    df_fromcsv['Overall_Time'] = df_fromcsv['Time'].cumsum(axis = 0)
    df_fromcsv['mHotels'] = pd.Series(np.arange(1, 25462, 100), index=df_fromcsv.index)
    #df_fromcsv['CumSum_Time'].plot()
    #df_fromcsv.plot(y='Overall_Time', x='mHotels')
    #df_fromcsv.plot(y='Score', x='mHotels')
    return (df_fromcsv)

#plt.pyplot.scatter(pd.Series(np.arange(1, 25462, 100)),q1_df_hotel_1_25462_100_1rad['Score'])

q1_rad1 = plot_time_vs_hotel_range(q1_df_hotel_1_25462_100_1rad)
q1_rad5 = plot_time_vs_hotel_range(q1_df_hotel_1_25462_100_5rad)
q1_rad10 = plot_time_vs_hotel_range(q1_df_hotel_1_25462_100_10rad)
q1_rad25 = plot_time_vs_hotel_range(q1_df_hotel_1_25462_100_25rad)
q1_rad50 = plot_time_vs_hotel_range(q1_df_hotel_1_25462_100_50rad)
q1_rad75 = plot_time_vs_hotel_range(q1_df_hotel_1_25462_100_75rad)

q1_over_time_hot1 = {'rad1': q1_rad1['Overall_Time'], 'rad5': q1_rad5['Overall_Time'],'rad10': q1_rad10['Overall_Time'], 'rad25': q1_rad25['Overall_Time'],'rad50': q1_rad50['Overall_Time'], 'rad75': q1_rad75['Overall_Time']}
q1_over_time_hot1 = pd.DataFrame(data = q1_over_time_hot1)
q1_over_time_hot1['mHotels'] = pd.Series(np.arange(1, 25462, 100), index=q1_over_time_hot1.index)
q1_over_time_hot1.plot(x='mHotels')
plt.title("\n".join(wrap("CumSum Time of Calculations VS Hotel Number for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("CumSum Time (sec)")
#plt.legend(loc='best')
plt.savefig('Q1_CumSum Time of Calculations VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.show()


q1_t_hot1 = {'rad1': q1_rad1['Time'], 'rad5': q1_rad5['Time'],'rad10': q1_rad10['Time'], 'rad25': q1_rad25['Time'],'rad50': q1_rad50['Time'], 'rad75': q1_rad75['Time']}
q1_t_hot1 = pd.DataFrame(data = q1_t_hot1)
q1_t_hot1['mHotels'] = pd.Series(np.arange(1, 25462, 100), index=q1_t_hot1.index)
q1_t_hot1.plot(x='mHotels')
plt.title("\n".join(wrap("Time for each Calculation VS Hotel Number for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Time for each Calculation (sec)")
#plt.legend(loc='best')plt.savefig('CumSum Time of Calculations VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.savefig('Q1_Time for each Calculation VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.show()


q1_s_hot1 = {'rad1': q1_rad1['Score'], 'rad5': q1_rad5['Score'],'rad10': q1_rad10['Score'], 'rad25': q1_rad25['Score'],'rad50': q1_rad50['Score'], 'rad75': q1_rad75['Score']}
q1_s_hot1 = pd.DataFrame(data = q1_s_hot1)
q1_s_hot1['mHotels'] = pd.Series(np.arange(1, 25462, 100), index=q1_s_hot1.index)
q1_s_hot1.plot(x='mHotels')
plt.title("\n".join(wrap("Score VS Number of Hotels for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Score")
#plt.legend(loc='best')
plt.savefig('Q1_Score VS Number of Hotels for Varying Radius.png', format='png', dpi=1000)
plt.show()


q1_rad1_unif = plot_time_vs_hotel_range(q1_df_uniform_78981_hotel_1_25462_100_1rad)
q1_rad5_unif = plot_time_vs_hotel_range(q1_df_uniform_78981_hotel_1_25462_100_5rad)
q1_rad10_unif = plot_time_vs_hotel_range(q1_df_uniform_78981_hotel_1_25462_100_10rad)
q1_rad25_unif = plot_time_vs_hotel_range(q1_df_uniform_78981_hotel_1_25462_100_25rad)
q1_rad50_unif = plot_time_vs_hotel_range(q1_df_uniform_78981_hotel_1_25462_100_50rad)
q1_rad75_unif = plot_time_vs_hotel_range(q1_df_uniform_78981_hotel_1_25462_100_75rad)

q1_over_time_t_hot_unif = {'rad1': q1_rad1_unif['Overall_Time'], 'rad5': q1_rad5_unif['Overall_Time'],'rad10': q1_rad10_unif['Overall_Time'], 'rad25': q1_rad25_unif['Overall_Time'],'rad50': q1_rad50_unif['Overall_Time'], 'rad75': q1_rad75_unif['Overall_Time']}
q1_over_time_t_hot_unif = pd.DataFrame(data = q1_over_time_t_hot_unif)
q1_over_time_t_hot_unif['mHotels'] = pd.Series(np.arange(1, 25462, 100), index=q1_over_time_t_hot_unif.index)
q1_over_time_t_hot_unif.plot(x='mHotels')
plt.title("\n".join(wrap("CumSum Time of Calculations VS m Hotel Number for Varying Radius (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("CumSum Time (sec)")
#plt.legend(loc='best')
plt.savefig('Q1_CumSum Time of Calculations VS m Hotel Number for Varying Radius (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()

q1_t_hot_unif = {'rad1': q1_rad1_unif['Time'], 'rad5': q1_rad5_unif['Time'],'rad10': q1_rad10_unif['Time'], 'rad25': q1_rad25_unif['Time'],'rad50': q1_rad50_unif['Time'], 'rad75': q1_rad75_unif['Time']}
q1_t_hot_unif = pd.DataFrame(data = q1_t_hot_unif)
q1_t_hot_unif['mHotels'] = pd.Series(np.arange(1, 25462, 100), index=q1_t_hot_unif.index)
q1_t_hot_unif.plot(x='mHotels')
plt.title("\n".join(wrap("Time for each Calculation VS Hotel Number for Varying Radius (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Time for each Calculation (sec)")
#plt.legend(loc='best')
plt.savefig('Q1_Time for each Calculation VS Hotel Number for Varying Radius (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()

q1_s_hot_unif = {'rad1': q1_rad1_unif['Score'], 'rad5': q1_rad5_unif['Score'],'rad10': q1_rad10_unif['Score'], 'rad25': q1_rad25_unif['Score'],'rad50': q1_rad50_unif['Score'], 'rad75': q1_rad75_unif['Score']}
q1_s_hot_unif = pd.DataFrame(data = q1_s_hot_unif)
q1_s_hot_unif['mHotels'] = pd.Series(np.arange(1, 25462, 100), index=q1_s_hot_unif.index)
q1_s_hot_unif.plot(x='mHotels')
plt.title("\n".join(wrap("Score VS Number of Hotels for Varying Radius (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Score")
#plt.legend(loc='best')
plt.savefig('Q1_Score VS Number of Hotels for Varying Radius (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()

######################################################       EXPERIMENT 2     #####################################################################


#import regular data for varius hotels
q1_df_radius_1_75_2_10hot = pd.read_csv(".\q1_df_radius_1_75_2_10hot.csv", sep=",", delimiter=None, header=0)
q1_df_radius_1_75_2_100hot = pd.read_csv(".\q1_df_radius_1_75_2_100hot.csv", sep=",", delimiter=None, header=0)
q1_df_radius_1_75_2_1000hot = pd.read_csv(".\q1_df_radius_1_75_2_1000hot.csv", sep=",", delimiter=None, header=0)
q1_df_radius_1_75_2_5000hot = pd.read_csv(".\q1_df_radius_1_75_2_5000hot.csv", sep=",", delimiter=None, header=0)
q1_df_radius_1_75_2_10000hot = pd.read_csv(".\q1_df_radius_1_75_2_10000hot.csv", sep=",", delimiter=None, header=0)
q1_df_radius_1_75_2_15000hot = pd.read_csv(".\q1_df_radius_1_75_2_15000hot.csv", sep=",", delimiter=None, header=0)
q1_df_radius_1_75_2_20000hot = pd.read_csv(".\q1_df_radius_1_75_2_20000hot.csv", sep=",", delimiter=None, header=0)
q1_df_radius_1_75_2_25462hot = pd.read_csv(".\q1_df_radius_1_75_2_25462hot.csv", sep=",", delimiter=None, header=0)

#import uniform data for varius radius
q1_df_uniform_78981_radius_1_75_2_10hot = pd.read_csv(".\q1_df_uniform_78981_radius_1_75_2_10hot.csv", sep=",", delimiter=None, header=0)
q1_df_uniform_78981_radius_1_75_2_100hot = pd.read_csv(".\q1_df_uniform_78981_radius_1_75_2_100hot.csv", sep=",", delimiter=None, header=0)
q1_df_uniform_78981_radius_1_75_2_1000hot = pd.read_csv(".\q1_df_uniform_78981_radius_1_75_2_1000hot.csv", sep=",", delimiter=None, header=0)
q1_df_uniform_78981_radius_1_75_2_5000hot = pd.read_csv(".\q1_df_uniform_78981_radius_1_75_2_5000hot.csv", sep=",", delimiter=None, header=0)
q1_df_uniform_78981_radius_1_75_2_10000hot = pd.read_csv(".\q1_df_uniform_78981_radius_1_75_2_10000hot.csv", sep=",", delimiter=None, header=0)
q1_df_uniform_78981_radius_1_75_2_15000hot = pd.read_csv(".\q1_df_uniform_78981_radius_1_75_2_15000hot.csv", sep=",", delimiter=None, header=0)
q1_df_uniform_78981_radius_1_75_2_20000hot = pd.read_csv(".\q1_df_uniform_78981_radius_1_75_2_20000hot.csv", sep=",", delimiter=None, header=0)
q1_df_uniform_78981_radius_1_75_2_25462hot = pd.read_csv(".\q1_df_uniform_78981_radius_1_75_2_25462hot.csv", sep=",", delimiter=None, header=0)

q1_df_radius_1_75_2_1000hot == q1_df_radius_1_75_2_20000hot

#function to plot Time vs Restaurant range
def plot_time_vs_rad_range(df_fromcsv):
    df_fromcsv = df_fromcsv.drop(["Unnamed: 0"], axis=1)
    df_fromcsv['Overall_Time'] = df_fromcsv['Time'].cumsum(axis = 0)
    df_fromcsv['Radius'] = pd.Series(np.arange(1.0, 75.0, 2), index=df_fromcsv.index)
    #df_fromcsv['CumSum_Time'].plot()
    #df_fromcsv.plot(y='Overall_Time', x='Radius')
    #df_fromcsv.plot(y='Score', x='Radius')
    return (df_fromcsv)



q1_hot10 = plot_time_vs_rad_range(q1_df_radius_1_75_2_10hot)
q1_hot100 = plot_time_vs_rad_range(q1_df_radius_1_75_2_100hot)
q1_hot1000 = plot_time_vs_rad_range(q1_df_radius_1_75_2_1000hot)
q1_hot5000 = plot_time_vs_rad_range(q1_df_radius_1_75_2_5000hot)
q1_hot10000 = plot_time_vs_rad_range(q1_df_radius_1_75_2_10000hot)
q1_hot15000 = plot_time_vs_rad_range(q1_df_radius_1_75_2_15000hot)
q1_hot20000 = plot_time_vs_rad_range(q1_df_radius_1_75_2_20000hot)
q1_hot25462 = plot_time_vs_rad_range(q1_df_radius_1_75_2_25462hot)


q1_over_time_t_hot2 = {'hot10': q1_hot10['Overall_Time'], 'hot100': q1_hot100['Overall_Time'],'hot1000': q1_hot1000['Overall_Time'], 'hot5000': q1_hot5000['Overall_Time'],'hot10000': q1_hot10000['Overall_Time'],'hot15000': q1_hot15000['Overall_Time'], 'hot20000': q1_hot20000['Overall_Time'], 'hot25462': q1_hot25462['Overall_Time']}
q1_over_time_t_hot2 = pd.DataFrame(data = q1_over_time_t_hot2)
q1_over_time_t_hot2['Radius'] = pd.Series(np.arange(1.0, 75.0, 2), index=q1_over_time_t_hot2.index)
q1_over_time_t_hot2.plot(x='Radius')
plt.title("\n".join(wrap("CumSum Time of Calculations VS Radius for Varying Hotels", 60)))
plt.xlabel("Radius")
plt.ylabel("CumSum Time (sec)")
#plt.legend(loc='best')
plt.savefig('Q1_CumSum Time of Calculations VS Radius for Varying Hotels.png', format='png', dpi=1000)
plt.show()


q1_t_hot2 = {'hot10': q1_hot10['Time'], 'hot100': q1_hot100['Time'],'hot1000': q1_hot1000['Time'], 'hot5000': q1_hot5000['Time'], 'hot10000': q1_hot10000['Time'],'hot15000': q1_hot15000['Time'], 'hot20000': q1_hot20000['Time'], 'hot25462': q1_hot25462['Time']}
q1_t_hot2 = pd.DataFrame(data = q1_t_hot2)
q1_t_hot2['Radius'] = pd.Series(np.arange(1.0, 75.0, 2), index=q1_t_hot2.index)
q1_t_hot2.plot(x='Radius')
plt.title("\n".join(wrap("Time for each Calculation VS Radius for Varying Hotels", 60)))
plt.xlabel("Radius")
plt.ylabel("Time for each Calculation (sec)")
#plt.legend(loc='best')
plt.savefig('Q1_Time for each Calculation VS Radius for Varying Hotels.png', format='png', dpi=1000)
plt.show()

q1_s_hot2 = {'hot10': q1_hot10['Score'], 'hot100': q1_hot100['Score'],'hot1000': q1_hot1000['Score'], 'hot5000': q1_hot5000['Score'], 'hot10000': q1_hot10000['Score'],'hot15000': q1_hot15000['Score'], 'hot20000': q1_hot20000['Score'], 'hot25462': q1_hot25462['Score']}
q1_s_hot2 = pd.DataFrame(data = q1_s_hot2)
q1_s_hot2['Radius'] = pd.Series(np.arange(1.0, 75.0, 2), index=q1_s_hot2.index)
q1_s_hot2.plot(x='Radius')
plt.title("\n".join(wrap("Score VS Radius for Varying Hotels", 60)))
plt.xlabel("Radius")
plt.ylabel("Score")
#plt.legend(loc='best')
plt.savefig('Q1_Score VS Radius for Varying Hotels.png', format='png', dpi=1000)
plt.show()

q1_hot10_unif = plot_time_vs_rad_range(q1_df_uniform_78981_radius_1_75_2_10hot)
q1_hot100_unif = plot_time_vs_rad_range(q1_df_uniform_78981_radius_1_75_2_100hot)
q1_hot1000_unif = plot_time_vs_rad_range(q1_df_uniform_78981_radius_1_75_2_1000hot)
q1_hot5000_unif = plot_time_vs_rad_range(q1_df_uniform_78981_radius_1_75_2_5000hot)
q1_hot10000_unif = plot_time_vs_rad_range(q1_df_uniform_78981_radius_1_75_2_10000hot)
q1_hot15000_unif = plot_time_vs_rad_range(q1_df_uniform_78981_radius_1_75_2_15000hot)
q1_hot20000_unif = plot_time_vs_rad_range(q1_df_uniform_78981_radius_1_75_2_20000hot)
q1_hot25462_unif = plot_time_vs_rad_range(q1_df_uniform_78981_radius_1_75_2_25462hot)


t_hot2_unif = {'hot10': q1_hot10_unif['Overall_Time'], 'hot100': q1_hot100_unif['Overall_Time'],'hot1000': q1_hot1000_unif['Overall_Time'], 'hot5000': q1_hot5000_unif['Overall_Time'], 'hot10000': q1_hot10000_unif['Overall_Time'],'hot15000': q1_hot15000_unif['Overall_Time'], 'hot20000': q1_hot20000_unif['Overall_Time'], 'hot25462': q1_hot25462_unif['Overall_Time']}
t_hot2_unif = pd.DataFrame(data = t_hot2_unif)
t_hot2_unif['Radius'] = pd.Series(np.arange(1.0, 75.0, 2), index=t_hot2_unif.index)
t_hot2_unif.plot(x='Radius')
plt.title("\n".join(wrap("CumSum Time of Calculations VS Radius for Varying Hotels (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Radius")
plt.ylabel("CumSum Time (sec)")
#plt.legend(loc='best')
plt.savefig('Q1_CumSum Time of Calculations VS Radius for Varying Hotels (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()


q1_t_hot2_unif = {'hot10': q1_hot10_unif['Time'], 'hot100': q1_hot100_unif['Time'],'hot1000': q1_hot1000_unif['Time'], 'hot5000': q1_hot5000_unif['Time'], 'hot10000': q1_hot10000_unif['Time'],'hot15000': q1_hot15000_unif['Time'], 'hot20000': q1_hot20000_unif['Time'], 'hot25462': q1_hot25462_unif['Time']}
q1_t_hot2_unif = pd.DataFrame(data = q1_t_hot2_unif)
q1_t_hot2_unif['Radius'] = pd.Series(np.arange(1.0, 75.0, 2), index=q1_t_hot2_unif.index)
q1_t_hot2_unif.plot(x='Radius')
plt.title("\n".join(wrap("Time for each Calculation VS Radius for Varying Hotels (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Radius")
plt.ylabel("Time for each Calculation (sec)")
#plt.legend(loc='best')
plt.savefig('Q1_Time for each Calculation VS Radius for Varying Hotels (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()


q1_s_hot2_unif = {'hot10': q1_hot10_unif['Score'], 'hot100': q1_hot100_unif['Score'],'hot1000': q1_hot1000_unif['Score'], 'hot5000': q1_hot5000_unif['Score'], 'hot10000': q1_hot10000_unif['Score'],'hot15000': q1_hot15000_unif['Score'], 'hot20000': q1_hot20000_unif['Score'], 'hot25462': q1_hot25462_unif['Score']}
q1_s_hot2_unif = pd.DataFrame(data = q1_s_hot2_unif)
q1_s_hot2_unif['Radius'] = pd.Series(np.arange(1.0, 75.0, 2), index=q1_s_hot2_unif.index)
q1_s_hot2_unif.plot(x='Radius')
plt.title("\n".join(wrap("Score VS Radius for Varying Hotels (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Radius")
plt.ylabel("Score")
#plt.legend(loc='best')
plt.savefig('Q1_Score VS Radius for Varying Hotels (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()

######################################################        QUESTION 2      ###############################################################################


######################################################       EXPERIMENT 1     #####################################################################

#import regular data for varius number of restaurants
q2_df_hotel_1_25462_100_50res = pd.read_csv(".\q2_df_hotel_1_25462_100_50res.csv", sep=",", delimiter=None, header=0)
q2_df_hotel_1_25462_100_100res = pd.read_csv(".\q2_df_hotel_1_25462_100_100res.csv", sep=",", delimiter=None, header=0)
q2_df_hotel_1_25462_100_1000res = pd.read_csv(".\q2_df_hotel_1_25462_100_1000res.csv", sep=",", delimiter=None, header=0)
q2_df_hotel_1_25462_100_10000res = pd.read_csv(".\q2_df_hotel_1_25462_100_10000res.csv", sep=",", delimiter=None, header=0)
q2_df_hotel_1_25462_100_40000res = pd.read_csv(".\q2_df_hotel_1_25462_100_40000res.csv", sep=",", delimiter=None, header=0)
q2_df_hotel_1_25462_100_78981res = pd.read_csv(".\q2_df_hotel_1_25462_100_78981res.csv", sep=",", delimiter=None, header=0)


#import uniform data for varius number of restaurants
q2_df_uniform_78981_hotel_1_25462_100_50res = pd.read_csv(".\q2_df_uniform_78981_hotel_1_25462_100_50res.csv", sep=",", delimiter=None, header=0)
q2_df_uniform_78981_hotel_1_25462_100_100res = pd.read_csv(".\q2_df_uniform_78981_hotel_1_25462_100_100res.csv", sep=",", delimiter=None, header=0)
q2_df_uniform_78981_hotel_1_25462_100_1000res = pd.read_csv(".\q2_df_uniform_78981_hotel_1_25462_100_1000res.csv", sep=",", delimiter=None, header=0)
q2_df_uniform_78981_hotel_1_25462_100_10000res = pd.read_csv(".\q2_df_uniform_78981_hotel_1_25462_100_10000res.csv", sep=",", delimiter=None, header=0)
q2_df_uniform_78981_hotel_1_25462_100_40000res = pd.read_csv(".\q2_df_uniform_78981_hotel_1_25462_100_40000res.csv", sep=",", delimiter=None, header=0)



q2_res50 = plot_time_vs_hotel_range(q2_df_hotel_1_25462_100_50res)
q2_res100 = plot_time_vs_hotel_range(q2_df_hotel_1_25462_100_100res)
q2_res1000 = plot_time_vs_hotel_range(q2_df_hotel_1_25462_100_1000res)
q2_res10000 = plot_time_vs_hotel_range(q2_df_hotel_1_25462_100_10000res)
q2_res40000 = plot_time_vs_hotel_range(q2_df_hotel_1_25462_100_40000res)
q2_res78981 = plot_time_vs_hotel_range(q2_df_hotel_1_25462_100_78981res)

#Overall Time vs mHotels
q2_over_time_res2 = {'res50': q2_res50['Overall_Time'], 'res100': q2_res100['Overall_Time'],'res1000': q2_res1000['Overall_Time'], 'res10000': q2_res10000['Overall_Time'],'res40000': q2_res40000['Overall_Time'],'res78981': q2_res78981['Overall_Time']}
q2_over_time_res2 = pd.DataFrame(data = q2_over_time_res2)
q2_over_time_res2['mHotels'] = pd.Series(np.arange(1.0, 25462, 100), index=q2_over_time_res2.index)
q2_over_time_res2.plot(x='mHotels')
plt.title("\n".join(wrap("CumSum Time of Calculations VS Hotel Number for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("CumSum Time (sec)")
#plt.legend(loc='best')
plt.savefig('Q2_CumSum Time of Calculations VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.show()

# Time per mHotel number vs mHotels
q2_t_res2 = {'res50': q2_res50['Time'], 'res100': q2_res100['Time'],'res1000': q2_res1000['Time'], 'res10000': q2_res10000['Time'],'res40000': q2_res40000['Time'],'res78981': q2_res78981['Time']}
q2_t_res2 = pd.DataFrame(data = q2_t_res2)
q2_t_res2['mHotels'] = pd.Series(np.arange(1.0, 25462, 100), index=q2_t_res2.index)
q2_t_res2.plot(x='mHotels')
plt.title("\n".join(wrap("Time for each Calculation VS Hotel Number for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Time for each Calculation (sec)")
#plt.legend(loc='best')plt.savefig('CumSum Time of Calculations VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.savefig('Q2_Time for each Calculation VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.show()


#Average Score vs mHotels
q2_s_hot2 = {'res50': q2_res50['Score'], 'res100': q2_res100['Score'],'res1000': q2_res1000['Score'],'res10000': q2_res10000['Score'], 'res40000': q2_res40000['Score'], 'res78981': q2_res78981['Score']}
q2_s_hot2 = pd.DataFrame(data = q2_s_hot2)
q2_s_hot2['mHotels'] = pd.Series(np.arange(1.0, 25462, 100), index=q2_s_hot2.index)
q2_s_hot2.plot(x='mHotels')
plt.title("\n".join(wrap("Score VS Number of Hotels for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Score")
#plt.legend(loc='best')
plt.savefig('Q2_Score VS Number of Hotels for Varying Radius.png', format='png', dpi=1000)
plt.show()


q2_res50_unif = plot_time_vs_hotel_range(q2_df_uniform_78981_hotel_1_25462_100_50res)
q2_res100_unif = plot_time_vs_hotel_range(q2_df_uniform_78981_hotel_1_25462_100_100res)
q2_res1000_unif = plot_time_vs_hotel_range(q2_df_uniform_78981_hotel_1_25462_100_1000res)
q2_res10000_unif = plot_time_vs_hotel_range(q2_df_uniform_78981_hotel_1_25462_100_10000res)
q2_res40000_unif = plot_time_vs_hotel_range(q2_df_uniform_78981_hotel_1_25462_100_40000res)


#Overall Time vs mHotels
q2_over_time_res2_unif = {'res50': q2_res50_unif['Overall_Time'], 'res100': q2_res100_unif['Overall_Time'],'res1000': q2_res1000_unif['Overall_Time'], 'res10000': q2_res10000_unif['Overall_Time'],'res40000': q2_res40000_unif['Overall_Time']} # 'hot20000': q2_hot20000['Overall_Time'], 'hot25462': q2_hot25462['Overall_Time']}
q2_over_time_res2_unif = pd.DataFrame(data = q2_over_time_res2_unif)
q2_over_time_res2_unif['mHotels'] = pd.Series(np.arange(1.0, 25462, 100), index=q2_over_time_res2_unif.index)
q2_over_time_res2_unif.plot(x='mHotels')
plt.title("\n".join(wrap("CumSum Time of Calculations VS m Hotel Number for Varying Radius (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("CumSum Time (sec)")
#plt.legend(loc='best')
plt.savefig('Q2_CumSum Time of Calculations VS m Hotel Number for Varying Radius (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()

# Time per mHotel number vs mHotels
q2_t_res2_unif = {'res50': q2_res50_unif['Time'], 'res100': q2_res100_unif['Time'],'res1000': q2_res1000_unif['Time'], 'res10000': q2_res10000_unif['Time'],'res40000': q2_res40000_unif['Time']} # 'hot20000': q2_hot20000['Overall_Time'], 'hot25462': q2_hot25462['Overall_Time']}
q2_t_res2_unif = pd.DataFrame(data = q2_t_res2_unif)
q2_t_res2_unif['mHotels'] = pd.Series(np.arange(1.0, 25462, 100), index=q2_t_res2_unif.index)
q2_t_res2_unif.plot(x='mHotels')
plt.title("\n".join(wrap("Time for each Calculation VS Hotel Number for Varying Radius (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Time for each Calculation (sec)")
#plt.legend(loc='best')
plt.savefig('Q2_Time for each Calculation VS Hotel Number for Varying Radius (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()

#Average Score vs mHotels
q2_s_hot2_unif = {'res50': q2_res50_unif['Score'], 'res100': q2_res100_unif['Score'],'res1000': q2_res1000_unif['Score'], 'res10000': q2_res10000_unif['Score'],'res40000': q2_res40000_unif['Score']} # 'hot20000': q2_hot20000['Overall_Time'], 'hot25462': q2_hot25462['Overall_Time']}
q2_s_hot2_unif = pd.DataFrame(data = q2_s_hot2_unif)
q2_s_hot2_unif['mHotels'] = pd.Series(np.arange(1.0, 25462, 100), index=q2_s_hot2_unif.index)
q2_s_hot2_unif.plot(x='mHotels')
plt.title("\n".join(wrap("Score VS Number of Hotels for Varying Radius (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Score")
#plt.legend(loc='best')
plt.savefig('Q2_Score VS Number of Hotels for Varying Radius (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()

######################################################       EXPERIMENT 2     #####################################################################

#import data for varius number of hotels
q2_df_restaurants_2_78981_500_10hot = pd.read_csv(".\q2_df_restaurants_2_78981_500_10hot.csv", sep=",", delimiter=None, header=0)
q2_df_restaurants_2_78981_500_100hot = pd.read_csv(".\q2_df_restaurants_2_78981_500_100hot.csv", sep=",", delimiter=None, header=0)
q2_df_restaurants_2_78981_500_1000hot = pd.read_csv(".\q2_df_restaurants_2_78981_500_1000hot.csv", sep=",", delimiter=None, header=0)
q2_df_restaurants_2_78981_500_5000hot = pd.read_csv(".\q2_df_restaurants_2_78981_500_5000hot.csv", sep=",", delimiter=None, header=0)
q2_df_restaurants_2_78981_500_10000hot = pd.read_csv(".\q2_df_restaurants_2_78981_500_10000hot.csv", sep=",", delimiter=None, header=0)
q2_df_restaurants_2_78981_500_15000hot = pd.read_csv(".\q2_df_restaurants_2_78981_500_15000hot.csv", sep=",", delimiter=None, header=0)
q2_df_restaurants_2_78981_500_20000hot = pd.read_csv(".\q2_df_restaurants_2_78981_500_20000hot.csv", sep=",", delimiter=None, header=0)
q2_df_restaurants_2_78981_500_25462hot = pd.read_csv(".\q2_df_restaurants_2_78981_500_25462hot.csv", sep=",", delimiter=None, header=0)

#import data for varius number of hotels for uniform restaurants
q2_df_uniform_78981_restaurants_2_78981_500_10hot = pd.read_csv(".\q2_df_uniform_78981_restaurants_2_78981_500_10hot.csv", sep=",", delimiter=None, header=0)
q2_df_uniform_78981_restaurants_2_78981_500_100hot = pd.read_csv(".\q2_df_uniform_78981_restaurants_2_78981_500_100hot.csv", sep=",", delimiter=None, header=0)
q2_df_uniform_78981_restaurants_2_78981_500_1000hot = pd.read_csv(".\q2_df_uniform_78981_restaurants_2_78981_500_1000hot.csv", sep=",", delimiter=None, header=0)
q2_df_uniform_78981_restaurants_2_78981_500_5000hot = pd.read_csv(".\q2_df_uniform_78981_restaurants_2_78981_500_5000hot.csv", sep=",", delimiter=None, header=0)
q2_df_uniform_78981_restaurants_2_78981_500_10000hot = pd.read_csv(".\q2_df_uniform_78981_restaurants_2_78981_500_10000hot.csv", sep=",", delimiter=None, header=0)
q2_df_uniform_78981_restaurants_2_78981_500_15000hot = pd.read_csv(".\q2_df_uniform_78981_restaurants_2_78981_500_15000hot.csv", sep=",", delimiter=None, header=0)
q2_df_uniform_78981_restaurants_2_78981_500_20000hot = pd.read_csv(".\q2_df_uniform_78981_restaurants_2_78981_500_20000hot.csv", sep=",", delimiter=None, header=0)
q2_df_uniform_78981_restaurants_2_78981_500_25462hot = pd.read_csv(".\q2_df_uniform_78981_restaurants_2_78981_500_25462hot.csv", sep=",", delimiter=None, header=0)

def plot_time_vs_rest_range(df_fromcsv):
    df_fromcsv = df_fromcsv.drop(["Unnamed: 0"], axis=1)
    df_fromcsv['Overall_Time'] = df_fromcsv['Time'].cumsum(axis = 0)
    df_fromcsv['Restaurants'] = pd.Series(np.arange(2.0, 78981, 500), index=df_fromcsv.index)
    #df_fromcsv['CumSum_Time'].plot()
    #df_fromcsv.plot(y='Overall_Time', x='Radius')
    return (df_fromcsv)


q2_hot10 = plot_time_vs_rest_range(q2_df_restaurants_2_78981_500_10hot)
q2_hot100 = plot_time_vs_rest_range(q2_df_restaurants_2_78981_500_100hot)
q2_hot1000 = plot_time_vs_rest_range(q2_df_restaurants_2_78981_500_1000hot)
q2_hot5000 = plot_time_vs_rest_range(q2_df_restaurants_2_78981_500_5000hot)
q2_hot10000 = plot_time_vs_rest_range(q2_df_restaurants_2_78981_500_10000hot)
q2_hot15000 = plot_time_vs_rest_range(q2_df_restaurants_2_78981_500_15000hot)
q2_hot20000 = plot_time_vs_rest_range(q2_df_restaurants_2_78981_500_20000hot)
q2_hot25462 = plot_time_vs_rest_range(q2_df_restaurants_2_78981_500_25462hot)


#Overall Time vs mHotels
q2_over_time_hot2 = {'hot10': q2_hot10['Overall_Time'], 'hot100': q2_hot100['Overall_Time'],'hot1000': q2_hot1000['Overall_Time'],'hot5000': q2_hot5000['Overall_Time'], 'hot10000': q2_hot10000['Overall_Time'],'hot15000': q2_hot15000['Overall_Time'], 'hot20000': q2_hot20000['Overall_Time'], 'hot25462': q2_hot25462['Overall_Time']}
q2_over_time_hot2 = pd.DataFrame(data = q2_over_time_hot2)
q2_over_time_hot2['Restaurants'] = pd.Series(np.arange(2.0, 78981, 500), index=q2_over_time_hot2.index)
q2_over_time_hot2.plot(x='Restaurants')
plt.title("\n".join(wrap("CumSum Time of Calculations VS Restaurants Number for Varying Hotels", 60)))
plt.xlabel("Number of k Restaurants")
plt.ylabel("CumSum Time (sec)")
#plt.legend(loc='best')
plt.savefig('Q2_CumSum Time of Calculations VS Restaurants Number for Varying Hotels.png', format='png', dpi=1000)
plt.show()

# Time per mHotel number vs mHotels
q2_t_hot2 = {'hot10': q2_hot10['Time'], 'hot100': q2_hot100['Time'],'hot1000': q2_hot1000['Time'], 'hot5000': q2_hot5000['Time'], 'hot10000': q2_hot10000['Time'],'hot15000': q2_hot15000['Time'], 'hot20000': q2_hot20000['Time'], 'hot25462': q2_hot25462['Time']}
q2_t_hot2 = pd.DataFrame(data = q2_t_hot2)
q2_t_hot2['Restaurants'] = pd.Series(np.arange(2.0, 78981, 500), index=q2_t_hot2.index)
q2_t_hot2.plot(x='Restaurants')
plt.title("\n".join(wrap("Time for each Calculation VS Restaurants Number for Varying Hotels", 60)))
plt.xlabel("Number of k Restaurants")
plt.ylabel("Time for each Calculation (sec)")
#plt.legend(loc='best')
plt.savefig('Q2_Time for each Calculation VS Restaurants Number for Varying Hotels.png', format='png', dpi=1000)
plt.show()


#Average Score vs mHotels
q2_s_hot2 = {'hot10': q2_hot10['Score'], 'hot100': q2_hot100['Score'],'hot1000': q2_hot1000['Score'], 'hot5000': q2_hot5000['Score'], 'hot10000': q2_hot10000['Score'],'hot15000': q2_hot15000['Score'], 'hot20000': q2_hot20000['Score'], 'hot25462': q2_hot25462['Score']}
q2_s_hot2 = pd.DataFrame(data = q2_s_hot2)
q2_s_hot2['Restaurants'] = pd.Series(np.arange(2.0, 78981, 500), index=q2_s_hot2.index)
q2_s_hot2.plot(x='Restaurants')
plt.title("\n".join(wrap("Score VS Restaurants Number for Varying Hotels", 60)))
plt.xlabel("Number of k Restaurants")
plt.ylabel("Score")
#plt.legend(loc='best')
plt.savefig('Q2_Score VS Restaurants Number for Varying Hotels.png', format='png', dpi=1000)
plt.show()

q2_hot10_unif = plot_time_vs_rest_range(q2_df_uniform_78981_restaurants_2_78981_500_10hot)
q2_hot100_unif = plot_time_vs_rest_range(q2_df_uniform_78981_restaurants_2_78981_500_100hot)
q2_hot1000_unif = plot_time_vs_rest_range(q2_df_uniform_78981_restaurants_2_78981_500_1000hot)
q2_hot5000_unif = plot_time_vs_rest_range(q2_df_uniform_78981_restaurants_2_78981_500_5000hot)
q2_hot10000_unif = plot_time_vs_rest_range(q2_df_uniform_78981_restaurants_2_78981_500_10000hot)
q2_hot15000_unif = plot_time_vs_rest_range(q2_df_uniform_78981_restaurants_2_78981_500_15000hot)
q2_hot20000_unif = plot_time_vs_rest_range(q2_df_uniform_78981_restaurants_2_78981_500_20000hot)
q2_hot25462_unif = plot_time_vs_rest_range(q2_df_uniform_78981_restaurants_2_78981_500_25462hot)


q2_over_hot2_unif = {'hot10': q2_hot10_unif['Overall_Time'], 'hot100': q2_hot100_unif['Overall_Time'],'hot1000': q2_hot1000_unif['Overall_Time'], 'hot5000': q2_hot5000_unif['Overall_Time'], 'hot10000': q2_hot10000_unif['Overall_Time'],'hot15000': q2_hot15000_unif['Overall_Time'], 'hot20000': q2_hot20000_unif['Overall_Time'], 'hot25462': q2_hot25462_unif['Overall_Time']}
q2_over_hot2_unif = pd.DataFrame(data = q2_over_hot2_unif)
q2_over_hot2_unif['Restaurants'] = pd.Series(np.arange(2.0, 78981, 500), index=q2_over_hot2_unif.index)
q2_over_hot2_unif.plot(x='Restaurants')
plt.title("\n".join(wrap("CumSum Time of Calculations VS Restaurants Number for Varying Hotels (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Number of k Restaurants")
plt.ylabel("CumSum Time (sec)")
#plt.legend(loc='best')
plt.savefig('Q2_CumSum Time of Calculations VS Restaurants Number for Varying Hotels (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()

q2_t_hot2_unif = {'hot10': q2_hot10_unif['Time'], 'hot100': q2_hot100_unif['Time'],'hot1000': q2_hot1000_unif['Time'], 'hot5000': q2_hot5000_unif['Time'], 'hot10000': q2_hot10000_unif['Time'],'hot15000': q2_hot15000_unif['Time'], 'hot20000': q2_hot20000_unif['Time'], 'hot25462': q2_hot25462_unif['Time']}
q2_t_hot2_unif = pd.DataFrame(data = q2_t_hot2_unif)
q2_t_hot2_unif['Restaurants'] = pd.Series(np.arange(2.0, 78981, 500), index=q2_t_hot2_unif.index)
q2_t_hot2_unif.plot(x='Restaurants')
plt.title("\n".join(wrap("Time for each Calculation VS Restaurants Number for Varying Hotels (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Number of k Restaurants")
plt.ylabel("Time for each Calculation (sec)")
#plt.legend(loc='best')
plt.savefig('Q2_Time for each Calculation VS Restaurants Number for Varying Hotels (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()

q2_s_hot2_unif = {'hot10': q2_hot10_unif['Score'], 'hot100': q2_hot100_unif['Score'],'hot1000': q2_hot1000_unif['Score'], 'hot5000': q2_hot5000_unif['Score'], 'hot10000': q2_hot10000_unif['Score'],'hot15000': q2_hot15000_unif['Score'], 'hot20000': q2_hot20000_unif['Score'], 'hot25462': q2_hot25462_unif['Score']}
q2_s_hot2_unif = pd.DataFrame(data = q2_s_hot2_unif)
q2_s_hot2_unif['Restaurants'] = pd.Series(np.arange(2.0, 78981, 500), index=q2_s_hot2_unif.index)
q2_s_hot2_unif.plot(x='Restaurants')
plt.title("\n".join(wrap("Score VS Restaurants Number for Varying Hotels (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Number of k Restaurants")
plt.ylabel("Score")
#plt.legend(loc='best')
plt.savefig('Q2_Score VS Restaurants Number for Varying Hotels (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()


######################################################        QUESTION 3      ###############################################################################


######################################################       EXPERIMENT 1     #####################################################################

def make_df_cumsum(df_fromcsv):
    df_fromcsv = df_fromcsv.drop(["Unnamed: 0"], axis=1)
    df_fromcsv['Overall_Time'] = df_fromcsv['Time'].cumsum(axis = 0)
    return (df_fromcsv)

#import data for varius radius and number of hotels for all restaurants
#q3_df_hotel_couples_rad_001_006_001_hot_2_1000_100_78981res = pd.read_csv(".\q3_df_hotel_couples_rad_001_006_001_hot_2_1000_100_78981res.csv", sep=",", delimiter=None, header=0)
#q3_df_hotel_couples_rad_001_006_001_hot_2_5000_100_78981res = pd.read_csv(".\q3_df_hotel_couples_rad_001_006_001_hot_2_5000_100_78981res.csv", sep=",", delimiter=None, header=0)
#q3_df_hotel_couples_rad_001_006_001_hot_2_10000_100_78981res = pd.read_csv(".\q3_df_hotel_couples_rad_001_006_001_hot_2_10000_100_78981res.csv", sep=",", delimiter=None, header=0)
#q3_df_hotel_couples_rad_001_006_001_hot_2_15000_100_78981res = pd.read_csv(".\q3_df_hotel_couples_rad_001_006_001_hot_2_15000_100_78981res.csv", sep=",", delimiter=None, header=0)
#q3_df_hotel_couples_rad_001_006_001_hot_2_20000_100_78981res = pd.read_csv(".\q3_df_hotel_couples_rad_001_006_001_hot_2_20000_100_78981res.csv", sep=",", delimiter=None, header=0)
q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res = pd.read_csv(".\q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.csv", sep=",", delimiter=None, header=0)
#q3_df_hotel_couples_rad_001_006_001_hot_2_25462_500_78981res = pd.read_csv(".\q3_df_hotel_couples_rad_001_006_001_hot_2_25462_500_78981res.csv", sep=",", delimiter=None, header=0)
q3_df_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res = pd.read_csv(".\q3_df_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res.csv", sep=",", delimiter=None, header=0)

q3_df_hotel_couples_rad_001_25462hot_78981res = q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res[(q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.Radius == 0.01)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]
q3_df_hotel_couples_rad_002_25462hot_78981res = q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res[(q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.Radius == 0.02)]
q3_df_hotel_couples_rad_003_25462hot_78981res = q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res[(q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.Radius == 0.03)]
q3_df_hotel_couples_rad_004_25462hot_78981res = q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res[(q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.Radius == 0.04)]
q3_df_hotel_couples_rad_005_25462hot_78981res = q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res[(q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.Radius == 0.05)]

q3_df_hotel_couples_rad_01_hot_2_25462_500_78981res = q3_df_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res[(q3_df_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res.Radius == 0.1)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]
q3_df_hotel_couples_rad_06_hot_2_25462_500_78981res = q3_df_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res[(q3_df_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res.Radius == 0.6)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]
#q3_df_hotel_couples_rad_1_1_hot_2_25462_500_78981res = q3_df_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res[(q3_df_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res.Radius == 1.1)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]
#q3_df_hotel_couples_rad_1_6_hot_2_25462_500_78981res = q3_df_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res[(q3_df_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res.Radius == 1.6)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]


#q3_df_hotel_couples_rad_001_hot_2_1000_100_78981res = q3_df_hotel_couples_rad_001_006_001_hot_2_1000_100_78981res[(q3_df_hotel_couples_rad_001_006_001_hot_2_1000_100_78981res.Radius == 0.01)]
#q3_df_hotel_couples_rad_002_hot_2_5000_100_78981res = q3_df_hotel_couples_rad_001_006_001_hot_2_5000_100_78981res[(q3_df_hotel_couples_rad_001_006_001_hot_2_5000_100_78981res.Radius == 0.02)]
#q3_df_hotel_couples_rad_003_hot_2_10000_100_78981res = q3_df_hotel_couples_rad_001_006_001_hot_2_10000_100_78981res[(q3_df_hotel_couples_rad_001_006_001_hot_2_10000_100_78981res.Radius == 0.03)]
#q3_df_hotel_couples_rad_004_hot_2_15000_100_78981res = q3_df_hotel_couples_rad_001_006_001_hot_2_15000_100_78981res[(q3_df_hotel_couples_rad_001_006_001_hot_2_15000_100_78981res.Radius == 0.04)]
#q3_df_hotel_couples_rad_005_hot_2_20000_100_78981res = q3_df_hotel_couples_rad_001_006_001_hot_2_20000_100_78981res[(q3_df_hotel_couples_rad_001_006_001_hot_2_20000_100_78981res.Radius == 0.05)]
#q3_df_hotel_couples_rad_005_hot_2_25462_100_78981res = q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res[(q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.Radius == 0.05)]

#q3_hot_2_1000_100_rad_001[(q3_hot_2_1000_100_rad_001.Radius == 0.01) & (q3_hot_2_1000_100_rad_001.mHotels <= 1000)]
#q3_df_hotel_couples_rad_001_25462hot_78981res[q3_df_hotel_couples_rad_001_25462hot_78981res.mHotels <= 1000]

q3_hot_2_25462_100_rad_001 = make_df_cumsum(q3_df_hotel_couples_rad_001_25462hot_78981res)
q3_hot_2_25462_100_rad_002 = make_df_cumsum(q3_df_hotel_couples_rad_002_25462hot_78981res)
q3_hot_2_25462_100_rad_003 = make_df_cumsum(q3_df_hotel_couples_rad_003_25462hot_78981res)
q3_hot_2_25462_100_rad_004 = make_df_cumsum(q3_df_hotel_couples_rad_004_25462hot_78981res)
q3_hot_2_25462_100_rad_005 = make_df_cumsum(q3_df_hotel_couples_rad_005_25462hot_78981res)


q3_over_time_rad0 = {'rad_0.01': q3_hot_2_25462_100_rad_001['Overall_Time'].values, 'rad_0.02': q3_hot_2_25462_100_rad_002['Overall_Time'].values,'rad_0.03': q3_hot_2_25462_100_rad_003['Overall_Time'].values, 'rad_0.04': q3_hot_2_25462_100_rad_004['Overall_Time'].values,'rad_0.05': q3_hot_2_25462_100_rad_005['Overall_Time'].values}
q3_over_time_rad0 = pd.DataFrame(data = q3_over_time_rad0)
q3_over_time_rad0['mHotels'] = pd.Series(np.arange(1, 25462, 100), index=q1_over_time_hot1.index)
q3_over_time_rad0.plot(x='mHotels')
plt.title("\n".join(wrap("CumSum Time of Calculations VS Hotel Number for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("CumSum Time (sec)")
#plt.legend(loc='best')
plt.savefig('Q3_CumSum Time of Calculations VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.show()


q3_t_rad0 = {'rad_0.01': q3_hot_2_25462_100_rad_001['Time'].values, 'rad_0.02': q3_hot_2_25462_100_rad_002['Time'].values,'rad_0.03': q3_hot_2_25462_100_rad_003['Time'].values, 'rad_0.04': q3_hot_2_25462_100_rad_004['Time'].values,'rad_0.05': q3_hot_2_25462_100_rad_005['Time'].values}
q3_t_rad0 = pd.DataFrame(data = q3_t_rad0)
q3_t_rad0['mHotels'] = pd.Series(np.arange(1, 25462, 100), index=q1_t_hot1.index)
q3_t_rad0.plot(x='mHotels')
plt.title("\n".join(wrap("Time for each Calculation VS Hotel Number for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Time for each Calculation (sec)")
#plt.legend(loc='best')plt.savefig('CumSum Time of Calculations VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.savefig('Q3_Time for each Calculation VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.show()


q3_s_rad0 = {'rad_0.01': q3_hot_2_25462_100_rad_001['avScore'].values, 'rad_0.02': q3_hot_2_25462_100_rad_002['avScore'].values,'rad_0.03': q3_hot_2_25462_100_rad_003['avScore'].values, 'rad_0.04': q3_hot_2_25462_100_rad_004['avScore'].values,'rad_0.05': q3_hot_2_25462_100_rad_005['avScore'].values}
q3_s_rad0 = pd.DataFrame(data = q3_s_rad0)
q3_s_rad0['mHotels'] = pd.Series(np.arange(1, 25462, 100), index=q1_s_hot1.index)
q3_s_rad0.plot(x='mHotels')
plt.title("\n".join(wrap("Score VS Number of Hotels for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Score")
#plt.legend(loc='best')
plt.savefig('Q3_Score VS Number of Hotels for Varying Radius.png', format='png', dpi=1000)
plt.show()


q3_hot_2_25462_100_rad_01 = make_df_cumsum(q3_df_hotel_couples_rad_01_hot_2_25462_500_78981res)
q3_hot_2_25462_100_rad_06= make_df_cumsum(q3_df_hotel_couples_rad_06_hot_2_25462_500_78981res)
#q3_hot_2_25462_100_rad_1_1 = make_df_cumsum(q3_df_hotel_couples_rad_1_1_hot_2_25462_500_78981res)
#q3_hot_2_25462_100_rad_1_6 = make_df_cumsum(q3_df_hotel_couples_rad_1_6_hot_2_25462_500_78981res)

q3_over_time_rad1 = {'rad_0.1': q3_hot_2_25462_100_rad_01['Overall_Time'][0:len(q3_hot_2_25462_100_rad_06)].values, 'rad_0.6': q3_hot_2_25462_100_rad_06['Overall_Time'].values}#,'rad_1_1': q3_hot_2_25462_100_rad_1_1['Overall_Time'].values, 'rad_1.6': q3_hot_2_25462_100_rad_1_6['Overall_Time'].values}#,'rad_0.05': q3_hot_2_25462_100_rad_005['Overall_Time'].values}
q3_over_time_rad1 = pd.DataFrame(data = q3_over_time_rad1)
q3_over_time_rad1['mHotels'] = pd.Series(np.arange(2, 15002, 500))
q3_over_time_rad1.plot(x='mHotels')
plt.title("\n".join(wrap("CumSum Time of Calculations VS Hotel Number for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("CumSum Time (sec)")
#plt.legend(loc='best')
plt.savefig('Q3_CumSum Time of Calculations VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.show()


q3_t_rad1 = {'rad_0.1': q3_hot_2_25462_100_rad_01['Time'][0:len(q3_hot_2_25462_100_rad_06)].values, 'rad_0.6': q3_hot_2_25462_100_rad_06['Time'].values}#,'rad_1_1': q3_hot_2_25462_100_rad_1_1['Time'].values, 'rad_1.6': q3_hot_2_25462_100_rad_1_6['Time'].values}#,'rad_0.05': q3_hot_2_25462_100_rad_005['Time'].values}
q3_t_rad1 = pd.DataFrame(data = q3_t_rad1)
q3_t_rad1['mHotels'] = pd.Series(np.arange(2, 15002, 500))
q3_t_rad1.plot(x='mHotels')
plt.title("\n".join(wrap("Time for each Calculation VS Hotel Number for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Time for each Calculation (sec)")
#plt.legend(loc='best')plt.savefig('CumSum Time of Calculations VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.savefig('Q3_Time for each Calculation VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.show()


q3_s_rad1 = {'rad_0.1': q3_hot_2_25462_100_rad_01['avScore'][0:len(q3_hot_2_25462_100_rad_06)].values, 'rad_0.6': q3_hot_2_25462_100_rad_06['avScore'].values}#,'rad_1_1': q3_hot_2_25462_100_rad_1_1['avScore'].values, 'rad_1.6': q3_hot_2_25462_100_rad_1_6['avScore'].values}#,'rad_0.05': q3_hot_2_25462_100_rad_005['avScore'].values}
q3_s_rad1 = pd.DataFrame(data = q3_s_rad1)
q3_s_rad1['mHotels'] = pd.Series(np.arange(2, 15002, 500))
q3_s_rad1.plot(x='mHotels')
plt.title("\n".join(wrap("Score VS Number of Hotels for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Score")
#plt.legend(loc='best')
plt.savefig('Q3_Score VS Number of Hotels for Varying Radius.png', format='png', dpi=1000)
plt.show()

#import data for varius radius and number of hotels for all uniform restaurants
#q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_1000_100_78981res = pd.read_csv(".\q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_1000_100_78981res.csv", sep=",", delimiter=None, header=0)
#q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_5000_100_78981res = pd.read_csv(".\q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_5000_100_78981res.csv", sep=",", delimiter=None, header=0)
#q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_10000_100_78981res = pd.read_csv(".\q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_10000_100_78981res.csv", sep=",", delimiter=None, header=0)
#q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_15000_100_78981res = pd.read_csv(".\q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_15000_100_78981res.csv", sep=",", delimiter=None, header=0)
#q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_20000_100_78981res = pd.read_csv(".\q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_20000_100_78981res.csv", sep=",", delimiter=None, header=0)
q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res = pd.read_csv(".\q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.csv", sep=",", delimiter=None, header=0)
q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res = pd.read_csv(".\q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res.csv", sep=",", delimiter=None, header=0)
q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res_rest_1_1 = pd.read_csv(".\q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res_rest_1_1.csv", sep=",", delimiter=None, header=0)
q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res = q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res.append(q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res_rest_1_1,ignore_index=True)

q3_df_hotel_couples_rad_001_25462hot_78981res_unif = q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res[(q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.Radius == 0.01)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]
q3_df_hotel_couples_rad_002_25462hot_78981res_unif = q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res[(q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.Radius == 0.02)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]
q3_df_hotel_couples_rad_003_25462hot_78981res_unif = q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res[(q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.Radius == 0.03)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]
q3_df_hotel_couples_rad_004_25462hot_78981res_unif = q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res[(q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.Radius == 0.04)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]
q3_df_hotel_couples_rad_005_25462hot_78981res_unif = q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res[(q3_df_uniform_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.Radius == 0.05)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]


q3_hot_2_25462_100_rad_001_unif = make_df_cumsum(q3_df_hotel_couples_rad_001_25462hot_78981res_unif)
q3_hot_2_25462_100_rad_002_unif = make_df_cumsum(q3_df_hotel_couples_rad_002_25462hot_78981res_unif)
q3_hot_2_25462_100_rad_003_unif = make_df_cumsum(q3_df_hotel_couples_rad_003_25462hot_78981res_unif)
q3_hot_2_25462_100_rad_004_unif = make_df_cumsum(q3_df_hotel_couples_rad_004_25462hot_78981res_unif)
q3_hot_2_25462_100_rad_005_unif = make_df_cumsum(q3_df_hotel_couples_rad_005_25462hot_78981res_unif)

q3_over_time_rad0_unif = {'rad_0.01': q3_hot_2_25462_100_rad_001_unif['Overall_Time'].values, 'rad_0.02': q3_hot_2_25462_100_rad_002_unif['Overall_Time'].values,'rad_0.03': q3_hot_2_25462_100_rad_003_unif['Overall_Time'].values, 'rad_0.04': q3_hot_2_25462_100_rad_004_unif['Overall_Time'].values,'rad_0.05': q3_hot_2_25462_100_rad_005_unif['Overall_Time'].values}
q3_over_time_rad0_unif = pd.DataFrame(data = q3_over_time_rad0_unif)
q3_over_time_rad0_unif['mHotels'] = pd.Series(np.arange(1, 25462, 500), index=q1_over_time_hot1.index)
q3_over_time_rad0_unif.plot(x='mHotels')
plt.title("\n".join(wrap("CumSum Time of Calculations VS Hotel Number for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("CumSum Time (sec)")
#plt.legend(loc='best')
plt.savefig('Q3_CumSum Time of Calculations VS Hotel Number for Varying Radius (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()


q3_t_rad0_unif = {'rad_0.01': q3_hot_2_25462_100_rad_001_unif['Time'].values, 'rad_0.02': q3_hot_2_25462_100_rad_002_unif['Time'].values,'rad_0.03': q3_hot_2_25462_100_rad_003_unif['Time'].values, 'rad_0.04': q3_hot_2_25462_100_rad_004_unif['Time'].values,'rad_0.05': q3_hot_2_25462_100_rad_005_unif['Time'].values}
q3_t_rad0_unif = pd.DataFrame(data = q3_t_rad0_unif)
q3_t_rad0_unif['mHotels'] = pd.Series(np.arange(1, 25462, 500), index=q1_t_hot1.index)
q3_t_rad0_unif.plot(x='mHotels')
plt.title("\n".join(wrap("Time for each Calculation VS Hotel Number for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Time for each Calculation (sec)")
#plt.legend(loc='best')plt.savefig('CumSum Time of Calculations VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.savefig('Q3_Time for each Calculation VS Hotel Number for Varying Radius (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()


q3_s_rad0_unif = {'rad_0.01': q3_hot_2_25462_100_rad_001_unif['avScore'].values, 'rad_0.02': q3_hot_2_25462_100_rad_002_unif['avScore'].values,'rad_0.03': q3_hot_2_25462_100_rad_003_unif['avScore'].values, 'rad_0.04': q3_hot_2_25462_100_rad_004_unif['avScore'].values,'rad_0.05': q3_hot_2_25462_100_rad_005_unif['avScore'].values}
q3_s_rad0_unif = pd.DataFrame(data = q3_s_rad0_unif)
q3_s_rad0_unif['mHotels'] = pd.Series(np.arange(1, 25462, 500), index=q1_s_hot1.index)
q3_s_rad0_unif.plot(x='mHotels')
plt.title("\n".join(wrap("Score VS Number of Hotels for Varying Radius", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Score")
#plt.legend(loc='best')
plt.savefig('Q3_Score VS Number of Hotels for Varying Radius (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()

q3_df_hotel_couples_rad_01_25462hot_78981res_unif = q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res[(q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res.Radius == 0.1)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]
q3_df_hotel_couples_rad_06_25462hot_78981res_unif = q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res[(q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res.Radius == 0.6)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]
q3_df_hotel_couples_rad_1_1_25462hot_78981res_unif = q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res[(q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res.Radius == 1.1)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]
q3_df_hotel_couples_rad_1_6_25462hot_78981res_unif = q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res[(q3_df_uniform_hotel_couples_rad_01_2_05_hot_2_25462_500_78981res.Radius == 1.6)]# & (q3_df_hotel_couples_rad_001_006_001_hot_2_25462_100_78981res.mHotels >= 102)]


q3_hot_2_25462_100_rad_01_unif = make_df_cumsum(q3_df_hotel_couples_rad_01_25462hot_78981res_unif)
q3_hot_2_25462_100_rad_06_unif = make_df_cumsum(q3_df_hotel_couples_rad_06_25462hot_78981res_unif)
q3_hot_2_25462_100_rad_1_1_unif = make_df_cumsum(q3_df_hotel_couples_rad_1_1_25462hot_78981res_unif)
q3_hot_2_25462_100_rad_1_6_unif = make_df_cumsum(q3_df_hotel_couples_rad_1_6_25462hot_78981res_unif)

q3_over_time_rad1_unif = {'rad_0.1': q3_hot_2_25462_100_rad_01_unif['Overall_Time'].values, 'rad_0.6': q3_hot_2_25462_100_rad_06_unif['Overall_Time'].values,'rad_1_1': q3_hot_2_25462_100_rad_1_1_unif['Overall_Time'].values}#, 'rad_1.6': q3_hot_2_25462_100_rad_1_6['Overall_Time'].values}#,'rad_0.05': q3_hot_2_25462_100_rad_005['Overall_Time'].values}
q3_over_time_rad1_unif = pd.DataFrame(data = q3_over_time_rad1_unif)
q3_over_time_rad1_unif['mHotels'] = pd.Series(np.arange(1, 25462, 500))
q3_over_time_rad1_unif.plot(x='mHotels')
plt.title("\n".join(wrap("CumSum Time of Calculations VS Hotel Number for Varying Radius (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("CumSum Time (sec)")
#plt.legend(loc='best')
plt.savefig('Q3_CumSum Time of Calculations VS Hotel Number for Varying Radius (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()


q3_t_rad1_unif = {'rad_0.1': q3_hot_2_25462_100_rad_01_unif['Time'].values, 'rad_0.6': q3_hot_2_25462_100_rad_06_unif['Time'].values,'rad_1_1': q3_hot_2_25462_100_rad_1_1_unif['Time'].values}#, 'rad_1.6': q3_hot_2_25462_100_rad_1_6['Time'].values}#,'rad_0.05': q3_hot_2_25462_100_rad_005['Time'].values}
q3_t_rad1_unif = pd.DataFrame(data = q3_t_rad1_unif)
q3_t_rad1_unif['mHotels'] = pd.Series(np.arange(1, 25462, 500))
q3_t_rad1_unif.plot(x='mHotels')
plt.title("\n".join(wrap("Time for each Calculation VS Hotel Number for Varying Radius (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Time for each Calculation (sec)")
#plt.legend(loc='best')plt.savefig('CumSum Time of Calculations VS Hotel Number for Varying Radius.png', format='png', dpi=1000)
plt.savefig('Q3_Time for each Calculation VS Hotel Number for Varying Radius (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()


q3_s_rad1_unif = {'rad_0.1': q3_hot_2_25462_100_rad_01_unif['avScore'].values, 'rad_0.6': q3_hot_2_25462_100_rad_06_unif['avScore'].values,'rad_1_1': q3_hot_2_25462_100_rad_1_1_unif['avScore'].values}#, 'rad_1.6': q3_hot_2_25462_100_rad_1_6['avScore'].values}#,'rad_0.05': q3_hot_2_25462_100_rad_005['avScore'].values}
q3_s_rad1_unif = pd.DataFrame(data = q3_s_rad1_unif)
q3_s_rad1_unif['mHotels'] = pd.Series(np.arange(1, 25462, 500))
q3_s_rad1_unif.plot(x='mHotels')
plt.title("\n".join(wrap("Score VS Number of Hotels for Varying Radius (Uniformly Distributed Restaurants)", 60)))
plt.xlabel("Number of m Hotels")
plt.ylabel("Score")
#plt.legend(loc='best')
plt.savefig('Q3_Score VS Number of Hotels for Varying Radius (Uniformly Distributed Restaurants).png', format='png', dpi=1000)
plt.show()