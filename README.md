# Computer Graphics and Image Processing — Python Lab

16 lab experiments from the practical syllabus. Beginner-friendly programs, organized by section.

**No OpenCV or SciPy required.**

## Setup

Install Python 3 and the dependencies:

```bash
python -m pip install -r requirements.txt
```

Run a program from the repository root, for example:

```bash
python section_a/a1_dda_line_drawing_algorithm.py
python section_b/b3_sobel_edge_detection.py
```

For all Section B programs, place an image named `image.jpg` in the working directory (the repository root if running the above commands). Use a small image for the manually implemented Sobel, Prewitt and Laplacian filters.

## Section A — Computer Graphics

1. [DDA Line Drawing Algorithm](section_a/a1_dda_line_drawing_algorithm.py)
2. [Bresenham's Line Drawing Algorithm](section_a/a2_bresenham_line_drawing_algorithm.py)
3. [Midpoint Circle Drawing Algorithm](section_a/a3_midpoint_circle_drawing_algorithm.py)
4. [2D Object Translation](section_a/a4_2d_object_translation.py)
5. [2D Object Rotation](section_a/a5_2d_object_rotation.py)
6. [2D Object Scaling](section_a/a6_2d_object_scaling.py)
7. [Cohen–Sutherland Line Clipping Algorithm](section_a/a7_cohen_sutherland_line_clipping.py)

## Section B — Image Processing

1. [Read and display image in RGB, grayscale and binary](section_b/b1_rgb_grayscale_and_binary_image.py)
2. [Histogram and histogram equalization](section_b/b2_histogram_and_histogram_equalization.py)
3. [Sobel edge detection](section_b/b3_sobel_edge_detection.py)
4. [Prewitt edge detection](section_b/b4_prewitt_edge_detection.py)
5. [Gradient and Laplacian filtering / edge sharpening](section_b/b5_gradient_and_laplacian_filtering.py)
6. [Global and intensity-based thresholding with histogram](section_b/b6_global_and_intensity_thresholding.py)
7. [Image translation](section_b/b7_image_translation.py)
8. [Image rotation](section_b/b8_image_rotation.py)
9. [Image scaling](section_b/b9_image_scaling.py)

## Notes

- The programs are adapted from the 16-experiment PDF lab manual discussed in ChatGPT.
- The input image is not included; supply your own `image.jpg`.
- Each script is designed to be run independently.
- Bresenham implementation handles lines in all directions.
- Most image operations use Pillow and NumPy, without OpenCV or SciPy.
