"""
Q11. Access and print the pixel value at a user-provided (x, y) coordinate.

Approach:
- Images are indexed as img[row, col] i.e. img[y, x] (NumPy uses
  row-major order, so y/height comes first).
- For a color image this returns a [B, G, R] array; for grayscale, a
  single intensity value.

Important functions:
- NumPy array indexing: img[y, x]
"""
import cv2

img = cv2.imread("images/input.jpg")
h, w = img.shape[:2]

# User-provided coordinate (hardcoded here for a non-interactive demo;
# replace with input() calls for real interactive use)
x, y = w // 2, h // 2

if 0 <= x < w and 0 <= y < h:
    pixel = img[y, x]
    print(f"Q11: Pixel at (x={x}, y={y}) = {pixel} (B, G, R)")
else:
    print("Q11: Coordinates out of range.")
