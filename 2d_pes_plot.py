import os
import numpy as np

PES_file = ('Cl-CH3-OH_PES_rscan.txt')
PES = np.genfromtxt(fname=PES_file, dtype='unicode')
headers = PES[0]
data = PES[1:]
data = data.astype(float)

clc = data[:,0]
co = data[:,1]
energy = data[:,2]

import matplotlib.pyplot as plt
from matplotlib import cm
# plot
fig, ax = plt.subplots()

ax.scatter(clc, co, c=energy, vmin=min(energy), vmax=max(0))

plt.show()
