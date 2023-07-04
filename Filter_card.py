import cv2
import numpy as np
import os


class Filter:
    def __init__(self):
        self.image = None

    def remove_extra_colors(self):
        lower_gray = np.array([100, 100, 100], dtype=np.uint8)
        upper_gray = np.array([190, 190, 190], dtype=np.uint8)

        mask = cv2.inRange(self.image, lower_gray, upper_gray)

        black_color = np.array([0, 0, 0], dtype=np.uint8)
        self.image[mask != 0] = black_color

    def cut_back(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        largest_contour = max(contours, key=cv2.contourArea)

        mask = np.zeros_like(self.image)

        cv2.drawContours(mask, [largest_contour], 0, (255, 255, 255), -1)
        self.image = cv2.bitwise_and(self.image, mask)

    # fix a bit
    def rotate(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        largest_contour = max(contours, key=cv2.contourArea)
        rect = cv2.minAreaRect(largest_contour)

        width = int(rect[1][0])
        height = int(rect[1][1])
        angle = rect[2]
        print(angle)
        if round(angle) == 90:
            print('extra')
            # extra_filter(self.image)
        elif 70 <= angle <= 95:
            angle -= 90
            m = cv2.getRotationMatrix2D(rect[0], angle, 1)

            result = cv2.warpAffine(self.image, m, (width, height))
            cv2.imshow('Cropped Image', result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            self.image = result
        else:
            m = cv2.getRotationMatrix2D(rect[0], angle, 1)

            result = cv2.warpAffine(self.image, m, (width, height))
            cv2.imshow('Cropped Image', result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            self.image = result  # fix

    def remove_black_cont(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        max_contour = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(max_contour)

        self.image = self.image[y:y + h, x:x + w]

    def show(self):
        cv2.imshow('Image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def filter(self, image):
        self.image = image
        self.show()
        self.remove_extra_colors()
        self.show()
        self.cut_back()
        self.show()


if __name__ == "__main__":
    print(1)
    F = Filter()
    for files in os.walk(r"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\F_cards"):
        for images in files[2]:
            image_load = cv2.imread(
                rf"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\F_cards\{images}")
            F.filter(image_load)
