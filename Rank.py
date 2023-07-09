import random

import cv2
import pytesseract
import os
import numpy as np

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract


class Rank:
    def __init__(self):
        self.image = None

    def show(self, name="Image"):
        cv2.imshow(name, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save(self, di=f'Ranks\im{random.randrange(0, 10000)}.jpg'):
        cv2.imwrite(di, self.image)

    import cv2
    import numpy as np

    def rem_extra_ob(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        lower_gray = np.array([0], dtype=np.uint8)
        upper_gray = np.array([20], dtype=np.uint8)
        white = np.array([255], dtype=np.uint8)
        mask = cv2.inRange(gray, lower_gray, upper_gray)
        result = cv2.bitwise_and(gray, cv2.bitwise_not(mask))
        self.image = cv2.add(result, cv2.bitwise_and(mask, white))

    def cont(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        contour_image = np.zeros_like(self.image)
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)

        cv2.imshow('Original Image', self.image)
        cv2.imshow('Contours', contour_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def place_in_rect(self):
        height, width = self.image.shape[:2]
        new_width = int(width * 3)
        new_height = int(height * 3)
        rectangle = np.full((new_height, new_width, 3), (255, 255, 255), dtype=np.uint8)
        x_offset = int((new_width - width) / 2)
        y_offset = int((new_height - height) / 2)
        rectangle[y_offset:y_offset + height, x_offset:x_offset + width] = self.image
        self.image = rectangle

    def crop_f(self):
        self.image = self.image[:95, :58]

    def crop_cent(self):
        height, width = self.image.shape[:2]

        center_x = width // 2
        center_y = height // 2

        x1 = center_x - 22
        x2 = center_x + 30
        y1 = center_y - 42
        y2 = center_y + 60

        self.image = self.image[y1:y2, x1:x2]
    def recog(self):

        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        custom_config = r'-l rus --psm 6'

        text = pytesseract.image_to_string(gray, config=custom_config)

        print(text)
        return text

    def do(self, image):
        self.image = image
        self.show()
        self.crop_f()
        self.place_in_rect()
        self.crop_cent()
        self.place_in_rect()
        self.show()
        self.recog()


if __name__ == "__main__":
    F = Rank()

    for files in os.walk(r"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\Problems"):
        for images in files[2]:
            image_load = cv2.imread(
                rf"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\Problems\{images}")
            F.do(image_load)
