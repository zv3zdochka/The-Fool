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
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        _, binary_image = cv2.threshold(gray_image, 1, 255, cv2.THRESH_BINARY)
        black_pixels_mask = np.where(binary_image == 0)

        self.image[black_pixels_mask] = (255, 255, 255)

        cv2.imwrite("result_image.png", self.image)




    def place_in_rect(self):
        height, width = self.image.shape[:2]
        new_width = int(width * 3)
        new_height = int(height * 3)
        rectangle = np.full((new_height, new_width, 3), (255, 255, 255), dtype=np.uint8)
        x_offset = int((new_width - width) / 2)
        y_offset = int((new_height - height) / 2)
        rectangle[y_offset:y_offset + height, x_offset:x_offset + width] = self.image
        self.image = rectangle

    def crop(self):
        self.image = self.image[:120, :80]

    def recog(self, image):
        self.image = image
        self.show()
        self.crop()
        self.show()
        self.place_in_rect()
        self.show()
        self.rem_extra_ob()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        custom_config = r'-l rus --psm 6'

        text = pytesseract.image_to_string(gray, config=custom_config)

        print(text)
        return text


if __name__ == "__main__":
    F = Rank()

    for files in os.walk(r"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\Problems"):
        for images in files[2]:
            image_load = cv2.imread(
                rf"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\Problems\{images}")
            F.recog(image_load)
