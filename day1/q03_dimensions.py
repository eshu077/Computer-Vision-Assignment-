"""
Q3. Print the image height, width, and number of channels.

Approach:
- A color image loaded by OpenCV is a NumPy array of shape (H, W, C).
- img.shape gives (height, width, channels) directly.

Important functions:
- ndarray.shape: tuple describing array dimensions.
"""
import cv2

img = cv2.imread("images/input.jpg")

height, width, channels = img.shape
print(f"Q3: Height = {height}px, Width = {width}px, Channels = {channels}")
