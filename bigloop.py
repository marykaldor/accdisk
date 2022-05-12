import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString
from matplotlib.ticker import MultipleLocator
import os
import math


# fin = open("/Users/marykaldor/accdisk/fortran/" + "parfile_original.dat", "r")
# fout = open("/Users/marykaldor/accdisk/fortran/" + "parfile.dat", "w")

# Setting up list iterations
a = 0
parameters = ["OUTFILE", "ANGI", "XI1", "XI2"]
angis = ("5", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55", "60", "65", "70", "75", "80", "85")
anglechoice = iter(angis)

''' Do I need this?
# Give system parameter to change
# adjust = input("What would you like to change? ")
adjust = angis[1]
parameters.append(adjust)

while a < len(angis):
    # Check for more parameters. If there are none, end loop.
    if input("Would you like to change anything else? ") == "Yes":
        # adjust = input("What would you like to change? ")
        adjust = angis(next)
        parameters.append(adjust)
        a += 1
    else:
        a = 27
'''

# Setting up range over which to iterate
b = 0
c = len(parameters) - 1
d = 1
e = 5

f = 0
g = len(parameters) - 1
# Setting up adjustments and the values to base them off of
adjust2 = " "
fin = open("/Users/marykaldor/accdisk/fortran/" + "parfile_original.dat", "r")
while f < g:
    for line in fin:
        if parameters[f] in line:
            x = line.split()
            if parameters[f] == x[1]:
                if parameters[f] == "ANGI":
                    refangle = float(x[0])
                    print(refangle)
                if parameters[f] == "XI1":
                    refxi1 = float(x[0])
                    print(refxi1)
                if parameters[f] == "XI2":
                    refxi2 = float(x[0])
                    print(refxi2)
                if parameters[f] == parameters[-1]:
                    pass
                else:
                    f += 1
ratio1 = float(math.sin(refangle*math.pi/180.0)/math.sqrt(refxi1))
ratio2 = float(math.sin(refangle*math.pi/180.0)/math.sqrt(refxi2))

# Go through text and only change given parameter's value
# Everything else just gets rewritten to the new file
while d < len(angis)+1:
    # Open old file in read mode and create new file in write mode
    fin = open("/Users/marykaldor/accdisk/fortran/" + "parfile_original.dat", "r")
    fout = open("/Users/marykaldor/accdisk/fortran/" + "parfile.dat", "w")
    while b < c:
        for line in fin:
            if parameters[b] in line:
                x = line.split()
                if parameters[b] == x[1]:
                    print("The current value of ", parameters[b], " is ", x[0])
                    if parameters[b] == "OUTFILE":
                        adjust2 = "test_" + str(e) + "deg.dat"
                    if parameters[b] == "ANGI":
                        adjust2 = next(anglechoice)
                        newangle = adjust2
                    # XI values are based off of maintaining sin(i)
                    if parameters[b] == "XI1":
                        adjust2 = str(float((1*math.sin((float(newangle)*math.pi/180))/ratio1)**2))
                        print(adjust2)
                    if parameters[b] == "XI2":
                        adjust2 = str(float((1*math.sin((float(newangle)*math.pi/180))/ratio2)**2))
                        print(adjust2)
                    fout.write(line.replace(x[0], adjust2))
                    if parameters[b] == parameters[-1]:
                        pass
                    else:
                        b += 1
                else:
                    fout.write(line)
            else:
                fout.write(line)
    fin.close()
    fout.close()
    # Run executable to create model based off new parfile
    os.system("./rel_profile_wave_pkg.x")
    b = 0
    d += 1
    e += 5

print("Done")

lines = []
selected_lines = []
wavelength = []
flambda = []
colors = ("red", "orangered", "orange", "yellow", "lime", "green", "cyan", "teal", "lightblue", "blue", "darkblue",
          "purple", "fuchsia", "violet", "pink", "darkgrey", "grey")
colorchoice = iter(colors)

# Reading the file
i = 0
j = 5
fig, ax = plt.subplots()

while i < len(angis):
    wavelength = []
    flambda = []
    filename = ("test_" + str(j) + "deg.dat")
    f = open("/Users/marykaldor/accdisk/fortran/" + filename, "r")
    lines = f.readlines()

# Gets rid of pound symbol lines
    for line in lines:
        if line[0] == "#":
            pass
        else:
            x, y = line.split()
            y = y.strip("\n")
            x = float(x)
            y = float(y)
            wavelength.append(x)
            flambda.append(y)
            selected_lines.append(line)

# Plots spectrum along with half maximum horizontal line
    maximum = max(flambda)
    x = [6300, 6900]
    y = [maximum/2, maximum/2]
    plt.plot(wavelength, flambda, color=next(colorchoice), label="Test_" + str(j) + "deg")
    plt.legend(prop={"family": "Times New Roman"})
    plt.plot(x, y, "-0")

# Find the intersection between spectrum and half max line, finds the params coordinates
# of those locations, then takes the difference of those to find the FWHM.
# LineString allows for interpolation between points so that we can find an exact
# intersection because sometimes there is no params value for an exact y = 0.5 value.
    line1 = LineString(np.column_stack((x, y)))
    line2 = LineString(np.column_stack((wavelength, flambda)))
    intersection = line1.intersection(line2)
    # x1, x2 = line1.intersection(line2)
    # fwhm = x2.params - x1.params
    # print(fwhm, "A")

# Makes the plot pretty and displays the image.
    plt.gcf().subplots_adjust(bottom=0.2)
    ax.xaxis.set_minor_locator(MultipleLocator(20))
    ax.yaxis.set_minor_locator(MultipleLocator(0.1))
    plt.xticks(fontname="Times New Roman")
    plt.yticks(fontname="Times New Roman")
    plt.xlabel("Wavelength (A)", fontname="Times New Roman")
    plt.ylabel("$f_{\u03BB}$", fontname="Times New Roman")
    plt.title("$f_{\u03BB}$ vs. Wavelength", fontname="Times New Roman")
    plt.savefig("/Users/marykaldor/accdisk/fortran/test_" + str(j) + "deg.pdf")
    i += 1
    j += 5

plt.text(6700, 0.8, "Test Label", fontname="Times New Roman")
plt.text(6375, 0.3, "Test Label", fontname="Times New Roman")
plt.show()
print("Done")
