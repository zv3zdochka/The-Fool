import cv2
import numpy as np
import os


class Filter:
    def __init__(self):
        self.image = None
    @staticmethod
    def remove_close_points(points):
        distance = 10
        filtered_points = []
        for point in points:
            keep = True
            for f_point in filtered_points:
                if abs(point[0] - f_point[0]) <= distance and abs(point[1] - f_point[1]) <= distance:
                    keep = False
                    break
            if keep:
                filtered_points.append(point)
        return filtered_points

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

    def problem_rotate(self):
        self.place_image_in_rectangle()
        self.show()
        cv2.imwrite("pr.jpg", self.image)
        self.rotate()
        self.show()

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

            self.problem_rotate()

        elif 70 <= angle <= 95:
            angle -= 90
            m = cv2.getRotationMatrix2D(rect[0], angle, 1)

            result = cv2.warpAffine(self.image, m, (width, height))
            self.image = result
        else:
            m = cv2.getRotationMatrix2D(rect[0], angle, 1)

            result = cv2.warpAffine(self.image, m, (width, height))

            self.image = result  # fix

    def place_image_in_rectangle(self):

        height, width = self.image.shape[:2]

        new_width = int(width * 1.3)
        new_height = int(height * 1.3)

        rectangle = np.full((new_height, new_width, 3), (0, 0, 0), dtype=np.uint8)

        x_offset = int((new_width - width) / 2)
        y_offset = int((new_height - height) / 2)

        rectangle[y_offset:y_offset + height, x_offset:x_offset + width] = self.image
        self.image = rectangle

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
        self.rotate()
        self.show()


if __name__ == "__main__":
    F = Filter()
    for files in os.walk(r"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\F_cards"):
        for images in files[2]:
            image_load = cv2.imread(
                rf"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\F_cards\{images}")
            F.filter(image_load)
