import os
import matplotlib.pyplot as plt
import math
import data

colours = ['k-', 'r-','b-', 'm-', 'y-', 'r-','c-','b-']
        

def GenerateGraphs():
    #generate a graph mapping the elliptical orbit of the inner 4 planets with the sun at 0,0
    fig1, grph1 = plt.subplots()
    
    grph1.plot(0, 0, 'yo')
    for j in range(0,4):
        xvals = []
        yvals = []
        for i in range(1000):
            theta = i*2*math.pi/1000
            r  = (data.SemiMajorAxis[j]*(1-data.Eccentricity[j]**2))/(1-(data.Eccentricity[j]*math.cos(theta)))
            xvals.append(r * math.cos(theta))
            yvals.append(r* math.sin(theta))
        grph1.plot(xvals, yvals, colours[j])
    
    grph1.xaxis.set_label_text('x / AU')
    grph1.yaxis.set_label_text('y / AU')
    grph1.set_title('Orbits of the Planets')
    
    #generate a graph mapping the elliptical orbit of all the planets with the sun at 0,0
    fig2, grph2 = plt.subplots()
    
    grph2.plot(0, 0, 'yo')
    for j in range(len(data.SemiMajorAxis)-1):
        xvals = []
        yvals = []
        for i in range(1000):
            theta = i*2*math.pi/1000
            r  = (data.SemiMajorAxis[j]*(1-data.Eccentricity[j]**2))/(1-(data.Eccentricity[j]*math.cos(theta)))
            xvals.append(r * math.cos(theta))
            yvals.append(r* math.sin(theta))
        grph2.plot(xvals, yvals, colours[j])
    
    grph2.xaxis.set_label_text('x / AU')
    grph2.yaxis.set_label_text('y / AU')
    grph2.set_title('Orbits of the Planets')
    
    plt.show()
    return [fig1, fig2]

#data.GenerateScript(os.path.basename(__file__), GenerateGraphs())