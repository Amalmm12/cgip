# A1. DDA Line Drawing Algorithm
# Aim: Draw a line between two points using DDA.
# Requirements: matplotlib (no OpenCV or SciPy)

import matplotlib.pyplot as plt

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dx = x2 - x1
dy = y2 - y1
steps = max(abs(dx), abs(dy))

x = x1
y = y1
if steps == 0:
    steps = 1

xinc = dx / steps
yinc = dy / steps
xp = []
yp = []

for i in range(steps + 1):
    xp.append(round(x))
    yp.append(round(y))
    x = x + xinc
    y = y + yinc

plt.plot(xp, yp, 'bo-')
plt.title("DDA Line Drawing")
plt.grid()
plt.axis("equal")
plt.show()
