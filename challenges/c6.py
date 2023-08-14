import os
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.optimize import newton
import data

x=[]
y=[]
colours = ['k-', 'r-','b-', 'm-', 'y-', 'r-','c-','b-', 'k-']

def DrawOrbit(planet):
    xvals = []
    yvals = []
    for i in range(1000):
        theta = i*2*math.pi/1000
        r  = (data.SemiMajorAxis[planet]*(1-data.Eccentricity[planet]**2))/(1-(data.Eccentricity[planet]*math.cos(theta)))
        xvals.append(r * math.cos(theta))
        yvals.append(r* math.sin(theta))
    return[xvals, yvals, colours[planet]]


def GenerateSpirograph(planeta, planetb):
    fig, grph = plt.subplots()
        
    grph.xaxis.set_label_text('x / AU')
    grph.yaxis.set_label_text('y / AU')
    grph.set_title('Spirograph of ' + data.PlanetName[planeta] + ' and ' + data.PlanetName[planetb] + ' orbits')
    
    if data.OrbPeriod[planeta] > data.OrbPeriod[planetb]:
        OrbSize = data.OrbPeriod[planeta]
    else:
        OrbSize = data.OrbPeriod[planetb]
    count = 0
    time = 0
    while count != 10*100:
        time = count*OrbSize/100
        count += 1
        x.clear()
        y.clear()
        
        theta = -time*2*math.pi/data.OrbPeriod[planeta]
        r  = (data.SemiMajorAxis[planeta]*(1-data.Eccentricity[planeta]**2))/(1-(data.Eccentricity[planeta]*math.cos(theta)))
        x.append(r * math.cos(theta))
        y.append(r* math.sin(theta))
        theta = -time*2*math.pi/data.OrbPeriod[planetb]
        r  = (data.SemiMajorAxis[planetb]*(1-data.Eccentricity[planetb]**2))/(1-(data.Eccentricity[planetb]*math.cos(theta)))

        x.append(r * math.cos(theta))
        y.append(r* math.sin(theta))
        grph.plot(x, y, '#00000040')
    
    grph.plot(0, 0, 'yo')
    orbita = DrawOrbit(planeta)
    grph.plot(orbita[0], orbita[1], orbita[2])
    orbitb = DrawOrbit(planetb)
    grph.plot(orbitb[0], orbitb[1], orbitb[2])
    
    plt.show()
    return [fig]

#figs = []
#figs.append(GenerateSpirograph(1, 2))
#figs.append(GenerateSpirograph(6, 7))
#figs.append(GenerateSpirograph(7, 8))


data.GenerateScript(os.path.basename(__file__), GenerateSpirograph(7, 8))
data.GenerateScript(os.path.basename(__file__), GenerateSpirograph(6, 7))
data.GenerateScript(os.path.basename(__file__), GenerateSpirograph(1, 2))