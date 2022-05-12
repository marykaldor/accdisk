import os
import random
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString
from matplotlib.ticker import MultipleLocator

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

tally = 0
while in_range == False:
    print(tally)
    tally += 1
    inrange()

print(in_range, tally)
print("q", q, "qout", qout, "angi", angi, "angiout", angiout, "xi1", xi1, "xi1out", xi1out, "xi2", xi2, "xi2out",
      xi2out)

parameters = ["OUTFILE", "ANGI", "XI1", "XI2", "Q"]
j = 0
adjust2 = " "
outfile = " "

# Go through text and only change given parameter's value
# Everything else just gets rewritten to the new file
for line in fin:
    found = False
    x = line.split()
    if parameters[j] in line and parameters[j] == x[1]:
        found = True
        if parameters[j] == x[1]:
            if parameters[j] == "ANGI":
                print("angi")
                adjust2 = str(angiout)
            if parameters[j] == "XI1":
                print("xi1")
                adjust2 = str(xi1out)
            if parameters[j] == "XI2":
                print("xi2")
                adjust2 = str(xi2out)
            if parameters[j] == "Q":
                print("q")
                adjust2 = str(qout)
            if parameters[j] == "OUTFILE":
                print("outfile")
                adjust2 = "brute-force"
                outfile = adjust2
                print(outfile)
            print(adjust2)
            fout.write(line.replace(x[0], adjust2))
            if parameters[j] == parameters[-1]:
                pass
            else:
                j += 1
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
plt.savefig("/Users/marykaldor/accdisk/fortran/bruteforce" + ".pdf")

plt.show()
print("Done")
