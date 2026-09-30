"""
Q19. Create a 256 x 256 grayscale image in which every pixel has
     intensity value 128.

Approach:
- np.full((H, W), value, dtype=np.uint8) creates an array of the given
  shape filled entirely with one value - here mid-gray (128).

Important functions:
- numpy.full(shape, fill_value, dtype)
"""
import cv2
import numpy as np
from _display_helper import show

flat_img = np.full((256, 256), 128, dtype=np.uint8)

show("Q19 - Flat Gray (128)", flat_img)
cv2.imwrite("outputs/q19_flat_gray_128.jpg", flat_img)
print(f"Q19: Created {flat_img.shape} image, unique values = "
      f"{np.unique(flat_img)}")
