# A3. Midpoint Circle Drawing Algorithm
# Aim: Draw a circle from a user-specified centre and radius using eight-way symmetry.
# Requirements: matplotlib (no OpenCV or SciPy)

import matplotlib.pyplot as plt

xc = int(input("Enter centre x: "))
yc = int(input("Enter centre y: "))
r = int(input("Enter radius: "))

x = 0
y = r
p = 1 - r
xp = []
yp = []

while x <= y:
    xp.extend([xc+x, xc-x, xc+x, xc-x,
               xc+y, xc-y, xc+y, xc-y])
    yp.extend([yc+y, yc+y, yc-y, yc-y,
               yc+x, yc+x, yc-x, yc-x])

    x = x + 1
    if p < 0:
        p = p + 2*x + 1
    else:
        y = y - 1
        p = p + 2*x - 2*y + 1

plt.plot(xp, yp, 'bo')
plt.title("Midpoint Circle")
plt.grid()
plt.axis("equal")
plt.show()
