"""
Q1. Read an image using OpenCV and display it.

Approach:
- cv2.imread() loads the image from disk into a NumPy array (BGR order).
- cv2.imshow() opens a window to display it; cv2.waitKey(0) waits for a
  keypress, and cv2.destroyAllWindows() closes the window.

Important functions:
- cv2.imread(path): reads an image file into a NumPy array.
- cv2.imshow(name, img): displays the image in a window.
- cv2.waitKey(ms): pauses until a key is pressed (0 = wait forever).
"""
import cv2
from _display_helper import show

img = cv2.imread("images/input.jpg")

show("Q1 - Original Image", img)
cv2.imwrite("outputs/q01_display.jpg", img)
print("Q1: Done. Output -> outputs/q01_display.jpg")
