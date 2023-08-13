import mpld3 as mpld
import matplotlib.pyplot as plt
import math

SemiMajorAxis = [0.387, 0.723, 1, 1.523, 5.20, 9.58, 19.29, 30.25]
Eccentricity = [0.21, 0.01, 0.02, 0.09, 0.05, 0.06, 0.05, 0.01]
colours = ['k-', 'r-','b-', 'm-', 'y-', 'r-','c-','b-']
#work out the semi-major axis from the orbital period
        

def GenerateGraph():
    #generate a graph mapping the elliptical orbit of each planet with the sun at 0,0
    fig1, grph1 = plt.subplots()
    
    grph1.plot(0, 0, 'yo')
    for j in range(0,4):
        xvals = []
        yvals = []
        for i in range(1000):
            theta = i*2*math.pi/1000
            r  = (SemiMajorAxis[j]*(1-Eccentricity[j]**2))/(1-(Eccentricity[j]*math.cos(theta)))
            xvals.append(r * math.cos(theta))
            yvals.append(r* math.sin(theta))
        grph1.plot(xvals, yvals, colours[j])
    
    grph1.xaxis.set_label_text('x / AU')
    grph1.yaxis.set_label_text('y / AU')
    grph1.set_title('Orbits of the Planets')
    
    fig2, grph2 = plt.subplots()
    
    grph2.plot(0, 0, 'yo')
    for j in range(len(SemiMajorAxis)):
        xvals = []
        yvals = []
        for i in range(1000):
            theta = i*2*math.pi/1000
            r  = (SemiMajorAxis[j]*(1-Eccentricity[j]**2))/(1-(Eccentricity[j]*math.cos(theta)))
            xvals.append(r * math.cos(theta))
            yvals.append(r* math.sin(theta))
        grph2.plot(xvals, yvals, colours[j])
    
    grph2.xaxis.set_label_text('x / AU')
    grph2.yaxis.set_label_text('y / AU')
    grph2.set_title('Orbits of the Planets')
    
    plt.show()
    return [fig1, fig2]
    
def GenerateScript(graphs):
    script = ""
    for i in graphs:
        script = script + mpld.fig_to_html(i) + "\n"
    script = "<!-- here -->\n\n" + script 
    with open('c2\c2.html', 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].__contains__("<!-- here -->"):
            lines[i] = script
    with open('c2\c2.html', 'w') as f:
        f.writelines(lines)