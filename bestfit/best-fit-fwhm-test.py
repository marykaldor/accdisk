import os
import random
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from numpy import random
from shapely.geometry import LineString
from matplotlib.ticker import MultipleLocator
import math
import statistics
from scipy.optimize import curve_fit
global wll
global wlh

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

parameters = ["OUTFILE", "ANGI", "XI1", "XI2", "Q"]
z = 0
d = 1
adjust2 = " "
outfile = " "

# Go through text and only change given parameter's value
# Everything else just gets rewritten to the new file
while d < 11:
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
                    # print("angi")
                    '''
                    print("angiout", angiout)
                    sigma = angiout / 20
                    angiout = np.random.normal(angiout, sigma)
                    print("angiout", angiout)
                    '''
                    adjust2 = str(angiout)
                if parameters[z] == "XI1":
                    # print("xi1")
                    '''
                    print("xi1out", xi1out)
                    sigma = xi1out / 20
                    xi1out = np.random.normal(xi1out, sigma)
                    print("xi1out", xi1out)
                    '''
                    adjust2 = str(xi1out)
                if parameters[z] == "XI2":
                    # print("xi2")
                    '''
                    print("xi2out", xi2out)
                    sigma = xi2out / 20
                    xi2out = np.random.normal(xi2out, sigma)
                    print("xi2out", xi2out)
                    '''
                    adjust2 = str(xi2out)
                if parameters[z] == "Q":
                    # print("q")
                    '''
                    print("qout", qout)
                    sigma = qout / 20
                    qout = np.random.normal(qout, sigma)
                    print("qout", qout)
                    '''
                    adjust2 = str(qout)
                if parameters[z] == "OUTFILE":
                    # print("outfile")
                    adjust2 = ("island_" + str(d))
                    outfile = adjust2
                    # print("outfile", outfile)
                # print(adjust2)
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

while i < 1:
    wavelength = []
    flambda = []
    noise = []
    ratio = []
    originalplot = []
    cont = 1
    sqrtcont = math.sqrt(cont)
    SN_cont = 20
    sigmacont = 1 / SN_cont
    selected_lines = []
    filename = ("island_" + str(k))
    f = open("/Users/marykaldor/accdisk/fortran/" + filename, "r")
    lines = f.readlines()

    # Gets rid of pound symbol lines
    # Calculates scaled flux, noise, ratio, and saves them all to their respective lists
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
            op = fluxnew - cont
            n = fluxnew - y - cont
            r = fluxnew / flux
            wavelength.append(x)
            flambda.append(fluxnew)
            noise.append(n)
            ratio.append(r)
            originalplot.append(op)
            selected_lines.append(line)

    # Plots spectrum along with half maximum horizontal line
    # maximum = max(flambda)
    # maximum = 1
    # a = [4400, 5400]
    # y = [maximum/2, maximum/2]
    plt.plot(wavelength, flambda, color=next(colorchoice), label="BestFit_" + str(k))
    plt.legend(prop={"family": "Times New Roman"})
    # plt.plot(x, y, "-0")

    # Setting up the parabola fit of the top of the model
    # Selects middle 60 A around expected peak, fits parabola to those data points, displays equation of curve
    wavelengthpeak = []
    flambdapeak = []
    cycle1 = 0
    while cycle1 < len(wavelength):
        # This selects 4770-4830
        if 128 < cycle1 < 198:
            wavelengthpeak.append(wavelength[cycle1])
        cycle1 += 1
    cycle2 = 0
    while cycle2 < len(originalplot):
        if 128 < cycle2 < 198:
            flambdapeak.append(originalplot[cycle2])
        cycle2 += 1
    parabolafit = np.polyfit(wavelengthpeak, flambdapeak, deg=2)
    # parabolafit = np.polynomial.polynomial.Polynomial.fit(wavelengthpeak, flambdapeak, deg=4)
    # coeff = parabolafit.convert().coef
    # print(parabolafit[0], "x^2+", parabolafit[1], "x+", parabolafit[2])

    # Uses coefficients of parabola fit, creates curve, finds maximum and half maximum without continuum,
    # adds continuum in after to hit the proper scaling with respect to the continuum-added model.
    standarddev = statistics.stdev(flambdapeak)
    # wavelengthpeak = np.array(wavelengthpeak)
    # flambdapeak = np.array(flambdapeak)

    # wavelengthpeak = LineString(np.column_stack((a, c)))
    # flambdapeak = LineString(np.column_stack((wavelength, flambda)))

    def gauss(m, x0, s):
        return np.exp(-(m - x0) ** 2 / (2 * s ** 2))

    # print("gauss", gauss(flambdapeak), max(flambdapeak), standarddev)

    '''
    print("gauss", gauss(1, 2, standarddev), max(flambdapeak), standarddev)
    parameters1, covariance1 = curve_fit(gauss, wavelengthpeak, flambdapeak)
    print(parameters1, covariance1)
    perr = np.sqrt(np.diag(covariance1))
    print("perr", perr)
    '''

    topfit = scipy.signal.savgol_filter(flambdapeak, 29, 4)
    topfit = topfit + 1
    print("topfit", topfit)
    print(wavelengthpeak)
    roughfit = plt.plot(wavelengthpeak, topfit, color="black")
    roughfitmax = max(topfit)
    print(type(roughfitmax))
    print("roughmax", roughfitmax)
    halfmax = roughfitmax/2
    plt.show()

    '''
    ran = np.linspace(4770, 4830, num=60)
    fx = []
    for q in range(len(ran)):
        # fx.append(gauss[0] * ran[q] ** 2 + gauss[1] * ran[q] + gauss[2])
        fx.append(parabolafit[0] * ran[q] ** 2 + parabolafit[1] * ran[q] + parabolafit[2])
        # fx.append(coeff[4]*ran[q]**4+coeff[3]*ran[q]**3+coeff[2]*ran[q]**2+coeff[1]*ran[q]+coeff[0])
    # plt.plot(ran, fx, "-y")
    maximum = max(fx)
    halfmax = maximum / 2
    '''

    a = [4400, 5400]
    b = [halfmax, halfmax]
    c = [halfmax + 1, halfmax + 1]
    # plt.plot(a, b, "-0")
    plt.plot(a, c, "-g")
    plt.show()
    # plt.plot(wavelengthpeak, parabolafit)

    # Find the intersection between spectrum and half max line, finds the params coordinates of those locations,
    # then takes the difference of those to find the FWHM. LineString allows for interpolation between points so that
    # we can find an exact intersection because sometimes there is no params value for an exact y = 0.5 value.
    line1 = LineString(np.column_stack((a, c)))
    line2 = LineString(np.column_stack((wavelength, flambda)))
    intersection = line1.intersection(line2)
    lowint = intersection[0].x
    highint = intersection[-1].x
    print(lowint)
    print(highint)


    def wllsearch():
        global wll
        wll = 0
        for w in wavelength:
            if w >= lowint:
                wll = w
                return wll


    def wlhsearch():
        global wlh
        wlh = 0
        for h in wavelength:
            if h >= highint:
                wlh = h
                return wlh


    print(wllsearch())
    wllind = wavelength.index(wll)
    print(wlhsearch())
    wlhind = wavelength.index(wlh)

    # Selects area around rough intersection, linearizes the model with the surrounding 20 points, finds intersection
    # with FWHM line, takes difference of points to find FWHM.
    it1 = 0
    lowlin1 = []
    lowlin2 = []
    while it1 < len(wavelength):
        if wllind - 10 < it1 < wllind + 10:
            lowlin1.append(wavelength[it1])
            lowlin2.append(flambda[it1])
        it1 += 1
    # print(lowlin1)
    # print(lowlin2)
    it2 = 0
    highlin1 = []
    highlin2 = []
    while it2 < len(wavelength):
        if wlhind - 10 < it2 < wlhind + 10:
            highlin1.append(wavelength[it2])
            highlin2.append(flambda[it2])
        it2 += 1
    # print(highlin1)
    # print(highlin2)
    linearfit1 = np.polyfit(lowlin1, lowlin2, deg=1)
    linearfit2 = np.polyfit(highlin1, highlin2, deg=1)
    # print("LF1", linearfit1)
    # print("LF2", linearfit2)

    fwhmlow = ((halfmax + 1) - linearfit1[1]) / linearfit1[0]
    # print(fwhmlow)
    fwhmhigh = ((halfmax + 1) - linearfit2[1]) / linearfit2[0]
    # print(fwhmhigh)
    fwhm = fwhmhigh - fwhmlow
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
    plt.savefig("/Users/marykaldor/accdisk/fortran/best-fit_" + str(k) + ".pdf")
    i += 1
    k += 1

# plt.text(6700, 0.8, "Test Label", fontanel="Times New Roman")
# plt.text(6375, 0.3, "Test Label", fontname="Times New Roman")
plt.show()
print("Done")
