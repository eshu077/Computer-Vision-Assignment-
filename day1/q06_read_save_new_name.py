"""
Q6. Read an image and save it with a different filename using OpenCV.

Approach:
- Read the image with cv2.imread(), then write it back out under a new
  filename/extension with cv2.imwrite(). OpenCV infers the output format
  (jpg/png/etc.) from the file extension you give it.

Important functions:
- cv2.imread(), cv2.imwrite()
"""
import cv2

img = cv2.imread("images/input.jpg")
new_path = "outputs/q06_saved_copy.png"
cv2.imwrite(new_path, img)
print(f"Q6: Image re-saved as '{new_path}'")
