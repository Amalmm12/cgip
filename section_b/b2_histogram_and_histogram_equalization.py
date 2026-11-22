# B2. Histogram and Histogram Equalization
# Aim: Plot a grayscale histogram and display the equalized result.
# Requirements: pillow, numpy, matplotlib (no OpenCV or SciPy)
# Place image.jpg in the current working directory.

from PIL import Image, ImageOps
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("image.jpg").convert("L")
gray = np.array(img)
eq = np.array(ImageOps.equalize(img))

plt.subplot(2, 2, 1)
plt.imshow(gray, cmap="gray", vmin=0, vmax=255)
plt.title("Original")

plt.subplot(2, 2, 2)
plt.hist(gray.flatten(), bins=256, range=(0,256))
plt.title("Original Histogram")

plt.subplot(2, 2, 3)
plt.imshow(eq, cmap="gray", vmin=0, vmax=255)
plt.title("Equalized")

plt.subplot(2, 2, 4)
plt.hist(eq.flatten(), bins=256, range=(0,256))
plt.title("Equalized Histogram")

plt.tight_layout()
plt.show()
