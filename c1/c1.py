import mpld3 as mpld
import matplotlib.pyplot as plt

def GenerateGraphs():
    fig1, grph1 = plt.subplots() 
    fig2, grph2 = plt.subplots()    
    xvals = []
    OrbPeriod = [29.63, 84.75, 11.86, 166.34, 248.35, 1.88, 0.62, 0.24, 1.00]
    OrbPeriod.sort()
    for i in range(len(OrbPeriod)):
        xvals.append(OrbPeriod[i]**(2/3))
    grph1.xaxis.set_label_text('Orbital Radius / AU')
    grph1.yaxis.set_label_text('Orbital Period / Years')
    grph1.set_title('Kepler III Correlation')
    grph1.plot(xvals, OrbPeriod, 'cD-')
    grph2.xaxis.set_label_text('Orbital Radius / AU^3/2')
    grph2.yaxis.set_label_text('Orbital Period / Years')
    grph2.plot(OrbPeriod, OrbPeriod, 'rD-')  
    plt.show()  
    return [fig1, fig2]


def GenerateScript(graphs):
    script = ""
    for i in graphs:
        script = script + mpld.fig_to_html(i) + "\n"
    script = "<!-- here -->\n\n" + script 
    with open('c1\c1.html', 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].__contains__("<!-- here -->"):
            lines[i] = script
    with open('c1\c1.html', 'w') as f:
        f.writelines(lines)

yes = GenerateGraphs()