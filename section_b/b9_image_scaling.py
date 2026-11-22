# B9. Image Scaling
# Aim: Resize an image using horizontal and vertical scale factors.
# Requirements: pillow, numpy, matplotlib (no OpenCV or SciPy)
# Place image.jpg in the current working directory.

from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("image.jpg").convert("RGB")
w, h = img.size
sx = float(input("Enter scaling x: "))
sy = float(input("Enter scaling y: "))

new_w = max(1, int(w * sx))
new_h = max(1, int(h * sy))
scaled = img.resize((new_w, new_h))

print("Original size:", img.size)
print("Scaled size:", scaled.size)

plt.subplot(1, 2, 1)
plt.imshow(img)
plt.title("Original")
plt.subplot(1, 2, 2)
plt.imshow(scaled)
plt.title("Scaled")
plt.tight_layout()
plt.show()
