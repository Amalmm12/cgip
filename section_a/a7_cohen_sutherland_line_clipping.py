# A7. Cohen-Sutherland Line Clipping
# Aim: Clip an arbitrary line against a rectangular viewing window.
# Requirements: matplotlib (no OpenCV or SciPy)

import matplotlib.pyplot as plt

xmin, ymin = 2, 2
xmax, ymax = 8, 6

def code(x, y):
    c = 0
    if x < xmin:
        c = c | 1
    elif x > xmax:
        c = c | 2
    if y < ymin:
        c = c | 4
    elif y > ymax:
        c = c | 8
    return c

def clip(x1, y1, x2, y2):
    while True:
        c1 = code(x1, y1)
        c2 = code(x2, y2)
        if (c1 | c2) == 0:
            return x1, y1, x2, y2
        if (c1 & c2) != 0:
            return None
        c = c1 if c1 != 0 else c2
        if c & 8:
            x = x1+(x2-x1)*(ymax-y1)/(y2-y1)
            y = ymax
        elif c & 4:
            x = x1+(x2-x1)*(ymin-y1)/(y2-y1)
            y = ymin
        elif c & 2:
            y = y1+(y2-y1)*(xmax-x1)/(x2-x1)
            x = xmax
        else:
            y = y1+(y2-y1)*(xmin-x1)/(x2-x1)
            x = xmin
        if c == c1:
            x1, y1 = x, y
        else:
            x2, y2 = x, y

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

plt.plot([xmin,xmax,xmax,xmin,xmin],
         [ymin,ymin,ymax,ymax,ymin], 'k-')
plt.plot([x1,x2], [y1,y2], 'r--', label="Original")
result = clip(x1, y1, x2, y2)
if result is not None:
    a, b, c, d = result
    plt.plot([a,c], [b,d], 'g-', label="Clipped")
else:
    print("Line rejected")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()
