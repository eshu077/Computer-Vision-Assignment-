"""
Q18. Calculate and print the mean and standard deviation of a grayscale
     image using NumPy/OpenCV.

Approach:
- cv2.meanStdDev() returns both statistics in one call, computed over
  each channel (here, just one channel since the image is grayscale).

Important functions:
- cv2.meanStdDev(src)
"""
import cv2

img = cv2.imread("images/input.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mean, std = cv2.meanStdDev(gray)
print(f"Q18: Mean = {mean[0][0]:.2f}, Std Dev = {std[0][0]:.2f}")
print(f"Q18 (NumPy check): mean={gray.mean():.2f}, std={gray.std():.2f}")
