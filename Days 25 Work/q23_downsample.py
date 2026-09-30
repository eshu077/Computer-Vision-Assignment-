"""
Q23. Downsample an image by a factor of 2 in both width and height and
     print the original and new resolutions.

Approach:
- Downsampling reduces the number of samples (pixels) representing the
  image. cv2.resize() with dimensions halved achieves this; INTER_AREA
  interpolation is used since it gives good results when shrinking
  (it averages pixel neighborhoods, reducing aliasing).

Important functions:
- cv2.resize(src, dsize, interpolation=cv2.INTER_AREA)
"""
import cv2

img = cv2.imread("images/input.jpg")
h, w = img.shape[:2]

factor = 2
new_w, new_h = w // factor, h // factor
downsampled = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

cv2.imwrite("outputs/q23_downsampled.jpg", downsampled)
print(f"Q23: Original resolution = {w}x{h}")
print(f"Q23: Downsampled resolution (factor {factor}) = {new_w}x{new_h}")
