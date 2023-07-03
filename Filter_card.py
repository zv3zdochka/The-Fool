import cv2
import numpy as np
import os

for files in os.walk("F_cards"):
    for images in files[2]:
        #image = cv2.imread(r"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\F_cards\output_image50.jpg")
        image = cv2.imread(rf"F_cards\{images}")

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        largest_contour = max(contours, key=cv2.contourArea)

        mask = np.zeros_like(image)

        cv2.drawContours(mask, [largest_contour], 0, (255, 255, 255), -1)
        result = cv2.bitwise_and(image, mask)
        cv2.imshow('Cropped Image', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        image = result

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        largest_contour = max(contours, key=cv2.contourArea)
        rect = cv2.minAreaRect(largest_contour)

        box = cv2.boxPoints(rect)
        box = np.intp(box)
        width = int(rect[1][0])
        height = int(rect[1][1])
        angle = rect[2]
        if angle == '90.0':
            result = image
        elif 70 <= angle <= 95:
            angle -= 90
            M = cv2.getRotationMatrix2D(rect[0], angle, 1)

            result = cv2.warpAffine(image, M, (width, height))
        else:
            M = cv2.getRotationMatrix2D(rect[0], angle, 1)

            result = cv2.warpAffine(image, M, (width, height))
        cv2.imshow('Cropped Image', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        image = result

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        max_contour = max(contours, key=cv2.contourArea)

        x, y, w, h = cv2.boundingRect(max_contour)

        cropped_image = image[y:y+h, x:x+w]

        cv2.imshow('Cropped Image', cropped_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
