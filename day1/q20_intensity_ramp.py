"""
Q20. Create and display a grayscale intensity ramp whose intensity
     gradually changes from 0 to 255.

Approach:
- np.linspace(0, 255, width) creates values evenly spaced from 0 to 255
  across the image width, cast to uint8.
- np.tile repeats that 1D row down every row to form a 2D image, so the
  ramp goes from black (left) to white (right).

Important functions:
- numpy.linspace(), numpy.tile(), numpy.astype()
"""
import cv2
import numpy as np
from _display_helper import show

width, height = 256, 100
row = np.linspace(0, 255, width, dtype=np.uint8)
ramp = np.tile(row, (height, 1))

show("Q20 - Intensity Ramp (0-255)", ramp)
cv2.imwrite("outputs/q20_intensity_ramp.jpg", ramp)
print(f"Q20: Ramp created, shape={ramp.shape}, "
      f"first pixel={ramp[0,0]}, last pixel={ramp[0,-1]}")
