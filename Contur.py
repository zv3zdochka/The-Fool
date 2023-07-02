import cv2
import numpy as np
import mss
from Rank_recog import Rank

class ScreenContur:
    def __init__(self):
        # screen dimensions
        self.screen_width = 1920
        self.screen_height = 1080
        self.target_resolution = (self.screen_width, self.screen_height)

        # regions of interest
        self.regions_of_interest = [
            (20, 250, 180, 550),
            (200, 270, 1780, 560),
            (30, 555, 1850, 900),
        ]

        # rectangle sizes
        self.min_rectangle_size = 80
        self.max_rectangle_size = 400

        # convert color
        self.gray_lower_white = np.array([220, 220, 220])
        self.gray_upper_white = np.array([255, 255, 255])

        # morphological operation
        self.kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

        # lists
        self.co_list = []
        self.reg_cards = []
        self.result = []
    def capture_screen(self):
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)
            image = np.array(screenshot)
            image = cv2.resize(image, self.target_resolution)
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
            return image

    def remove_nested_quads(self, coords_list):
        result = []
        n = len(coords_list)

        for i in range(n):
            quad = coords_list[i]
            is_nested = False

            for j in range(n):
                if i != j:
                    other_quad = coords_list[j]
                    if self.is_quad_nested(quad, other_quad):
                        is_nested = True
                        break

            if not is_nested:
                result.append(quad)

        return result

    def remove_unwanted_reg_cards(self):
        demi_cards = []
        for i in self.reg_cards:
            if i[0] in self.result:
                demi_cards.append(i)
        self.reg_cards = demi_cards

    @staticmethod
    def is_quad_nested(quad1, quad2):
        x1, y1, w1, h1 = quad1
        x2, y2, w2, h2 = quad2

        if (x1 >= x2 and y1 >= y2 and x1 + w1 <= x2 + w2 and y1 + h1 <= y2 + h2):
            return True

        return False

    def process_screen(self, image):
        # convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        mask = cv2.inRange(image, self.gray_lower_white, self.gray_upper_white)

        # remove noise
        opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.kernel, iterations=0)

        # find contours
        contours, _ = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.co_list = []
        # coordinates of squares
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if (
                    self.min_rectangle_size <= w <= self.max_rectangle_size
                    and self.min_rectangle_size <= h <= self.max_rectangle_size
            ):
                for roi in self.regions_of_interest:
                    roi_x, roi_y, roi_w, roi_h = roi
                    if roi_x <= x <= roi_x + roi_w and roi_y <= y <= roi_y + roi_h:
                        self.reg_cards.append([(x, y, w, h), image[y:y + h, x:x + w]])
                        self.co_list.append((x, y, w, h))

                        #print(rank.recog_rank(image[y:y + h, x:x + w]))
                        cv2.imshow('Изображение', image[y:y + h, x:x + w])
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()



        self.result = self.remove_nested_quads(self.co_list)
        self.remove_unwanted_reg_cards()
        #return self.reg_cards
        return self.result


    def ret_ima_co(self):
        return self.reg_cards
    def run(self):
        # Capture screen image
        image = self.capture_screen()
        return self.process_screen(image)


if __name__ == "__main__":
    screen_contour = ScreenContur()
    result = screen_contour.run()

