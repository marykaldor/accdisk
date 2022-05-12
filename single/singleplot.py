import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString
from matplotlib.ticker import MultipleLocator

# Reading the file
fig, ax = plt.subplots()
wavelength = []
flambda = []
selected_lines = []
filename = input("Which file would you like to use? ") + ".dat"
# Can name specific file manually if you do not want the system to prompt you
# filename = ("examplefile")
# Can use the full path if you are looking for a file outside of current directory
# f = open("/Users/marykaldor/accdisk/fortran/" + filename, "r")
f = open(filename)
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
plt.plot(wavelength, flambda, color="blue", label="SinglePlot")
plt.legend(prop={"family": "Times New Roman"})
plt.plot(x, y, "-r")

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
plt.savefig("/Users/marykaldor/accdisk/fortran/singleplot" + ".pdf")

plt.show()
print("Done")
