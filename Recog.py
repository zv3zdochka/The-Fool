import cv2
import numpy as np
import mss


class ScreenCapture:
    def __init__(self):
        # Screen dimensions
        self.screen_width = 1920
        self.screen_height = 108
        self.target_resolution = (self.screen_width, self.screen_height)

        # Regions of interest
        self.regions_of_interest = [
            (20, 250, 180, 550),
            (200, 270, 1780, 560),
            (30, 555, 1850, 900),
        ]

        # Minimum and maximum allowed rectangle sizes
        self.min_rectangle_size = 80
        self.max_rectangle_size = 400

        # Convert color values to grayscale
        self.gray_lower_white = np.array([220, 220, 220])
        self.gray_upper_white = np.array([255, 255, 255])

        # morphological operations
        self.kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    def capture_screen(self):
        with mss.mss() as sct:
            monitor = sct.monitors[1]
            screenshot = sct.grab(monitor)
            image = np.array(screenshot)
            image = cv2.resize(image, self.target_resolution)
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
            return image

    def process_screen(self, image):
        # сonvert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # filter to extract white color
        mask = cv2.inRange(image, self.gray_lower_white, self.gray_upper_white)

        # morphological operations to remove noise
        opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, self.kernel, iterations=0)

        # contours on the processed image
        contours, _ = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

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
                        print("Square coordinates:", x, y, x + w, y + h)

    def run(self):
        while True:
            # сapture screen image
            image = self.capture_screen()
            self.process_screen(image)

            # Close windows
            if cv2.waitKey(1) == 27:  # Esc key
                break

        cv2.destroyAllWindows()



# screen_capture = ScreenCapture()
# screen_capture.run()
