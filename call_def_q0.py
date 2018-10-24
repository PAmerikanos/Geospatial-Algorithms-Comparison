# -*- coding: utf-8 -*-
from def_vlQ1cKDTree import vl_ckdtree_q1
from def_vlQ1KDTree import vl_kdtree_q1
from def_vlQ1Grid import vl_grid_q1
from def_vlQ1Simple import vl_simple_q1
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


hfile = "C:\Users\user\Qsync\ergasies_2ou_ex\IV\Vlachou\code\hotels-ver2.txt"
rfile = "C:\\Users\\user\\Qsync\\ergasies_2ou_ex\\IV\\Vlachou\\code\\restaurants-ver2.txt"


c = vl_ckdtree_q1(2.0, 25462, hfile, rfile)  
d = vl_kdtree_q1(2.0, 25462, hfile, rfile)
e = vl_grid_q1(2.0, 25462, hfile, rfile)
f = vl_simple_q1(2.0, 25462, hfile, rfile) 

df_hotel_2rad = pd.DataFrame(c)
df_hotel_2rad = df_hotel_2rad.rename(index=str, columns={0: "Time", 1: "Score"})
#df_hotel_50rad.to_csv('q1_df_uniform_78981_hotel_1_25462_100_50rad.csv')



