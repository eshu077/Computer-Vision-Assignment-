"""
Q10. Resize an image to 50% of its original width and height.

Approach:
- Compute new dimensions as half of the original width/height.
- cv2.resize(img, (new_w, new_h)) resizes using interpolation
  (default INTER_LINEAR); INTER_AREA is often preferred when shrinking.

Important functions:
- cv2.resize(src, dsize, interpolation)
"""
import cv2
from _display_helper import show

img = cv2.imread("images/input.jpg")
h, w = img.shape[:2]
resized = cv2.resize(img, (w // 2, h // 2), interpolation=cv2.INTER_AREA)

show("Q10 - Resized 50%", resized)
cv2.imwrite("outputs/q10_resized_50pct.jpg", resized)
print(f"Q10: Original {w}x{h} -> Resized {resized.shape[1]}x{resized.shape[0]}")
