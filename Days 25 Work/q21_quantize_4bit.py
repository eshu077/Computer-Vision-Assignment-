"""
Q21. Convert an 8-bit grayscale image into a 4-bit quantized image and
     display the result.

Approach:
- An 8-bit image has 256 (2^8) possible intensity levels (0-255).
- Quantizing to 4 bits means reducing this to only 16 (2^4) levels.
- Technique: integer-divide by the step size (256/16 = 16), then
  multiply back up, so values are rounded down to the nearest of 16
  evenly-spaced levels while staying in the 0-255 display range.

Important functions:
- NumPy integer division (//), array multiplication, astype(np.uint8)
"""
import cv2
import numpy as np
from _display_helper import show

img = cv2.imread("images/input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

levels = 16                      # 2^4
step = 256 // levels             # = 16
quantized_4bit = (gray // step) * step
quantized_4bit = quantized_4bit.astype(np.uint8)

show("Q21 - 4-bit Quantized", quantized_4bit)
cv2.imwrite("outputs/q21_quantized_4bit.jpg", quantized_4bit)
print(f"Q21: Unique intensity levels after 4-bit quantization: "
      f"{len(np.unique(quantized_4bit))} (max possible = {levels})")
