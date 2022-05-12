import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

parameters = ["XI1", "XI2", "XISPIN", "XISPOUT"]
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


def cart2pol(x, y, xcenter, ycenter):
    # Converts cartesian coordinates to polar coordinates
    # r is in units of x and y
    # theta is in radians
    r = np.sqrt((x - xcenter) ** 2 + (y - ycenter) ** 2)
    theta = np.arctan(y / x)
    return r, theta


def pol2cart(r, theta):
    # Converts polar coordinates to cartesian coordinates
    # x and y are in units of r
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y


def rrange(x, y, xcenter, ycenter):
    # Checks if some values of x and y are within a certain radius range
    # Radius range is determined by rmin and rmax above
    if rmin < cart2pol(x, y, xcenter, ycenter)[0] < rmax:
        return True
    else:
        return False


# This plots in a relatively choppy way - the discrete values are very obvious, but it is the only way to get line 88 to
# not produce an error with decimal value inputs.
rmin = (int(parvaluesf[0])/int(parvaluesf[1]))*500
rmax = (int(parvaluesf[1])/int(parvaluesf[1]))*500
print("rmin", rmin, "rmax", rmax)
im = Image.new("RGB", (1000, 1000), "black")
rgb_im = im.convert("RGB")
[xs, ys] = rgb_im.size
for x in range(1, xs):
    for y in range(1, ys):
        if rrange(x, y, xs/2, ys/2):
            # r = g = b = round(0.001*((cart2pol(x, y, xs / 2, ys / 2)[0]) ** 2))
            r = g = b = 15*math.trunc(math.log(((cart2pol(x, y, xs/2, ys/2)[0]) ** 2), 10))
        else:
            r = g = b = 400
        value = (r, g, b)
        rgb_im.putpixel((x, y), value)

rgb_im.show()
rgb_im.save("/Users/marykaldor/accdisk/fortran/logplot-rgb.png")


'''
r = 0.5
# np.arange(0, rmax, 0.1*rmax)
theta = np.arange(0, (2 * np.pi), 0.01)
print(theta)

for i in theta:
    plt.polar(i, r, "g")

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rmax(2)
# ax.set_rticks([0.5, 1, 1.5, 2])  # Fewer radial ticks
# ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
# ax.grid(True)

# ax.set_title("A line plot on a polar axis", va='bottom')
plt.show()
'''

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
