import cv2
import numpy as np


image = cv2.imread('table_image.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Определение диапазона синего цвета в HSV
lower_blue = np.array([90, 50, 50])
upper_blue = np.array([130, 255, 255])

# Применение цветового фильтра для обнаружения синего фона
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Применение морфологической операции для удаления шума
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Обнаружение контуров
contours, _ = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Фильтрация контуров по площади
filtered_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 1000:  # Подберите подходящий порог площади
        filtered_contours.append(contour)

# Обводка найденных контуров на изображении
cv2.drawContours(image, filtered_contours, -1, (0, 255, 0), 2)

cv2.imshow('Detected Cards', image)
cv2.waitKey(0)
cv2.destroyAllWindows()