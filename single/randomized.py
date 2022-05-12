import os
import random
from random import sample
import matplotlib.pyplot as plt
import numpy as np
import math
from shapely.geometry import LineString
from matplotlib.ticker import MultipleLocator

# Open old file in read mode and create new file in write mode
fin = open("/Users/marykaldor/accdisk/fortran/" + "parfile_original.dat", "r")
fout = open("/Users/marykaldor/accdisk/fortran/" + "parfile.dat", "w")

# Setting up random parameter list
# Start will all options, then randomly select a smaller amount
parametersfull = ["NSTEP", "OUTFILE", "Q", "ANGI", "XI1", "XI2", "BROAD", "AMP", "PITCH"]
i = random.randint(1, 9)
parameters = sample(parametersfull, i)

# Make sure that outfile is in parameter list
if "OUTFILE" in parameters:
    pass
else:
    parameters.append("OUTFILE")
print(parameters)

# Setting up range over which to iterate
j = 0
k = len(parameters)
low = 0
high = 1
found = False
#outfile = "outfile"

# Go through text and only change given parameter's value
# Everything else just gets rewritten to the new file
for line in fin:
    found = False
    for j in range(0, k):
        x = line.split()
        if parameters[j] in line and parameters[j] == x[1]:
            found = True
            if parameters[j] == x[1]:
                if parameters[j] == "ANGI":
                    print("angi")
                    low = 15
                    high = 60
                if parameters[j] == "XI1":
                    print("xi1")
                    low = 100
                    high = 10000
                if parameters[j] == "XI2":
                    print("xi2")
                    low = 10000
                    high = 1000000
                if parameters[j] == "Q":
                    print("q")
                    low = 1
                    high = 3
                if parameters[j] == "BROAD":
                    print("broad")
                    low = 400
                    high = 1500
                if parameters[j] == "AMP":
                    print("amp")
                    low = 0
                    high = 4
                if parameters[j] == "PITCH":
                    print("pitch")
                    low = -90
                    high = 0
                adjust2 = str(random.uniform(low, high))
                if parameters[j] == "NSTEP":
                    print("nstep")
                    low = 50
                    high = 100
                    adjust2 = str(int(random.uniform(low, high)))
                if parameters[j] == "OUTFILE":
                    print("outfile")
                    adjust2 = "randomized"
                    outfile = adjust2
                    print(outfile)
                print(adjust2)
                fout.write(line.replace(x[0], adjust2))
                if parameters[j] == parameters[-1]:
                    pass
                else:
                    j += 1
    print(found)
    if not found:
        fout.write(line)

fin.close()
fout.close()
os.system("./rel_profile_wave_pkg.x")
print("Done")

# Reading the file
fig, ax = plt.subplots()
wavelength = []
flambda = []
selected_lines = []
f = open(outfile)
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
x = [4000, 6000]
y = [maximum/2, maximum/2]
plt.plot(wavelength, flambda, color="blue", label="SinglePlot")
plt.legend(prop={"family": "Times New Roman"})
plt.plot(x, y, "-r")

# Find the intersection between spectrum and half max line, finds the x coordinates
# of those locations, then takes the difference of those to find the FWHM.
# LineString allows for interpolation between points so that we can find an exact
# intersection because sometimes there is no x value for an exact y = 0.5 value.
line1 = LineString(np.column_stack((x, y)))
line2 = LineString(np.column_stack((wavelength, flambda)))
intersection = line1.intersection(line2)
# x1, x2 = line1.intersection(line2)
# fwhm = x2.x - x1.x
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
plt.savefig("/Users/marykaldor/accdisk/fortran/randomized" + ".pdf")

plt.show()
print("Done")
