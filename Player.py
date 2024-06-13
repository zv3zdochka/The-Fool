import numpy as np
import cv2
import mss


class Player:
    def __init__(self):
        pass

    def capture_screen(self):
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)
            image = np.array(screenshot)
            cv2.imshow(image)
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

            return image

P = Player()
P.capture_screen()
