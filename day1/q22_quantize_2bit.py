"""
Q22. Convert an 8-bit grayscale image into a 2-bit quantized image and
     display the result.

Approach:
- Same idea as Q21, but with only 4 (2^2) levels instead of 16.
- step = 256 / 4 = 64, so pixels are grouped into 4 bins: ~0, ~64, ~128,
  ~192.

Important functions:
- NumPy integer division (//), array multiplication, astype(np.uint8)
"""
import cv2
import numpy as np
from _display_helper import show

img = cv2.imread("images/input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

levels = 4                       # 2^2
step = 256 // levels             # = 64
quantized_2bit = (gray // step) * step
quantized_2bit = quantized_2bit.astype(np.uint8)

show("Q22 - 2-bit Quantized", quantized_2bit)
cv2.imwrite("outputs/q22_quantized_2bit.jpg", quantized_2bit)
print(f"Q22: Unique intensity levels after 2-bit quantization: "
      f"{len(np.unique(quantized_2bit))} (max possible = {levels})")
