# A6. 2D Object Scaling
# Aim: Change the width and height of a triangle using scaling factors.
# Requirements: matplotlib (no OpenCV or SciPy)

import matplotlib.pyplot as plt

x = [1, 4, 2, 1]
y = [1, 1, 3, 1]
sx = float(input("Enter scaling x: "))
sy = float(input("Enter scaling y: "))
xp = []
yp = []

for i in range(len(x)):
    xp.append(x[i] * sx)
    yp.append(y[i] * sy)

plt.plot(x, y, 'bo-', label="Original")
plt.plot(xp, yp, 'ro-', label="Scaled")
plt.title("2D Scaling")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()
