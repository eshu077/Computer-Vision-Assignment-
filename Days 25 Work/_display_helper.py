"""
Shared helper used by every script in this folder.

show(): displays an image in a window with cv2.imshow() when a display is
available (i.e. when you run this on your own PC). On a headless machine
(no monitor / SSH / CI server), it safely skips imshow so the script keeps
running instead of crashing, and the image is still saved with cv2.imwrite
in each script.
"""
import os
import cv2

def show(window_name, img):
    if os.environ.get("DISPLAY") or os.name == "nt":
        try:
            cv2.imshow(window_name, img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return
        except cv2.error:
            pass
    print(f"[no display detected - skipping cv2.imshow for '{window_name}']")
