# B6. Global and Intensity Thresholding
# Aim: Apply three global thresholds, a selectable intensity band, and plot a histogram.
# Requirements: pillow, numpy, matplotlib (no OpenCV or SciPy)
# Place image.jpg in the current working directory.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("image.jpg").convert("L")
a = np.array(img)
t1 = np.where(a > 50, 255, 0)
t2 = np.where(a > 127, 255, 0)
t3 = np.where(a > 200, 255, 0)

low = int(input("Enter lower intensity: "))
high = int(input("Enter upper intensity: "))
t4 = np.where((a >= low) & (a <= high), 255, 0)

images = [a, t1, t2, t3, t4]
titles = ["Original", "Threshold 50", "Threshold 127",
           "Threshold 200", "Intensity Range"]
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap="gray", vmin=0, vmax=255)
    plt.title(titles[i])
    plt.axis("off")
plt.subplot(2, 3, 6)
plt.hist(a.flatten(), 256, (0, 256))
plt.title("Histogram")
plt.tight_layout()
plt.show()
