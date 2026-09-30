"""
Q14. Split a color image into its B, G, and R channels and display each
     channel.

Approach:
- cv2.split() separates a multi-channel image into a list of
  single-channel images. Each channel displayed alone appears grayscale
  (since it's a single intensity value), not tinted, unless you merge it
  back with zeroed-out other channels.

Important functions:
- cv2.split(img)
"""
import cv2
from _display_helper import show

img = cv2.imread("images/input.jpg")
b, g, r = cv2.split(img)

show("Q14 - Blue Channel", b)
show("Q14 - Green Channel", g)
show("Q14 - Red Channel", r)

cv2.imwrite("outputs/q14_blue_channel.jpg", b)
cv2.imwrite("outputs/q14_green_channel.jpg", g)
cv2.imwrite("outputs/q14_red_channel.jpg", r)
print("Q14: Done. Saved b/g/r channel images to outputs/")
