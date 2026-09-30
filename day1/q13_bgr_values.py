"""
Q13. Read a color image and print the B, G, and R values of a selected
     pixel.

Approach:
- OpenCV stores color images in BGR (not RGB) channel order by default.
- Indexing img[y, x] returns the 3 channel values in that order.

Important functions:
- NumPy indexing: img[y, x]
"""
import cv2

img = cv2.imread("images/input.jpg")
h, w = img.shape[:2]
x, y = w // 2, h // 2

b, g, r = img[y, x]
print(f"Q13: Pixel at ({x},{y}) -> B={b}, G={g}, R={r}")
