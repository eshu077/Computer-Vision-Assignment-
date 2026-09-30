"""
Q9. Display an image using Matplotlib and hide the axis.

Approach:
- OpenCV loads images in BGR order, but Matplotlib expects RGB, so we
  convert with cv2.cvtColor(..., cv2.COLOR_BGR2RGB) before plotting.
- plt.axis('off') hides the x/y tick marks and axis lines.

Important functions:
- cv2.cvtColor(), plt.imshow(), plt.axis('off')
"""
import cv2
import matplotlib
matplotlib.use("Agg")  # headless-safe backend; use default backend for GUI display
import matplotlib.pyplot as plt

img = cv2.imread("images/input.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img_rgb)
plt.axis("off")
plt.title("Q9 - Image without axis")
plt.savefig("outputs/q09_matplotlib_no_axis.png", bbox_inches="tight")
plt.show()
print("Q9: Done. Output -> outputs/q09_matplotlib_no_axis.png")
