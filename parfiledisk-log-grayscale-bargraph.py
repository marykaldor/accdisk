import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
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


# Create new image to build on
# Calculate values of radial gradient
normlistin = []
normlistout = []
rmin = (int(parvaluesf[0])/int(parvaluesf[1]))*500
rmax = (int(parvaluesf[1])/int(parvaluesf[1]))*500
im = Image.new("RGB", (1500, 1000), "black")
rgb_im = im.convert("RGB")
[xs, ys] = rgb_im.size
for x in range(1, xs):
    for y in range(1, ys):
        if rrange(x, y, xs/3, ys/2):
            normlistin.append(math.log(((cart2pol(x, y, xs/3, ys/2)[0]) ** 2), 10))

# Normalize the values of the radial gradient
maximum = max(normlistin)
for n in normlistin:
    n = n/maximum
    normlistout.append(n)


'''
# normlistout = 255 * (1.0 - normlistout)
normlistout.resize((500, 500))
img = Image.fromarray(normlistout.astype(np.uint8), mode='L')
# img = img.resize((140, 140))
img.show()
'''

# Scales the normalized list to the range of the grayscale (0-255)
tally = 0
ycoord = 101
values = []
img = Image.new("L", (1500, 1000))
draw = ImageDraw.Draw(img)
[xs, ys] = rgb_im.size
for x in range(1, xs):
    for y in range(1, ys):
        if rrange(x, y, xs/3, ys/2) and tally < len(normlistout):
            value = round(normlistout[tally]*255)
            tally += 1
            values.append(value)
        else:
            value = 255
        img.putpixel((x, y), value)

# Organizing the lists so that the indices all match up
normlistin.sort()
normlistout.sort()
values.sort()
print(normlistin[0], normlistin[-1])

# Find the quarter, half, three-quarter, and maximum values of the list in order to find marker locations for bar graph
# Calculate indices of these values to find corresponding color markers in the values list
for item in normlistin:
    if item < maximum/2:
        half = item
    if item < 3*maximum/4:
        threequarter = item

print(half, threequarter, maximum)
# qind = normlistin.index(quarter)
hind = normlistin.index(half)
tqind = normlistin.index(threequarter)
mind = normlistin.index(maximum)
print(hind, tqind, mind)
print(values[hind], values[tqind], values[mind])
half = "%.3f"%(half)
threequarter = "%.3f"%(threequarter)
maximum = "%.3f"%(maximum)

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
    '''
        if x < qind:
        xq = x
        ycoordq = 1000 - ycoord
    '''
    if x < hind:
        xh = x
        ycoordh = 1000 - ycoord
    if x < tqind:
        xtq = x
        ycoordtq = 1000 - ycoord
    if x < mind:
        xm = x
        ycoordm = 1000 - ycoord
    x += round(len(values)/height)
    ycoord += 1

draw.line([1020, 0, 1020, 1000], fill=0, width=1)
draw.line([x1 - 3, ycoordh, x2 + 3, ycoordh], fill=0, width=2)
draw.line([x1 - 3, ycoordtq, x2 + 3, ycoordtq], fill=0, width=2)
# Create font style and write labels in locations specified by pixel number
myfont = ImageFont.truetype("Times New Roman", 20)
draw.text((1195, 50), "L = log(B)", font=myfont, fill=0)
draw.text((1190, ycoordh), half, font=myfont, fill=0, anchor="ra")
draw.text((1190, ycoordtq), threequarter, font=myfont, fill=0, anchor="rm")
draw.text((1190, ycoordm), maximum, font=myfont, fill=0, anchor="rm")

# Create vertical bar graph labels
llabelimg = Image.new("L", (250, 40), "white")
llabeldraw = ImageDraw.Draw(llabelimg)
llabeldraw.text((10, 20), "L = log(B) (square pixels)", font=myfont, fill=0, anchor="lm")
lrotatedlabelimg = llabelimg.rotate(90.0, expand=1)

# Paste new vertical labels into original image
img.paste(lrotatedlabelimg, (1040, 400))

# Display and save the image
img.show()
img.save("/Users/marykaldor/accdisk/fortran/logplot-gray.png")
print("Done")

'''
Start with logarithmic scale, normalize it based off highest value, then go to 0-1 grayscale value
'''


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

# this is a change
