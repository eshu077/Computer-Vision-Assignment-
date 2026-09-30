"""
Q25. Rotate an image by 90 degrees, display it, and save the rotated
     image.

Approach:
- cv2.rotate() with cv2.ROTATE_90_CLOCKWISE performs a fast, exact 90
  degree rotation (no interpolation needed, since it's just a
  transpose + flip under the hood, unlike arbitrary-angle rotation).

Important functions:
- cv2.rotate(src, rotateCode)
"""
import cv2
from _display_helper import show

img = cv2.imread("images/input.jpg")
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

show("Q25 - Rotated 90 degrees", rotated)
cv2.imwrite("outputs/q25_rotated_90.jpg", rotated)
print(f"Q25: Original shape {img.shape} -> Rotated shape {rotated.shape}")
