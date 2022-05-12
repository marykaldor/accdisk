import os
import random
from random import sample
import matplotlib.pyplot as plt
import numpy as np
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

q = "0"
angi = "0"
xi1 = "0"
xi2 = "0"
amp = "0"
pitch = "0"

'''
def island1():
    q = 1
    angi = str(int(random.uniform(17, 23)))
    xi1 = str(int(random.uniform(150, 190)))
    xi2 = str(int(random.uniform(1500, 2300)))
    amp = 4
    pitch = str(int(random.uniform(20, 50)))

def island2():
    q = 1
    angi = 20
    xi1 = 100
    xi2 = str(int(random.uniform(1500, 2300)))
    amp = 4
    pitch= str(int(random.uniform(20, 50)))

def island3():
    q = 1
    angi = 20
    xi1 = 100
    xi2 = str(int(random.uniform(1500, 2300)))
    amp = 2
    pitch = str(int(random.uniform(20, 50)))

def island4():
    q = 1
    angi = 20
    xi1 = 1000
    xi2 = str(int(random.uniform(2500, 3500)))
    amp = 2
    pitch = str(int(random.uniform(0, 20)))

def island5():
    q = 1
    angi = 25
    xi1 = 500
    xi2 = str(int(random.uniform(4500, 5500)))
    amp = 4
    pitch = 90

def island6():
    q = 1
    angi = 30
    xi1 = 600
    xi2 = str(int(random.uniform(5000, 6000)))
    amp = 4
    pitch = 90

def island7():
    q = 1
    angi = str(int(random.uniform(25, 35)))
    xi1 = 600
    xi2 = str(int(random.uniform(5000, 6000)))
    amp = 4
    pitch = str(int(random.uniform(70, 110)))

def island8():
    q = 1
    angi = str(int(random.uniform(25, 35)))
    xi1 = 600
    xi2 = str(int(random.uniform(5000, 6000)))
    amp = 4
    pitch = str(int(random.uniform(70, 110)))

def island9():
    q = 1
    angi = str(int(random.uniform(25, 35)))
    xi1 = 100
    xi2 = str(int(random.uniform(5000, 6000)))
    amp = 4
    pitch = str(int(random.uniform(70, 160)))

def island10():
    q = 1
    angi = str(int(random.uniform(25, 35)))
    xi1 = 100
    xi2 = str(int(random.uniform(4500, 5500)))
    amp = 4
    pitch = str(int(random.uniform(70, 160)))

def island11():
    q = 1
    angi = str(int(random.uniform(25, 35)))
    xi1 = 100
    xi2 = str(int(random.uniform(4500, 5500)))
    amp = 4
    pitch = str(int(random.uniform(70, 160)))

def island12():
    q = 1
    angi = str(int(random.uniform(40, 50)))
    xi1 = str(int(random.uniform(100, 500)))
    xi2 = str(int(random.uniform(4500, 5500)))
    amp = str(int(random.uniform(2, 4)))
    pitch = str(int(random.uniform(70, 110)))

def island13():
    q = 2
    angi = 12
    xi1 = str(int(random.uniform(150, 190)))
    xi2 = str(int(random.uniform(1500, 2300)))
    amp = 0
    pitch = str(int(random.uniform(20, 50)))

def island14():
    q = 2
    angi = 20
    xi1 = str(int(random.uniform(70, 130)))
    xi2 = str(int(random.uniform(1500, 2300)))
    amp = 4
    pitch = str(int(random.uniform(20, 50)))

def island15():
    q = 2
    angi = 20
    xi1 = str(int(random.uniform(70, 130)))
    xi2 = str(int(random.uniform(1500, 2300)))
    amp = 4
    pitch = str(int(random.uniform(20, 50)))

def island16():
    q = 2
    angi = 15
    xi1 = 400
    xi2 = str(int(random.uniform(1500, 2300)))
    amp = 3
    pitch = str(int(random.uniform(20, 50)))

def island17():
    q = 2
    angi = 15
    xi1 = 200
    xi2 = str(int(random.uniform(1500, 2300)))
    amp = 3
    pitch = str(int(random.uniform(20, 50)))

def island18():
    q = 2
    angi = 15
    xi1 = 300
    xi2 = str(int(random.uniform(1500, 2300)))
    amp = 3
    pitch = str(int(random.uniform(20, 50)))

def island19():
    q = 2
    angi = 15
    xi1 = 300
    xi2 = str(int(random.uniform(1500, 2500)))
    amp = 3
    pitch = str(int(random.uniform(20, 50)))

def island20():
    q = 2
    angi = 15
    xi1 = 300
    xi2 = str(int(random.uniform(2500, 3500)))
    amp = 0
    pitch = str(int(random.uniform(20, 50)))

def island21():
    q = 2
    angi = str(int(random.uniform(85, 115)))
    xi1 = str(int(random.uniform(150, 200)))
    xi2 = str(int(random.uniform(1500, 2300)))
    amp = 1
    pitch = str(int(random.uniform(20, 50)))

def island22():
    q = 2
    angi = 20
    xi1 = 100
    xi2 = str(int(random.uniform(1500, 2300)))
    amp = 4
    pitch = str(int(random.uniform(20, 50)))

y = str(random.randint(1,22))
pick_island = "island" + y + "()"
'''

q = str(random.randint(1,3))
print(q)
in_range = False

def inrange():
    global in_range
    global q
    global angi
    global xi1
    global xi2
    if q == "1":
        angi = random.randint(17,50)
        print(angi)
        if angi not in range(17,24) and angi != 20 and angi != 25 and angi != 30 and angi not in range(25,36) and angi not in range(40,51):
            in_range = False
            return
        else:
            in_range = True
            angi = str(angi)
        xi1 = random.randint(100,1000)
        print(xi1)
        if xi1 not in range(150,190) and xi1 != 100 and xi1 != 1000 and xi1 != 500 and xi1 != 600 and xi1 not in range(100,500):
            in_range = False
            return
        else:
            in_range = True
            xi1 = str(xi1)
        xi2 = random.randint(1500,6000)
        print(xi2)
        if xi2 not in range(1500,2300) and xi2 not in range (2500,3500) and xi2 not in range(4500,5500) and xi2 not in range(5000,6000):
            in_range = False
            return
        else:
            in_range = True
            xi2 = str(xi2)
    if q == "2":
        angi = random.randint(12,115)
        print(angi)
        if angi != 12 and angi != 15 and angi != 20 and angi not in range(85,116):
            in_range = False
            return
        else:
            in_range = True
            angi = str(angi)
        xi1 = random.randint(70, 400)
        print(xi1)
        if xi1 not in range(150, 190) and xi1 not in range (70,130) and xi1 != 400 and xi1 != 200 and xi1 != 300 and xi1 not in range(150,200):
            in_range = False
            return
        else:
            in_range = True
            xi1 = str(xi1)
        xi2 = random.randint(1500, 6000)
        print(xi2)
        if xi2 not in range(1500, 2300) and xi2 not in range(2500, 3500):
            in_range = False
            return
        else:
            in_range = True
            xi2 = str(xi2)
    if q == "3":
        print(q)
        print('hi')
        angi = "20"
        xi1 = "100"
        xi2 = str(random.randint(1500,2300))
        in_range = True
        print(in_range)

print("in range", in_range)
inrange()
print("in range", in_range)

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
                    adjust2 = angi
                if parameters[j] == "XI1":
                    print("xi1")
                    adjust2 = xi1
                if parameters[j] == "XI2":
                    print("xi2")
                    adjust2 = xi2
                if parameters[j] == "Q":
                    print("q")
                    adjust2 = q
                if parameters[j] == "BROAD":
                    print("broad")
                    low = 400
                    high = 1500
                if parameters[j] == "AMP":
                    print("amp")
                    adjust2 = amp
                if parameters[j] == "PITCH":
                    print("pitch")
                    adjust2 = pitch
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
