# B3. Sobel Edge Detection
# Aim: Detect edges with Sobel X and Y gradient kernels.
# Requirements: pillow, numpy, matplotlib (no OpenCV or SciPy)
# Place image.jpg in the current working directory.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("image.jpg").convert("L")
a = np.array(img, dtype=float)

kx = np.array([[-1, 0, 1],
               [-2, 0, 2],
               [-1, 0, 1]])
ky = np.array([[-1, -2, -1],
               [ 0, 0, 0],
               [ 1, 2, 1]])

h, w = a.shape
output = np.zeros((h, w))
p = np.pad(a, 1, mode="edge")

for i in range(h):
    for j in range(w):
        region = p[i:i+3, j:j+3]
        gx = np.sum(region * kx)
        gy = np.sum(region * ky)
        output[i, j] = np.sqrt(gx**2 + gy**2)

plt.subplot(1, 2, 1)
plt.imshow(a, cmap="gray")
plt.title("Original")
plt.subplot(1, 2, 2)
plt.imshow(output, cmap="gray")
plt.title("Sobel")
plt.tight_layout()
plt.show()
