# B7. Image Translation
# Aim: Translate an actual image horizontally and vertically.
# Requirements: pillow, numpy, matplotlib (no OpenCV or SciPy)
# Place image.jpg in the current working directory.

from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("image.jpg").convert("RGB")
w, h = img.size
tx = int(input("Enter tx: "))
ty = int(input("Enter ty: "))

translated = img.transform(
    (w, h),
    Image.Transform.AFFINE,
    (1, 0, -tx, 0, 1, -ty)
)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original")
plt.subplot(1, 2, 2)
plt.imshow(translated)
plt.title("Translated")
plt.tight_layout()
plt.show()
