import time

import cv2
import numpy as np
import mss


def take_screenshot():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        screenshot = sct.grab(monitor)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    return img


def crop_image(image, regions):
    cropped_images = []

    for region in regions:
        x, y, w, h = region
        cropped_image = image[y:y + h, x:x + w]
        cropped_images.append(cropped_image)

    return cropped_images


def display_images(images):
    for i, img in enumerate(images):
        cv2.imshow(f'Image {i + 1}', img)
        cv2.waitKey(10000)  # Ждет 1000 миллисекунд (1 секунда)
    cv2.destroyAllWindows()

    # Дожидаемся нажатия любой клавиши
    cv2.waitKey(0)
    # Закрываем все окна
    cv2.destroyAllWindows()


# Пример использования
if __name__ == "__main__":
    # Шаг 1: Сделать скриншот
    time.sleep(3)
    screenshot = take_screenshot()

    # Шаг 2: Указать области для обрезки в формате (x, y, width, height)
    regions = [
        # (0, 520, 1920, 380),  # hand
        # (0, 100, 200, 450),  # deck
        (100, 250, 1900, 280)  # table
        # Добавьте больше областей по вашему желанию
    ]

    # Шаг 3: Обрезать изображение по заданным областям
    cropped_images = crop_image(screenshot, regions)

    # Шаг 4: Отобразить обрезанные изображения
    display_images(cropped_images)
