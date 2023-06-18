import cv2
import numpy as np
import mss

# Размеры экрана
screen_width = 1920
screen_height = 1080

# Разрешение целевого изображения
target_resolution = (screen_width, screen_height)

# Определение областей интереса (x, y, ширина, высота)
regions_of_interest = [
    (20, 250, 180, 550),
    (200, 270, 1780, 560),
    (30, 555, 1850, 900),
]

# Минимальные и максимальные разрешенные размеры прямоугольников
min_rectangle_size = 80  # Минимальная ширина или высота
max_rectangle_size = 400  # Максимальная ширина или высота


def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Индекс монитора, с которого вы хотите получить снимок
        screenshot = sct.grab(monitor)
        image = np.array(screenshot)
        image = cv2.resize(image, (screen_width, screen_height))
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        return image


while True:
    # Получение изображения с экрана
    image = capture_screen()

    # Преобразование изображения в оттенки серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Применение фильтра для выделения белого цвета
    lower_white = np.array([220, 220, 220])
    upper_white = np.array([255, 255, 255])
    mask = cv2.inRange(image, lower_white, upper_white)

    # Применение морфологических операций для удаления шума
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    opened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=0)

    # Нахождение контуров на обработанном изображении
    contours, _ = cv2.findContours(opened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Вывод координат квадратов
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if min_rectangle_size <= w <= max_rectangle_size and min_rectangle_size <= h <= max_rectangle_size:
            for roi in regions_of_interest:
                roi_x, roi_y, roi_w, roi_h = roi
                if roi_x <= x <= roi_x + roi_w and roi_y <= y <= roi_y + roi_h:
                    print("Square coordinates:", x, y, x + w, y + h)

# Закрытие окон
cv2.destroyAllWindows()
