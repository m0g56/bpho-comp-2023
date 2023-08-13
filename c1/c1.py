import mpld3 as mpld
import matplotlib.pyplot as plt
import math

G = 6.67 * (10 ** -11)
PI = math.pi
M = 1.9891 * (10 ** 30)
multiplier = (G * M) / (4 * (PI ** 2))

def GenerateGraph():
    fig, grph = plt.subplots()    
    xvals = []
    OrbPeriod = [29.63, 84.75, 11.86, 166.34, 1.88, 0.62, 0.24, 1.00]
    for i in range(len(OrbPeriod)):
        xvals.append(multiplier * OrbPeriod[i])
    grph.plot(xvals, OrbPeriod, 'ro') 
    plt.show()
    #return mpld.fig_to_html(fig)




def GenerateScript(script):
    script = "<!-- here -->\n\n" + script
    with open('index.html', 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].__contains__("<!-- here -->"):
            lines[i] = script
    with open('index.html', 'w') as f:
        f.writelines(lines)

GenerateGraph()