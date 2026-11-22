# B1. RGB, Grayscale and Binary Image
# Aim: Read and display an image in three formats.
# Requirements: pillow, numpy, matplotlib (no OpenCV or SciPy)
# Place image.jpg in the current working directory.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("image.jpg")
rgb = img.convert("RGB")
gray = np.array(img.convert("L"))
binary = np.where(gray > 127, 255, 0)

plt.subplot(1, 3, 1)
plt.imshow(rgb)
plt.title("RGB")

plt.subplot(1, 3, 2)
plt.imshow(gray, cmap="gray", vmin=0, vmax=255)
plt.title("Grayscale")

plt.subplot(1, 3, 3)
plt.imshow(binary, cmap="gray", vmin=0, vmax=255)
plt.title("Binary")

plt.tight_layout()
plt.show()
