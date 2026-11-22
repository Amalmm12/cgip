# A5. 2D Object Rotation
# Aim: Rotate a triangle about the origin by a user-specified angle.
# Requirements: matplotlib (no OpenCV or SciPy)

import matplotlib.pyplot as plt
import math

x = [1, 4, 2, 1]
y = [1, 1, 3, 1]
angle = float(input("Enter rotation angle: "))
t = math.radians(angle)
xp = []
yp = []

for i in range(len(x)):
    xp.append(x[i]*math.cos(t) - y[i]*math.sin(t))
    yp.append(x[i]*math.sin(t) + y[i]*math.cos(t))

plt.plot(x, y, 'bo-', label="Original")
plt.plot(xp, yp, 'ro-', label="Rotated")
plt.title("2D Rotation")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()
