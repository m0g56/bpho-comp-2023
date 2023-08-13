import mpld3 as mpld
import matplotlib.pyplot as plt
import math




def GenerateGraph():
    fig, grph = plt.subplots()
    grph.plot([1, 2, 3, 4], [1 , 4 , 9 ,16], 'ro')
    plt.show()
    return mpld.fig_to_html(fig)




def write(script):
    script = "<!-- here -->\n\n" + script
    with open('index.html', 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].__contains__("<!-- here -->"):
            lines[i] = script
    with open('index.html', 'w') as f:
        f.writelines(lines)
