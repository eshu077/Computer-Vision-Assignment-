"""
Q24. Crop a rectangular Region of Interest (ROI) from an image using
     user-provided coordinates.

Approach:
- NumPy slicing extracts a sub-array directly: img[y1:y2, x1:x2] selects
  rows y1..y2 and columns x1..x2, which is a rectangular crop. No
  special OpenCV function is needed - it's plain array slicing.

Important functions:
- NumPy slicing: img[y1:y2, x1:x2]
"""
import cv2
from _display_helper import show

img = cv2.imread("images/input.jpg")
h, w = img.shape[:2]

# User-provided ROI coordinates (hardcoded for a non-interactive demo)
x1, y1, x2, y2 = w // 4, h // 4, 3 * w // 4, 3 * h // 4

roi = img[y1:y2, x1:x2]

show("Q24 - Cropped ROI", roi)
cv2.imwrite("outputs/q24_cropped_roi.jpg", roi)
print(f"Q24: Cropped ROI from ({x1},{y1}) to ({x2},{y2}) "
      f"-> shape {roi.shape}")
