# B8. Image Rotation
# Aim: Rotate an image about its centre by a selected angle.
# Requirements: pillow, numpy, matplotlib (no OpenCV or SciPy)
# Place image.jpg in the current working directory.

from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("image.jpg").convert("RGB")
angle = float(input("Enter angle: "))
rotated = img.rotate(angle, expand=True)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original")
plt.subplot(1, 2, 2)
plt.imshow(rotated)
plt.title("Rotated")
plt.tight_layout()
plt.show()
