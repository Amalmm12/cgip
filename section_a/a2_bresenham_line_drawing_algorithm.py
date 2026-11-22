# A2. Bresenham Line Drawing Algorithm
# Aim: Draw a line between any two integer-coordinate points using integer error updates.
# Requirements: matplotlib (no OpenCV or SciPy)

import matplotlib.pyplot as plt

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dx = abs(x2 - x1)
dy = abs(y2 - y1)
sx = 1 if x1 < x2 else -1
sy = 1 if y1 < y2 else -1
err = dx - dy

xp = []
yp = []
while True:
    xp.append(x1)
    yp.append(y1)
    if x1 == x2 and y1 == y2:
        break

    e = 2 * err
    if e > -dy:
        err = err - dy
        x1 = x1 + sx
    if e < dx:
        err = err + dx
        y1 = y1 + sy

plt.plot(xp, yp, 'bo-')
plt.title("Bresenham Line Drawing")
plt.grid()
plt.axis("equal")
plt.show()
