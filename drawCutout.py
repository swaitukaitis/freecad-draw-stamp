import numpy as np
import matplotlib.pyplot as plt
import os
import pickle as p

#load the temporary data file saved by the freeCAD code stamp.py
#datafile = '/Users/swaitukaitis/work/stampFolding/tempData.py'
#[D, g, l ] = p.load( open( datafile, 'rb' ) )
D = 50.0 / 25.4
boltD = 3 / 25.4

#set up the figure
fig = plt.figure(figsize = [D*1.01,D*1.01], frameon = False )
ax = fig.add_axes([0,0,1,1], aspect = 'equal')
ax.set_xlim(-D/2.*1.01, D/2.*1.01)
ax.set_ylim(-D/2.*1.01, D/2.*1.01)
plt.axis('off')

#draw the cutout boundary
edgeCircle=plt.Circle((0,0),D/2.,facecolor='None', edgecolor = 'r', linewidth = 0.25)
fig.gca().add_artist(edgeCircle)

#draw the bolt holes
boltCircle1 = plt.Circle((-D/4.,0), boltD/2., facecolor='None', edgecolor = 'r', linewidth = 0.25)
boltCircle2 = plt.Circle((D/4.,0), boltD/2., facecolor='None', edgecolor = 'r', linewidth = 0.25)
fig.gca().add_artist(boltCircle1)
fig.gca().add_artist(boltCircle2)

#save the figure as a pdf (so it can be read by the laser cutter)
plt.savefig('testFig.pdf', facecolor = 'None', edgecolor = 'None', pad_inches=0)
plt.show(fig)
