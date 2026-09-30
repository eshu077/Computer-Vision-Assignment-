"""
Q5. Print the data type (dtype) of the image matrix.

Approach:
- OpenCV loads standard images as 8-bit unsigned integers (uint8) per
  channel by default, i.e. values from 0-255.

Important functions:
- ndarray.dtype
"""
import cv2

img = cv2.imread("images/input.jpg")
print(f"Q5: Image dtype = {img.dtype}")
