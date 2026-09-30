"""
Q16. Calculate and print the minimum and maximum intensity values of a
     grayscale image.

Approach:
- Convert to grayscale, then use NumPy's .min()/.max() (or
  cv2.minMaxLoc()) to find the darkest and brightest pixel values.

Important functions:
- ndarray.min(), ndarray.max(), cv2.minMaxLoc()
"""
import cv2

img = cv2.imread("images/input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
print(f"Q16: Min intensity = {min_val} at {min_loc}, "
      f"Max intensity = {max_val} at {max_loc}")
print(f"Q16 (NumPy check): min={gray.min()}, max={gray.max()}")
