import os
import matplotlib.pyplot as plt
import data

def GenerateGraphs():
    fig1, grph1 = plt.subplots() 
    fig2, grph2 = plt.subplots()   
    

    grph1.xaxis.set_label_text('Orbital Radius / AU')
    grph1.yaxis.set_label_text('Orbital Period / Years')
    grph1.set_title('Kepler III Correlation')
    grph1.plot(data.SemiMajorAxis, data.OrbPeriod, 'cD-')
    
    xvals = []
    for i in range(len(data.OrbPeriod)):
        xvals.append(data.SemiMajorAxis[i]**(3/2))
    grph2.xaxis.set_label_text('Orbital Radius / AU^3/2')
    grph2.yaxis.set_label_text('Orbital Period / Years')
    grph2.plot(xvals, data.OrbPeriod, 'rD-')
    
    plt.show()  
    return [fig1, fig2]

#data.GenerateScript(os.path.basename(__file__), GenerateGraphs())