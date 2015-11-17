import FreeCAD as FC
import numpy as np
import Part as P
import time as t
import os
import pickle 

#Make FreeCAD vectors easier to work with
def V(x):
    return(FC.Vector(x[0], x[1], x[2]))
    
#Physics input parameters
n=-1
D = 20.0
theta = 80  
gap = 10.5

#Technical input parameters
lShaft = 35.0
dShaft = 12.0
lThread = 15.0
dThread = 16.0
dCrossbar = 6.0
hCrossbar = 8.0
dBoltHole = 2.4
lBoltHole = 10.0
dBoltHead = 5.5
hBoltHead = 3.0
sheathWidth = 4.0

#Derived input parameters
height = gap*np.tan(theta*(np.pi/180))

#Setting up the export file
outFolder=u"P:\\Work\\stampFolding\\"+t.strftime('%Y%m%d')+'_'+str(n)+'_'+str(D)+'_'+str(theta)+'_'+str(gap)+'\\'

if not os.path.exists(outFolder):
    os.makedirs(outFolder)

#outFolder = "Users\\waitukaitus\\Desktop\\"+t.strftime('%Y%m%d')+'_'+str(n)+'_'+str(D)+'_'+str(theta)+'_'+str(gap)+'\\'

FC.newDocument()

#Now create the parts
#First the base (for both stump and sheath)
shaft = P.makeCylinder(dShaft/2., lShaft, V([0,0,0]), V([0,0,1]) )
thread = P.makeCylinder(dThread/2., lThread, V([0,0,lShaft-lThread]), V([0,0,1]) )
crossbar = P.makeCylinder(dCrossbar/2., 2*dShaft, V([0,-dShaft,hCrossbar]), V([0,1,0]))
baseAdapter = shaft.fuse(thread)
baseAdapter = baseAdapter.cut(crossbar)

#Now create the stump
topPlate = P.makeCircle(D/2., V([0,0,0]), V([0,0,1]))
bottomPlate = P.makeCircle(D/2.+gap, V([0,0,height]), V([0,0,1]))
stump = P.makeLoft([topPlate, bottomPlate], True)
baseAdapter.rotate(V([0,0,0]), V([1,0,0]), 180)
baseAdapter.translate(V([0,0,height+lShaft]))
stump = stump.fuse(baseAdapter)
boltHole = P.makeCylinder(dBoltHole/2., lBoltHole, V([D/4,0,0]))
stump = stump.cut(boltHole)
boltHole.translate(V([-D/2,0,0]))
stump = stump.cut(boltHole)
stump.exportStl(outFolder+'stump.stl')
P.show(stump)

#Now create the sheath
outerBottomPlate = P.makeCircle(D/2.+sheathWidth,  V([0,0,0]), V([0,0,1]))
outerTopPlate = P.makeCircle(D/2.+gap+sheathWidth, V([0,0,height+sheathWidth]), V([0,0,1]))
sheath = P.makeLoft([outerBottomPlate, outerTopPlate], True)
stump.translate(V([0,0,sheathWidth]))
sheath = sheath.cut(stump)
boltHeadHole = P.makeCylinder(dBoltHead/2., hBoltHead+15.0, V([D/4.,0,sheathWidth-hBoltHead]), V([0,0,1]))
sheath = sheath.cut(boltHeadHole)
boltHeadHole.translate(V([-D/2.,0,0]))
sheath = sheath.cut(boltHeadHole)
sheath.rotate(V([0,0,(height+sheathWidth)/2.]), V([1,0,0]), 180)
baseAdapter.translate(V([0,0,sheathWidth]))
sheath = sheath.fuse(baseAdapter)
sheath.rotate(V([0,0,(sheathWidth+height+lShaft)/2]), V([1,0,0]), 180)
sheath.translate(V([(D+sheathWidth+2*gap)+3,0,0]))
sheath.exportStl(outFolder+'sheath.stl')
P.show(sheath)

#Save parameters to pickle file for sheet cutout code to use
pickle.dump([n, D, gap, dBoltHole], open(u"P:\\Work\\stampFolding\\tempParameters.p", 'wb'))

#Derived parameters