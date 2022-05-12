import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def cart2pol(x, y, xcenter, ycenter):
    # Converts cartesian coordinates to polar coordinates
    # r is in units of x and y
    # theta is in radians
    r = np.sqrt((x-xcenter) ** 2 + (y-ycenter) ** 2)
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



im = Image.open("/Users/marykaldor/accdisk/fortran/whitesquare.png")
rgb_im = im.convert('RGB')
[xs, ys] = rgb_im.size
rmin = 10
rmax = 500
for x in range(1, xs):
    for y in range(1, ys):
        if rrange(x, y, xs/2, ys/2):
            r = g = b = round(0.001*cart2pol(x, y, xs/2, ys/2)[0]**2)
        else:
            r = g = b = 400
        value = (r, g, b)
        rgb_im.putpixel((x, y), value)

rgb_im.show()

rgb_im.save("/Users/marykaldor/accdisk/fortran/powerlawgradientdisk.png")

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
