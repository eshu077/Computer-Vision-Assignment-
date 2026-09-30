"""
Q4. Calculate and print the total number of pixels in an image.

Approach:
- Total pixels = height * width (channels are not counted as separate
  pixels; they are values *per* pixel).
- img.size gives total number of array elements (H*W*C), so we divide by
  channel count to get pure pixel count, or compute H*W directly.

Important functions:
- ndarray.shape, ndarray.size
"""
import cv2

img = cv2.imread("images/input.jpg")
height, width, channels = img.shape

total_pixels = height * width
print(f"Q4: Total pixels (H x W) = {total_pixels}")
print(f"Q4: Total array elements (H x W x C, via img.size) = {img.size}")
