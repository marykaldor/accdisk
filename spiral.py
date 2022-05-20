# Broken power law
# B1 = (R/ximin)^-q1
# B2 = A(R/ximin)^-q2
# At some xi_b they will match (R=xi_b, B1=B2)
"""
B1 = B2 = (xi_b/ximin)^-q1 = A(xi_b/ximin)^-q2
[(xi_b/ximin)^-q1]/[(xi_b/ximin)^-q2] = A
A = (xi_b/ximin)^(-q1--q2)
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import math
import timeit

start = timeit.default_timer()


parameters = ["XI1", "XI2", "PITCH", "WIDTH", "XISPIN", "XISPOUT"]
parvaluesi = []
parvaluesf = []
j = 0
k = len(parameters) - 1

f = open("/Users/marykaldor/accdisk/fortran/" + "parfile.dat", "r")
while j < k:
    for line in f:
        if line[0] == "#":
            pass
        else:
            x = line.split()
            if parameters[j] == x[1]:
                # print("The current value of ", parameters[j], " is ", x[0])
                if x[0] == "0":
                    if parameters[j] == "XISPIN":
                        xispin = xi1
                    if parameters[j] == "XISPOUT":
                        xispout = xi2
                else:
                    if parameters[j] == "XI1":
                        xi1 = x[0]
                    if parameters[j] == "XI2":
                        xi2 = x[0]
                    if parameters[j] == "XISPIN":
                        xispin = x[0]
                    if parameters[j] == "XISPOUT":
                        xispout = x[0]
                parvaluesi.append(x[0])
                if parameters[j] == parameters[-1]:
                    pass
                else:
                    j += 1

f.close()

parvaluesf.append(xispin)
parvaluesf.append(xispout)
parvaluesf.append(parvaluesi[2])
parvaluesf.append(parvaluesi[3])


def cart2pol(x, y, xcenter, ycenter):
    # Converts cartesian coordinates to polar coordinates
    # r is in units of x and y
    # theta is in radians
    xi = (np.sqrt((x - xcenter) ** 2 + (y - ycenter) ** 2))
    if x != xcenter:
        phi = np.arctan((ycenter - y) / (x - xcenter))
        if x < xcenter:
            phi += math.pi
    if x == xcenter:
        if y > ycenter:
            phi = 3*math.pi/2
        if y < ycenter:
            phi = math.pi/2
        if y == ycenter:
            phi = 0
    return xi, phi


def pol2cart(r, theta):
    # Converts polar coordinates to cartesian coordinates
    # x and y are in units of r
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y


def rrangein(x, y, xcenter, ycenter):
    # Checks if some values of x and y are within a certain radius range
    # Radius range is determined by ximin and ximax above
    if ximin < cart2pol(x, y, xcenter, ycenter)[0] < xi_b + 1:
        return True
    else:
        return False


def rrangeout(x, y, xcenter, ycenter):
    # Checks if some values of x and y are within a certain radius range
    # Radius range is determined by ximin and ximax above
    if xi_b < cart2pol(x, y, xcenter, ycenter)[0] < ximax:
        return True
    else:
        return False


# Create new image to build on
# Calculate values of radial gradient
normlistinplaw = []
normlistin = []
normlistout = []
values = []
im = Image.new("RGB", (1500, 1000), "black")
rgb_im = im.convert('RGB')
[xs, ys] = rgb_im.size
ximin = int(xispin) / 10
ximax = int(xispout) / 10
xi_b = 250

for x in range(1, xs):
    for y in range(1, ys):
        if rrangein(x, y, xs / 3, ys / 2):
            # Linear
            # normlistinplaw.append(cart2pol(x, y, xs / 3, ys / 2)[0] ** 0)
            normlistinplaw.append(cart2pol(x, y, xs / 3, ys / 2)[0] ** 2)
            # Log
            # normlistin.append(math.log((cart2pol(x, y, xs / 3, ys / 2)[0] ** 1), 10))
        if rrangeout(x, y, xs / 3, ys / 2):
            # This one has an extra factor at the beginning to make sure that the two are equal at xi_b
            # Linear
            # normlistinplaw.append(cart2pol(x, y, xs / 3, ys / 2)[0] ** 0)
            normlistinplaw.append(((xi_b ** 1) * (cart2pol(x, y, xs / 3, ys / 2)[0] ** 1)))
            # Log
            # normlistin.append(math.log((((xi_b / ximin) ** 0.5) * (cart2pol(x, y, xs / 3, ys / 2)[0] ** 0.5)), 10))


# General equation for spiral formation and location
# phi0 = 0, azimuth at xi = xi2 (location of spiral at outer radius)
# p goes from 0 to -90, pitch angle, controls how many times the spiral goes around, sign of p will switch way that
# spiral spins
# xisp = ximin
# A = contrast, of order a few (2, 3?)
# set e0 = 1 and xi = (xi/ximin) (I already do this)
# delta = angular width, fatness of the spiral
# constant = e0*xi**-q = what I already calculate


def e(constant, xi, phi, phi0, p, a, delta):
    # Convert p from degrees to radians to get properly-calculated tangent
    p = p*math.pi/180
    if p > 3*math.pi/2:
        p += math.pi
    # phi = phi*math.pi/180
    phi0 = phi0*math.pi/180
    delta = delta*math.pi/180
    # Define and calculate psi0 constant
    psi0 = phi0 + math.log(xi/ximin, 10) / math.tan(p)
    final = constant / (
            1 + (a / 2) * math.e ** (-4 * math.log(2, math.e) * ((phi - psi0) ** 2) / (delta ** 2)) + (a / 2) *
            math.e ** (-4 * math.log(2, math.e) * (((2 * math.pi) - phi + psi0) ** 2) / (delta ** 2)))
    return final


tally = 0
for x in range(1, xs):
    for y in range(1, ys):
        if rrangein(x, y, xs / 3, ys / 2):
            # normlistin.append(e(normlistinplaw[tally], cart2pol(x, y, xs / 3, ys / 2)[0], (cart2pol(x, y, xs / 3,
             # ys / 2)[1]) * 180 / math.pi, 20, 10, 3, 10))
            normlistin.append(e(normlistinplaw[tally], cart2pol(x, y, xs / 3, ys / 2)[0], (cart2pol(x, y, xs / 3,
            ys / 2)[1]), -90, float(parvaluesf[2]), 100, float(parvaluesf[3])))
            tally += 1
        if rrangeout(x, y, xs / 3, ys / 2):
            # normlistin.append(e(normlistinplaw[tally], cart2pol(x, y, xs / 3, ys / 2)[0], (cart2pol(x, y, xs / 3,
            #ys / 2)[1]) * 180 / math.pi, 20, 10, 3, 10))
            normlistin.append(e(normlistinplaw[tally], cart2pol(x, y, xs / 3, ys / 2)[0], (cart2pol(x, y, xs / 3,
            ys / 2)[1]), -90, float(parvaluesf[2]), 100, float(parvaluesf[3])))
            tally += 1
# Figure out how to have spiral apply in the same way across this border - maybe I don't even need one?


# Normalize the values of the radial gradient
maximum = max(normlistin)
for n in normlistin:
    n = n / maximum
    normlistout.append(n)

print("max normlistout", max(normlistout))
print("min normlistout", min(normlistout))

# Scales the normalized list to the range of the grayscale (0-255)
tally = 0
ycoord = 101
values = []
img = Image.new("L", (1500, 1000))
draw = ImageDraw.Draw(img)
[xs, ys] = rgb_im.size
for x in range(1, xs):
    for y in range(1, ys):
        if rrangein(x, y, xs / 3, ys / 2) and tally < len(normlistout):
            value = round(normlistout[tally] * 255)
            tally += 1
            values.append(value)
            img.putpixel((x, y), value)
        if rrangeout(x, y, xs / 3, ys / 2) and tally < len(normlistout):
            value = round(normlistout[tally] * 255)
            tally += 1
            values.append(value)
            img.putpixel((x, y), value)
        if rrangein(x, y, xs / 3, ys / 2) == False and rrangeout(x, y, xs / 3, ys / 2) == False:
            value = 255
            img.putpixel((x, y), value)

# Organizing the lists so that the indices all match up
normlistin.sort()
normlistout.sort()
values.sort()

print(min(values))
print(min(normlistin))
print(max(normlistin))

# Find the quarter, half, three-quarter, and maximum values of the list in order to find marker locations for bar graph
# Calculate indices of these values to find corresponding color markers in the values list
for item in normlistin:
    if item < maximum / 4:
        quarter = item
    if item < maximum / 2:
        half = item
    if item < 3 * maximum / 4:
        threequarter = item

# print(quarter, half, threequarter, maximum)
logq = "%.3f" % (math.log(quarter, 10))
logh = "%.3f" % (math.log(half, 10))
logtq = "%.3f" % (math.log(threequarter, 10))
logm = "%.3f" % (math.log(maximum, 10))
qind = normlistin.index(quarter)
hind = normlistin.index(half)
tqind = normlistin.index(threequarter)
mind = normlistin.index(maximum)
# print(qind, hind, tqind, mind)
# print(values[qind], values[hind], values[tqind], values[mind])
print("values", values[0], values[10], values[100], values[1000], values[10000])
quarter = "%.3f" % quarter
half = "%.3f" % half
threequarter = "%.3f" % threequarter
maximum = "%.3f" % maximum

# Draw outline of bar graph
x1 = 1200
y1 = 100
x2 = 1250
y2 = 900
draw.rectangle((x1, y1, x2, y2), outline=0)
width = x2 - x1
height = y2 - y1

# Grabbing enough values to perfectly fill the bar graph, drawing lines of those values across the bar graph outline
# Creates a linear gradient that aligns with the radial gradient plotted next to it
x = 0
while x < len(values) and ycoord < 900:
    draw.line([x1 + 1, ycoord, x2 - 1, ycoord], fill=values[x], width=1)
    if x < qind:
        xq = x
        ycoordq = 1000 - ycoord
    if x < hind:
        xh = x
        ycoordh = 1000 - ycoord
    if x < tqind:
        xtq = x
        ycoordtq = 1000 - ycoord
    if x < mind:
        xm = x
        ycoordm = 1000 - ycoord
    x += round(len(values) / height)
    ycoord += 1

# print(xq, xh, xtq, xm)
# print(ycoordq, ycoordh, ycoordtq, ycoordm)

draw.line([1020, 0, 1020, 1000], fill=0, width=1)
draw.line([x1 - 3, ycoordq, x2 + 3, ycoordq], fill=0, width=2)
draw.line([x1 - 3, ycoordh, x2 + 3, ycoordh], fill=0, width=2)
draw.line([x1 - 3, ycoordtq, x2 + 3, ycoordtq], fill=0, width=2)

# Create font style and write labels in locations specified by pixel number
myfont = ImageFont.truetype("Times New Roman", 20)
draw.text((1195, 50), "B and L", font=myfont, fill=0)
draw.text((1190, ycoordq), quarter, font=myfont, fill=0, anchor="rm")
draw.text((1190, ycoordh), half, font=myfont, fill=0, anchor="rm")
draw.text((1190, ycoordtq), threequarter, font=myfont, fill=0, anchor="rm")
draw.text((1190, ycoordm), maximum, font=myfont, fill=0, anchor="rm")
draw.text((1260, ycoordq), logq, font=myfont, fill=0, anchor="lm")
draw.text((1260, ycoordh), logh, font=myfont, fill=0, anchor="lm")
draw.text((1260, ycoordtq), logtq, font=myfont, fill=0, anchor="lm")
draw.text((1260, ycoordm), logm, font=myfont, fill=0, anchor="lm")

# Create vertical bar graph labels
blabelimg = Image.new("L", (180, 40), "white")
llabelimg = Image.new("L", (250, 40), "white")
blabeldraw = ImageDraw.Draw(blabelimg)
llabeldraw = ImageDraw.Draw(llabelimg)
blabeldraw.text((10, 20), "B (square pixels)", font=myfont, fill=0, anchor="lm")
llabeldraw.text((10, 20), "L = log(B) (square pixels)", font=myfont, fill=0, anchor="lm")
brotatedlabelimg = blabelimg.rotate(90.0, expand=1)
lrotatedlabelimg = llabelimg.rotate(90.0, expand=1)

# Paste new vertical labels into original image
img.paste(brotatedlabelimg, (1040, 400))
img.paste(lrotatedlabelimg, (1360, 350))

# Display and save the image
img.show()
img.save("/Users/marykaldor/accdisk/fortran/spiral.png")

stop = timeit.default_timer()
print('Time: ', stop - start, "s")

'''
Tinting matrix for certain RGB values
r = r + rtint
g = g + gtint
b = b + btint

Getting the RGB value of a pixel (successful)
r, g, b = rgb_im.getpixel((70, 35))
print(r, g, b)

Setting up a plot
fig, ax = plt.subplots()

Attempt to get the RGB of a certain pixel (random selection of (12, 34))
img = im.load()
print(im.size)
[xs, ys] = im.size
coordinates = x, y = 12, 34
print(im.getpixel(coordinates))

for x in range(0, xs):
    for y in range(0, ys):
        # get the RGB color of the pixel
        print(im.load([x, y]))

Example of how to make a gradient image
m = 256
img = np.zeros((m, m, 3), dtype=np.uint8)
R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
R_flat = R.flatten()
G_flat = G.flatten()
B_flat = B.flatten()

c = 0
for i in range(m):
    for j in range(m):
        for k in range(m):
            if c == len(R_flat):
                break
            R_flat[c] = i
            G_flat[c] = j
            B_flat[c] = k
            c += 1

img[:, :, 0] = R_flat.reshape((m, m))
img[:, :, 1] = G_flat.reshape((m, m))
img[:, :, 2] = B_flat.reshape((m, m))

plt.figure(figsize=(7, 7))
plt.imshow(img, cmap='gray')
plt.show()
'''
