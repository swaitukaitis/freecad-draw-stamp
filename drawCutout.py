import numpy as np
import matplotlib.pyplot as plt
import os
import pickle as p

datafile = '/Users/swaitukaitis/work/stampFolding/tempData.py'
[D, g, l ] = p.load( open( datafile, 'rb' ) )

fig = plt.figure(figsize = [5,5], frameon = False )
ax = fig.add_axes([0,0,1,1], aspect = 'equal')

ax.plot(np.linspace(-2.5, 2.5, 100), np.linspace(-1, 1, 100), 'r')

plt.show(fig)
