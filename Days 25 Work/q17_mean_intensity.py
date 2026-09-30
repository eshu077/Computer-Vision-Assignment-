"""
Q17. Calculate and print the mean intensity of a grayscale image.

Approach:
- Convert to grayscale, then compute the average pixel value with
  NumPy's .mean() or cv2.mean().

Important functions:
- ndarray.mean(), cv2.mean()
"""
import cv2

img = cv2.imread("images/input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mean_val = gray.mean()
print(f"Q17: Mean intensity = {mean_val:.2f}")
