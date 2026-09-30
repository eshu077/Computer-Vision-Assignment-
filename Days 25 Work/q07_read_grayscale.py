"""
Q7. Read an image directly in grayscale mode and display it.

Approach:
- cv2.imread() accepts a flag as the second argument. Passing
  cv2.IMREAD_GRAYSCALE (or 0) tells OpenCV to convert the image to a
  single-channel grayscale image while reading it from disk, which is
  faster than reading color and converting afterwards.

Important functions:
- cv2.imread(path, cv2.IMREAD_GRAYSCALE)
"""
import cv2
from _display_helper import show

gray = cv2.imread("images/input.jpg", cv2.IMREAD_GRAYSCALE)

show("Q7 - Grayscale (read directly)", gray)
cv2.imwrite("outputs/q07_grayscale_direct.jpg", gray)
print(f"Q7: Done. Shape = {gray.shape} (no channel dim = grayscale)")
