# -*- coding: utf-8 -*-
import random
import numpy

max = 78981

a = []
for i in range(0, max):
    a.append([i,i,i,random.uniform(24.0, 49.0),random.uniform(-125.0, -70.0)])
b = numpy.asarray(a)
numpy.savetxt("uniform" + str(max) + ".csv", b, delimiter="|")

