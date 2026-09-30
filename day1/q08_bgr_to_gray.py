"""
Q8. Convert a color image to grayscale using cv2.cvtColor().

Approach:
- Read the image normally (color, BGR order).
- Use cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) to convert it, which applies
  a weighted sum of the B, G, R channels (perceptual luminance weights)
  to produce a single grayscale channel.

Important functions:
- cv2.cvtColor(src, code)
"""
import cv2
from _display_helper import show

img = cv2.imread("images/input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

show("Q8 - Converted to Grayscale", gray)
cv2.imwrite("outputs/q08_grayscale_converted.jpg", gray)
print(f"Q8: Done. Original shape {img.shape} -> Gray shape {gray.shape}")
