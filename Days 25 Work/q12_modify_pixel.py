"""
Q12. Modify the intensity/value of a selected pixel and save the
     modified image.

Approach:
- Directly assign a new [B, G, R] value to img[y, x] using NumPy
  indexing, then save the modified array with cv2.imwrite().

Important functions:
- NumPy indexing/assignment: img[y, x] = [B, G, R]
- cv2.imwrite()
"""
import cv2

img = cv2.imread("images/input.jpg")
h, w = img.shape[:2]

x, y = w // 2, h // 2
print(f"Q12: Original pixel at ({x},{y}) = {img[y, x]}")

img[y, x] = [0, 0, 255]  # set to pure red (B=0, G=0, R=255)
print(f"Q12: Modified pixel at ({x},{y}) = {img[y, x]}")

cv2.imwrite("outputs/q12_modified_pixel.jpg", img)
print("Q12: Saved -> outputs/q12_modified_pixel.jpg")
