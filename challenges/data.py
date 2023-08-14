import mpld3 as mpld

OrbPeriod = [0.24, 0.62, 1.00, 1.88, 11.86, 29.63, 84.75, 166.34, 248.35]
SemiMajorAxis = [0.387, 0.723, 1, 1.523, 5.20, 9.58, 19.29, 30.25, 39.51]
Eccentricity = [0.21, 0.01, 0.02, 0.09, 0.05, 0.06, 0.05, 0.01]
Mass = [0.055, 0.815, 1, 0.107, 317.85, 95.16, 14.50, 17.20, 0.00]
Radius = [0.38, 0.95, 1, 0.53, 11.21, 9.45, 4.01, 3.88, 0.19]
RotationalPeriod = [58.65, 243.02, 1, 1.03, 0.41, 0.44, 0.72, 0.67, 6.39]


def GenerateScript(this_file, graphs):
    script = ""
    html_file = this_file.replace(".py", ".html")
    file_path = "challenges\website\ " + html_file
    file_path = file_path.replace(" ", "")
    for i in graphs:
        script = script + mpld.fig_to_html(i) + "\n"
    script = "<!-- here -->\n\n" + script 
    with open(file_path, 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].__contains__("<!-- here -->"):
            lines[i] = script
    with open(file_path, 'w') as f:
        f.writelines(lines)
        
#data.GenerateScript(os.path.basename(__file__), GenerateGraphs())