"""
Q2. Check whether an image was loaded successfully. If loading fails,
    print a meaningful error message.

Approach:
- cv2.imread() returns None (not an exception) when the file is missing
  or unreadable, so we must explicitly check "img is None".

Important functions:
- cv2.imread(path): returns a NumPy array on success, None on failure.
"""
import cv2

path = "images/input.jpg"
img = cv2.imread(path)

if img is None:
    print(f"Q2 ERROR: Could not load image at '{path}'. "
          f"Check that the file exists and the path/extension is correct.")
else:
    print(f"Q2: Image '{path}' loaded successfully. Shape: {img.shape}")

# Demonstrate the failure case too
bad = cv2.imread("images/does_not_exist.jpg")
if bad is None:
    print("Q2 (demo of failure case): 'images/does_not_exist.jpg' "
          "failed to load, as expected.")
