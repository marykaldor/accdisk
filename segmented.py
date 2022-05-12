import os
import random
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
# from shapely.geometry import LineString
import matplotlib
# from matplotlib.ticker import MultipleLocator
import math
import statistics as stat
from tabulate import tabulate

# Open old file in read mode and create new file in write mode
fin = open("/Users/marykaldor/accdisk/fortran/" + "parfile_original.dat", "r")
fout = open("/Users/marykaldor/accdisk/fortran/" + "parfile.dat", "w")

q = random.randint(1, 3)
angi = random.randint(15, 115)
xi1 = random.randint(70, 1000)
xi2 = random.randint(1500, 6000)

in_range = False
qout = 0
angiout = 0
xi1out = 0
xi2out = 0


def inrange():
    global in_range
    global q
    global angi
    global xi1
    global xi2
    global qout
    global angiout
    global xi1out
    global xi2out
    q = random.randint(1, 3)
    angi = random.randint(15, 115)
    xi1 = random.randint(70, 1000)
    xi2 = random.randint(1500, 6000)
    if q == 1 and angi in range(17, 23) and xi1 in range(150, 190) and xi2 in range(1500, 2300):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 1 and angi == 20 and xi1 == 100 and xi2 in range(1500, 2300):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 1 and angi == 20 and xi1 == 1000 and xi2 in range(2500, 3500):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 1 and angi == 25 and xi1 == 500 and xi2 in range(4500, 5500):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 1 and angi == 30 and xi1 == 600 and xi2 in range(5000, 6000):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 1 and angi in range(25, 35) and xi1 == 600 and xi2 in range(5000, 6000):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 1 and angi in range(25, 35) and xi1 == 100 and xi2 in range(5000, 6000):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 1 and angi in range(25, 35) and xi1 == 100 and xi2 in range(4500, 5500):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 1 and angi in range(40, 50) and xi1 in range(100, 500) and xi2 in range(4500, 5500):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 2 and angi == 12 and xi1 in range(150, 190) and xi2 in range(1500, 2300):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 2 and angi == 20 and xi1 in range(70, 130) and xi2 in range(1500, 2300):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 2 and angi == 15 and xi1 == 400 and xi2 in range(1500, 2300):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 2 and angi == 15 and xi1 == 200 and xi2 in range(1500, 2300):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 2 and angi == 15 and xi1 == 300 and xi2 in range(1500, 2300):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 2 and angi == 15 and xi1 == 300 and xi2 in range(1500, 2500):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 2 and angi == 15 and xi1 == 300 and xi2 in range(2500, 3500):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 2 and angi in range(85, 115) and xi1 in range(150, 200) and xi2 in range(1500, 2300):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False
    if q == 3 and angi == 20 and xi1 == 100 and xi2 in range(1500, 2300):
        in_range = True
        qout = q
        angiout = angi
        xi1out = xi1
        xi2out = xi2
        return
    else:
        in_range = False


inrange()


def nmoment(x, weight, c, n):
    sum1 = 0
    norm = 0
    for p in range(len(x)):
        sum1 += (weight[p] * ((x[p] - c) ** n))
        norm += weight[p]
        # print("sum", sum)
    return sum1 / norm


def velshiftstring(v):
    velocity = (v * 3e10) / 4861
    # print(velocity, "cm/s")
    velocity_km = velocity / 1e5
    vs = str(velocity_km) + " km/s"
    return vs


def velshiftfloat(v):
    velocity = (v * 3e10) / 4861
    # print(velocity, "cm/s")
    velocity_km = velocity / 1e5
    vs = velocity_km
    return vs


def psncalc(var1, var2):
    # Creating the 2d array for moment calculations
    a = nmoment(var1, var2, 0, 1)
    second = nmoment(var1, var2, a, 2)
    sg = math.sqrt(second)
    # Calculate Pearson skewness coefficient
    med = stat.median(var1)
    psn = (np.average(var1, weights=var2) - med) / sg
    return psn


def firstcalc(var1, var2):
    # Creating the 2d array for moment calculations
    a = nmoment(var1, var2, 0, 1)
    first = nmoment(wavelength, flambda, a, 1)
    # Calculate Pearson skewness coefficient
    return first


parameters = ["OUTFILE", "Q", "ANGI", "XI1", "XI2"]
z = 0
d = 1
adjust2 = " "
outfile = " "

# Go through text and only change given parameter's value
# Everything else just gets rewritten to the new file
while d < 3001:
    print(parameters)
    print(parameters[z])
    fin = open("/Users/marykaldor/accdisk/fortran/" + "parfile_original.dat", "r")
    fout = open("/Users/marykaldor/accdisk/fortran/" + "parfile.dat", "w")
    tally = 0
    in_range = False
    while not in_range:
        inrange()
    for line in fin:
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
                if parameters[z] == "OUTFILE":
                    adjust2 = ("moments" + str(d))
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
xf = "xfile"
fluxnewf = "fluxnewfile"
nf = "nfile"
rf = "rfile"
pf = "peakfile"
vsstringsf = "vsstrings"
vsfloatsf = "vsfloats"
psnsf = "psns"
firstsf = "firsts"
itf = "iterations"
xfile = open("/Users/marykaldor/accdisk/fortran/xfile/" + xf, "w")
fluxnewfile = open("/Users/marykaldor/accdisk/fortran/fluxnewfile/" + fluxnewf, "w")
nfile = open("/Users/marykaldor/accdisk/fortran/nfile/" + nf, "w")
rfile = open("/Users/marykaldor/accdisk/fortran/rfile/" + rf, "w")
peakfile = open("/Users/marykaldor/accdisk/fortran/peakfile/" + pf, "w")
vsstringsfile = open("/Users/marykaldor/accdisk/fortran/vsstrings/" + vsstringsf, "w")
vsfloatsfile = open("/Users/marykaldor/accdisk/fortran/vsfloats/" + vsfloatsf, "w")
psnsfile = open("/Users/marykaldor/accdisk/fortran/psns/" + psnsf, "w")
firstsfile = open("/Users/marykaldor/accdisk/fortran/firsts/" + firstsf, "w")
iterationsfile = open("/Users/marykaldor/accdisk/fortran/iterations/" + itf, "w")

wavelength = []
flambda = []

# Open, read file, do math, write new values off to external text files. Close them.
while i < 3000:
    cont = 1
    sqrtcont = math.sqrt(cont)
    SN_cont = 20
    sigmacont = 1 / SN_cont
    filename = ("moments" + str(k))
    f = open("/Users/marykaldor/accdisk/fortran/" + filename, "r")
    lines = f.readlines()
    fluxnewmax = 0
    wavelengthofmax = 0

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
            sigma = sigmacont * math.sqrt((flux / cont) + 1)
            fluxnew = np.random.normal(flux, sigma)
            n = fluxnew - y - cont
            r = fluxnew / flux
            if fluxnew > fluxnewmax:
                fluxnewmax = fluxnew
                wavelengthofmax = x
            xfile.write(str(x) + "\n")
            wavelength.append(x)
            fluxnewfile.write(str(fluxnew) + "\n")
            flambda.append(fluxnew)
            nfile.write(str(n) + "\n")
            rfile.write(str(r) + "\n")

    peakshift = 4861 - wavelengthofmax
    peakfile.write(str(peakshift) + "\n")
    vsstringsfile.write(str(velshiftstring(peakshift)) + "\n")
    vsfloatsfile.write(str(velshiftfloat(peakshift)) + "\n")
    psnsfile.write(str(psncalc(wavelength, flambda)) + "\n")
    firstsfile.write(str(firstcalc(wavelength, flambda)) + "\n")
    iterationsfile.write(str(k) + "\n")
    wavelength = []
    flambda = []
    i += 1
    k += 1

xfile.close()
fluxnewfile.close()
nfile.close()
rfile.close()
peakfile.close()
vsstringsfile.close()
vsfloatsfile.close()
psnsfile.close()
firstsfile.close()
iterationsfile.close()
i = 0
k = 1


def createlist(list):
    desiredlist = [str(list)]
    df = str(list)
    desired = open("/Users/marykaldor/accdisk/fortran/" + str(list) + "/" + str(df), "r")
    lines = desired.readlines()
    for line in lines:
        if list == "iterations" or "vsstrings":
            line = line.strip("km/s" + "\n")
            desiredlist.append(float(line))
        else:
            desiredlist.append(float(line))
    return desiredlist


iterations = "iterations"
psns = "psns"
firsts = "firsts"
vsstrings = "vsstrings"
vsfloats = "vsfloats"

table = [createlist(iterations), createlist(psns), createlist(firsts), createlist(vsstrings)]
print(tabulate(table))

# plt.plot(wavelength, flambda, color=next(colorchoice), label="PSN vs Peak Shift" + str(k))
# plt.legend(prop={"family": "Times New Roman"})

# Makes the plot pretty and displays the image.
plt.gcf().subplots_adjust(bottom=0.2, left=0.3)
plt.ticklabel_format(axis="both", style="sci", scilimits=(0, 0))
# ax.xaxis.set_minor_locator(MultipleLocator(100))
# ax.yaxis.set_minor_locator(MultipleLocator(500))
plt.xticks(fontname="Times New Roman")
# plt.xlim(2000,10000)
plt.yticks(fontname="Times New Roman")
# plt.ylim(-1, 1)
# plt.ticklabel_format(style="sci", axis="both")
# matplotlib.axes.Axes.ticklabel_format(fig, axis="both", style="sci")
# matplotlib.axes.Axes.set_xticks(["2000", "3000", "4000", "5000", "6000", "7000", "8000", "9000", "10000"])
# matplotlib.axes.Axes.set_yticks(["-1", "-0.5", "0", "0.5", "1"])
plt.xlabel("Peak Shift (km/s)", fontname="Times New Roman")
plt.ylabel("Pearson Skewness Coefficient", fontname="Times New Roman")
plt.title("Pearson Skewness Coefficient vs. Peak Shift", fontname="Times New Roman")
plt.savefig("/Users/marykaldor/accdisk/fortran/psnvspeakshift.pdf")

# Making labels with movable locations
# plt.text(6700, 0.8, "Test Label", fontname="Times New Roman")
# plt.text(6375, 0.3, "Test Label", fontname="Times New Roman")

psnslist = createlist(psns)
psnslist.pop(0)
vsfloatslist = createlist(vsfloats)
vsfloatslist.pop(0)

print("vs", vsfloatslist)
print("psn", psnslist)

fig = plt.scatter(vsfloatslist, psnslist)

plt.show()
print("Done")
