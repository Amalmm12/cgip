# A4. 2D Object Translation
# Aim: Translate a triangle horizontally and vertically.
# Requirements: matplotlib (no OpenCV or SciPy)

import matplotlib.pyplot as plt

x = [1, 4, 2, 1]
y = [1, 1, 3, 1]
tx = int(input("Enter tx: "))
ty = int(input("Enter ty: "))
xp = []
yp = []

for i in range(len(x)):
    xp.append(x[i] + tx)
    yp.append(y[i] + ty)

plt.plot(x, y, 'bo-', label="Original")
plt.plot(xp, yp, 'ro-', label="Translated")
plt.title("2D Translation")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()
