"""
Q15. Merge three separate image channels into a single color image.

Approach:
- cv2.merge([b, g, r]) stacks three single-channel images back together
  into one 3-channel BGR image, in the given order.

Important functions:
- cv2.merge(channel_list)
"""
import cv2
from _display_helper import show

img = cv2.imread("images/input.jpg")
b, g, r = cv2.split(img)

merged = cv2.merge([b, g, r])
show("Q15 - Merged Image", merged)
cv2.imwrite("outputs/q15_merged.jpg", merged)

# Sanity check: merged should be identical to the original
import numpy as np
print(f"Q15: Merged image matches original: {np.array_equal(merged, img)}")
