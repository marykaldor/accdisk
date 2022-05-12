import os
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString
from matplotlib.ticker import MultipleLocator
import math
import statistics as stat

# Open old file in read mode and create new file in write mode
fin = open("/Users/marykaldor/accdisk/fortran/" + "parfile_original.dat", "r")
fout = open("/Users/marykaldor/accdisk/fortran/" + "parfile.dat", "w")

# Setting up list iterations
i = 0
parameters = []

# Give system parameter to change
adjust = input("What would you like to change? ")
parameters.append(adjust)

while i < 27:
    # Check for more parameters. If there are none, end loop.
    if input("Would you like to change anything else? ") == "Yes":
        adjust = input("What would you like to change? ")
        parameters.append(adjust)
        i += 1
    else:
        i = 27

# Setting up range over which to iterate
j = 0
k = len(parameters) - 1

# Go through text and only change given parameter's value
# Everything else just gets rewritten to the new file
while j < k:
    for line in fin:
        if parameters[j] in line:
            x = line.split()
            if parameters[j] == x[1]:
                print("The current value of ", parameters[j], " is ", x[0])
                adjust2 = input("What value would you like to use? ")
                if parameters[j] == "OUTFILE":
                    outfile = adjust2
                fout.write(line.replace(x[0], adjust2))
                if parameters[j] == parameters[-1]:
                    pass
                else:
                    j += 1
            else:
                fout.write(line)
        else:
            fout.write(line)

fin.close()
fout.close()
os.system("./rel_profile_wave_pkg.x")
print("Done")

# Reading the file
fig, ax = plt.subplots()
wavelength = []
flambda = []
noise = []
ratio = []
cont = 1
sqrtcont = math.sqrt(cont)
SN_cont = 20
sigmacont = 1/SN_cont
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
        flux = y + cont
        squareroot = math.sqrt(flux)
        sigma = sigmacont * math.sqrt((flux / cont) + 1)
        fluxnew = np.random.normal(flux, sigma)
        n = fluxnew - y - cont
        r = fluxnew / flux
        wavelength.append(x)
        flambda.append(fluxnew)
        noise.append(n)
        ratio.append(r)
        selected_lines.append(line)

# Plots spectrum along with half maximum horizontal line
maximum = max(flambda)
x = [6300, 6900]
y = [maximum/2, maximum/2]
plt.plot(wavelength, flambda, color="blue", label="SinglePlot")
plt.legend(prop={"family": "Times New Roman"})
# plt.plot(x, y, "-r")

# Find the intersection between spectrum and half max line, finds the params coordinates
# of those locations, then takes the difference of those to find the FWHM.
# LineString allows for interpolation between points so that we can find an exact
# intersection because sometimes there is no params value for an exact y = 0.5 value.
line1 = LineString(np.column_stack((x, y)))
line2 = LineString(np.column_stack((wavelength, flambda)))
intersection = line1.intersection(line2)
x1, x2 = line1.intersection(line2)
fwhm = x2.params - x1.params
print(fwhm, "A")

# Makes the plot pretty and displays the image.
plt.gcf().subplots_adjust(bottom=0.2)
ax.xaxis.set_minor_locator(MultipleLocator(20))
ax.yaxis.set_minor_locator(MultipleLocator(0.1))
plt.xticks(fontname="Times New Roman")
plt.yticks(fontname="Times New Roman")
plt.xlabel("Wavelength (A)", fontname="Times New Roman")
plt.ylabel("$f_{\u03BB}$", fontname="Times New Roman")
plt.title("$f_{\u03BB}$ vs. Wavelength", fontname="Times New Roman")
plt.savefig("/Users/marykaldor/accdisk/fortran/singlemoments" + ".pdf")

def nmoment(x, weight, c, n):
    sum = 0
    norm = 0
    for i in range(len(x)):
        sum += (weight[i]*((x[i] - c) ** n))
        norm += weight[i]
        # print("sum", sum)
    return sum / norm

# (np.average(wavelength, weights=flambda))
a = nmoment(wavelength, flambda, 0, 1)
print("my formula", a, "\n")
first = nmoment(wavelength, flambda, a, 1)
second = nmoment(wavelength, flambda, a, 2)
third = nmoment(wavelength, flambda, a, 3)
fourth = nmoment(wavelength, flambda, a, 4)
sg = math.sqrt(second)
skew = third / (sg ** 3)
kurt = fourth / (sg ** 4)

# Calculate Pearson skewness coefficient
med = stat.median(wavelength)
print("median", med, "A")
psn = (np.average(wavelength, weights=flambda) - med) / sg
# print(np.average(wavelength, weights=flambda) - med)
# print(sg)
print("pearson skewness", psn, "\n")

# Display statistics about the spectrum
print("first", first)
print("second", second)
print("third", third)
print("fourth", fourth, "\n")
print("sigma", sg, "A")
print("skewness", skew)
print("kurtosis", kurt)

# Adjust wavelength values to velocity values

def velshift(v):
    velocity = (v * 3e10)/4861
    # print(velocity, "cm/s")
    velocity_km = velocity/1e5
    print(velocity_km, "km/s")

print("\nv 1st moment")
velshift(first)
print("\nsigma")
velshift(sg)
print("\nskew", skew)
print("Pearson", psn)
print("kurtosis", kurt)

plt.show()
print("Done")