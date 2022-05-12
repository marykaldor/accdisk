import os
import random
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
from shapely.geometry import LineString
from matplotlib.ticker import MultipleLocator
import math

# Open old file in read mode and create new file in write mode
fin = open("/Users/marykaldor/accdisk/fortran/" + "parfile_original.dat", "r")
fout = open("/Users/marykaldor/accdisk/fortran/" + "parfile.dat", "w")

q = random.randint(1, 3)
angi = random.randint(15, 115)
xi1 = random.randint(70, 1000)
xi2 = random.randint(1500, 6000)
viewangle = random.randint(0, 360)
amp = random.randint(0, 4)
xispin = random.randint(150, 4500)
pitch = random.randint(0, 160)
angwidth = random.randint(35, 100)

in_range = False
qout = 0
angiout = 0
xi1out = 0
xi2out = 0
viewangleout = 0
ampout = 0
xispinout = 0
pitchout = 0
angwidthout = 0


def inrange():
    global in_range
    global q
    global angi
    global xi1
    global xi2
    global viewangle
    global amp
    global xispin
    global pitch
    global angwidth
    global qout
    global angiout
    global xi1out
    global xi2out
    global viewangleout
    global ampout
    global xispinout
    global pitchout
    global angwidthout
    q = random.randint(1, 3)
    angi = random.randint(15, 115)
    xi1 = random.randint(70, 1000)
    xi2 = random.randint(1500, 6000)
    viewangle = random.randint(0, 360)
    amp = random.randint(0, 4)
    xispin = random.randint(150, 4500)
    pitch = random.randint(0, 160)
    angwidth = random.randint(35, 100)
    if q == 1 and angi in range(17, 23) and xi1 in range(150, 190) and xi2 in range(1500, 2300) and viewangle in range(127, 163) and amp == 4 and xispin == 800 and pitch in range(20, 50) and angwidth == 35:
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 1 and angi == 20 and xi1 == 100 and xi2 in range(1500, 2300) and viewangle == 40 and amp == 4 and xispin == 800 and pitch in range(20, 50) and angwidth == 35:
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 1 and angi == 20 and xi1 == 100 and xi2 in range(1500, 2300) and viewangle == 90 and amp == 2 and xispin == 800 and pitch in range(20, 50) and angwidth == 35:
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 1 and angi == 20 and xi1 == 1000 and xi2 in range(2500, 3500) and viewangle == 90 and amp == 2 and xispin == 1000 and pitch in range(0, 20) and angwidth in range(15, 50):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 1 and angi == 25 and xi1 == 500 and xi2 in range(4500, 5500) and viewangle in range(35, 165) and amp == 4 and xispin == 4500 and pitch == 90 and angwidth in range(30, 40):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 1 and angi == 30 and xi1 == 600 and xi2 in range(5000, 6000) and viewangle in range(35, 105) and amp == 4 and xispin == 4400 and pitch == 90 and angwidth in range(50, 90):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 1 and angi in range(25, 35) and xi1 == 600 and xi2 in range(5000, 6000) and viewangle in range(0, 190) and amp == 4 and xispin == 4000 and pitch in range(70, 110) and angwidth in range(50, 90):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 1 and angi in range(25, 35) and xi1 == 600 and xi2 in range(5000, 6000) and viewangle in range(350, 360) and amp == 4 and xispin == 4000 and pitch in range(70, 110) and angwidth in range(50, 90):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 1 and angi in range(25, 35) and xi1 == 100 and xi2 in range(5000, 6000) and viewangle in range(10, 90) and amp == 4 and xispin == 4500 and pitch in range(70, 160) and angwidth in range(50, 90):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 1 and angi in range(25, 35) and xi1 == 100 and xi2 in range(4500, 5500) and viewangle in range(235, 355) and amp == 4 and xispin == 4500 and pitch in range(70, 160) and angwidth in range(50, 90):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 1 and angi in range(25, 35) and xi1 == 100 and xi2 in range(4500, 5500) and viewangle in range(15, 165) and amp == 4 and xispin == 4500 and pitch in range(70, 160) and angwidth in range(50, 90):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 1 and angi in range(40, 50) and xi1 in range(100, 500) and xi2 in range(4500, 5500) and viewangle in range(10, 30) and amp in range(2, 4) and xispin in range(3500, 4000) and pitch in range(70, 110) and angwidth in range(80, 100):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 2 and angi == 12 and xi1 in range(150, 190) and xi2 in range(1500, 2300) and viewangle in range(15, 65) and amp == 0 and xispin == 170 and pitch in range(20, 50) and angwidth == 35:
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 2 and angi == 20 and xi1 in range(70, 130) and xi2 in range(1500, 2300) and viewangle in range(265, 355) and amp == 4 and xispin == 800 and pitch in range(20, 50) and angwidth == 35:
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 2 and angi == 20 and xi1 in range(70, 130) and xi2 in range(1500, 2300) and viewangle in range(130, 160) and amp == 4 and xispin == 800 and pitch in range(20, 50) and angwidth == 35:
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 2 and angi == 15 and xi1 == 400 and xi2 in range(1500, 2300) and viewangle in range(35, 230) and amp == 3 and xispin == 800 and pitch in range(20, 50) and angwidth == 35:
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 2 and angi == 15 and xi1 == 200 and xi2 in range(1500, 2300) and viewangle in range(45, 115) and amp == 3 and xispin == 800 and pitch in range(20, 50) and angwidth == 35:
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 2 and angi == 15 and xi1 == 300 and xi2 in range(1500, 2300) and viewangle in range(195, 360) and amp == 3 and xispin == 800 and pitch in range(20, 50) and angwidth == 35:
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 2 and angi == 15 and xi1 == 300 and xi2 in range(1500, 2500) and viewangle in range(45, 115) and amp == 3 and xispin == 800 and pitch in range(20, 50) and angwidth == 35:
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 2 and angi == 15 and xi1 == 300 and xi2 in range(2500, 3500) and viewangle in range(85, 185) and amp == 3 and xispin == 800 and pitch in range(20, 50) and angwidth == 35:
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 2 and angi in range(85, 115) and xi1 in range(150, 200) and xi2 in range(1500, 2300) and viewangle in range(55, 125) and amp == 1 and xispin in range(150, 200) and pitch in range(20, 50) and angwidth == 35:
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False
    if q == 3 and angi == 20 and xi1 == 100 and xi2 in range(1500, 2300) and viewangle in range(65, 95) and amp == 4 and xispin == 800 and pitch in range(20, 50) and angwidth == 35:
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        viewangleout = viewangle
        ampout = amp
        xispinout = xispin
        pitchout = pitch
        angwidthout = angwidth
        return
    else:
        in_range = False


inrange()

parameters = ["OUTFILE", "Q", "ANGI", "XI1", "XI2", "AMP", "AOBS", "PITCH", "WIDTH", "XISPIN"]
z = 0
d = 1
adjust2 = " "
outfile = " "

# Go through text and only change given parameter's value
# Everything else just gets rewritten to the new file
while d < 11:
    print(parameters)
    print(parameters[z])
    fin = open("/Users/marykaldor/accdisk/fortran/" + "parfile_original.dat", "r")
    fout = open("/Users/marykaldor/accdisk/fortran/" + "parfile.dat", "w")
    tally = 0
    in_range = False
    while not in_range:
        print("not in range")
        inrange()
    for line in fin:
        print("found!")
        found = False
        x = line.split()
        if parameters[z] in line and parameters[z] == x[1]:
            found = True
            if parameters[z] == x[1]:
                if parameters[z] == "ANGI":
                    adjust2 = str(angiout)
                if parameters[z] == "XI1":
                    adjust2 = str(xi1out)
                if parameters[z] == "XI2":
                    adjust2 = str(xi2out)
                if parameters[z] == "Q":
                    adjust2 = str(qout)
                if parameters[z] == "AMP":
                    adjust2 = str(ampout)
                if parameters[z] == "AOBS":
                    adjust2 = str(viewangleout)
                if parameters[z] == "PITCH":
                    adjust2 = str(pitchout)
                if parameters[z] == "WIDTH":
                    adjust2 = str(angwidthout)
                if parameters[z] == "XISPIN":
                    adjust2 = str(xispinout)
                if parameters[z] == "OUTFILE":
                    adjust2 = ("moments-fullparams" + str(d))
                    outfile = adjust2
                fout.write(line.replace(x[0], adjust2))
                if parameters[z] != parameters[-1]:
                    z += 1
                else:
                    z = 0
        if not found:
            fout.write(line)
    fin.close()
    fout.close()
    os.system("./rel_profile_wave_pkg.x")
    d += 1
print("Done")

colors = ("red", "orange", "yellow", "lime", "cyan", "teal", "blue", "purple", "fuchsia", "darkgrey")
colorchoice = iter(colors)

# Reading the file
i = 0
k = 1
fig, ax = plt.subplots()

while i < 10:
    wavelength = []
    flambda = []
    noise = []
    ratio = []
    cont = 1
    sqrtcont = math.sqrt(cont)
    SN_cont = 20
    sigmacont = 1/SN_cont
    selected_lines = []
    filename = ("island_" + str(k))
    f = open("/Users/marykaldor/accdisk/fortran/" + filename, "r")
    lines = f.readlines()

# old idea
    # sigma = sigmacont*squareroot/sqrtcont

# Gets rid of pound symbol lines
    for line in lines:
        if line[0] == "#":
            pass
        else:
            x, y = line.split()
            y = y.strip("\n")
            x = float(x)
            y = float(y)
            flux = y + cont
            squareroot = math.sqrt(flux)
            sigma = sigmacont*math.sqrt((flux/cont)+1)
            fluxnew = np.random.normal(flux, sigma)
            n = fluxnew - y - cont
            r = fluxnew/flux
            wavelength.append(x)
            flambda.append(fluxnew)
            noise.append(n)
            ratio.append(r)
            selected_lines.append(line)

# Plots spectrum along with half maximum horizontal line
    # maximum = max(flambda)
    maximum = 1
    x = [4400, 5400]
    y = [maximum/2, maximum/2]
    plt.plot(wavelength, flambda, color=next(colorchoice), label="Island_" + str(k))
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
    plt.savefig("/Users/marykaldor/accdisk/fortran/island_" + str(k) + ".pdf")
    i += 1
    k += 1

# plt.text(6700, 0.8, "Test Label", fontname="Times New Roman")
# plt.text(6375, 0.3, "Test Label", fontname="Times New Roman")
plt.show()
print("Done")

'''
plt.plot(wavelength, noise, color=next(colorchoice), label="Noise_" + str(k))
plt.plot(wavelength, ratio, color=next(colorchoice), label="Ratio_" + str(k))
'''
