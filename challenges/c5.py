import os
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.optimize import newton
import data

P = data.OrbPeriod[8]
e = data.Eccentricity[8]
a = data.SemiMajorAxis[8]

def GenerateGraphs():
    fig, grph = plt.subplots()
    grph.xaxis.set_label_text('Time / Years')
    grph.yaxis.set_label_text('Orbit Polar Angle / Radians')
    grph.set_title('Angle vs Time for planets of varying eccentricity')

    tvals = []
    cpavals = []
    ppavals = []
    
    for i in range(3000):   
        time = (i+1)*P/1000
        tvals.append(time)
        theta = i*2*math.pi/1000
        #plot of a planet with 0 eccentricity    
        cpavals.append(theta)
        #plot of pluto
        ppavals.append(polar_angle_coordinate(time, P, e)+(2*math.pi*int((i)/1000)))
    grph.plot(tvals, cpavals, 'b-')
    grph.plot(tvals, ppavals, 'c-')

    plt.show()
    return [fig]
    
def polar_angle_coordinate(t, P, ecc):
    # Step 1: Calculate mean anomaly
    M = 2 * np.pi * (t / P)

    # Step 2: Solve Kepler's equation for eccentric anomaly
    def kepler_equation(E):
        return E - ecc * np.sin(E) - M

    E = newton(kepler_equation, M)  # Using Newton-Raphson for solving Kepler's equation

    # Step 3: Compute true anomaly
    nu = 2 * np.arctan2(np.sqrt(1 + ecc) * np.sin(E / 2), np.sqrt(1 - ecc) * np.cos(E / 2))

    # Step 4: Calculate polar angle coordinate
    theta = nu % (2 * np.pi)

    # Make sure theta is greater than 0
    if theta <= 0:
        theta += 2 * np.pi

    return theta

#data.GenerateScript(os.path.basename(__file__), GenerateGraphs())