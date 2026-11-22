# B5. Gradient and Laplacian Filtering
# Aim: Enhance edges using gradient and Laplacian operators.
# Requirements: pillow, numpy, matplotlib (no OpenCV or SciPy)
# Place image.jpg in the current working directory.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("image.jpg").convert("L")
a = np.array(img, dtype=float)

def apply_kernel(a, k):
    h, w = a.shape
    output = np.zeros((h, w))
    p = np.pad(a, 1, mode="edge")
    for i in range(h):
        for j in range(w):
            region = p[i:i+3, j:j+3]
            output[i, j] = np.sum(region * k)
    return output

kx = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
ky = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
g = np.sqrt(apply_kernel(a,kx)**2 +
            apply_kernel(a,ky)**2)

kl = np.array([[0,1,0],[1,-4,1],[0,1,0]])
lap = apply_kernel(a, kl)
sharp_g = np.clip(a + 0.2*g, 0, 255)
sharp_l = np.clip(a - lap, 0, 255)

images = [a, g, sharp_g, abs(lap), sharp_l]
titles = ["Original", "Gradient", "Gradient Sharp",
           "Laplacian", "Laplacian Sharp"]
for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")
plt.tight_layout()
plt.show()
