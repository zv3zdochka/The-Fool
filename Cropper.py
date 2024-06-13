import random
import time
import uuid
import cv2
import numpy as np
import mss
import os


class Crop:
    def __init__(self):
        self.deck = []
        self.table = []
        self.hand = []
        self.data = 0
        self.regions = [
            (0, 520, 1920, 390),  # hand
            (0, 100, 200, 450),  # deck
            (160, 250, 1900, 280)  # table
        ]
        self.all = []

    def take_screenshot(self):
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)
            img = np.array(screenshot)
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        self.data = img

    def crop_image(self):
        for region in self.regions:
            x, y, w, h = region
            self.all.append(self.data[y:y + h, x:x + w])

    def show(self):
        for i, img in enumerate(self.all):
            cv2.imshow(f'Image {i + 1}', img)
            cv2.waitKey(10000)  # 1 sec
        cv2.destroyAllWindows()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save_images(self, folder="go"):
        if not os.path.exists(folder):
            os.makedirs(folder)
        print(len(self.all))
        for img in self.all:
            unique_filename = str(uuid.uuid4()) + ".png"
            filepath = os.path.join(folder, unique_filename)
            cv2.imwrite(filepath, img)
            print(f"Saved image to {filepath}")


    def run(self):
        self.take_screenshot()
        self.crop_image()
        self.save_images()


if __name__ == "__main__":
    time.sleep(3)
    r = Crop()
    r.run()
