import cv2
import pytesseract
import os


path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract


class Rank:
    @staticmethod
    def crop(image):

        cropped_image = image[:120, :80]

        # cv2.imshow('Cropped Image', cropped_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        return cropped_image


    def recog_rank(self, image):
        cv2.imshow('Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Установка параметров для pytesseract (языковой пакет и распознавание только заглавных букв)
        custom_config = r'-l rus --psm 6'

        # Распознавание текста на изображении
        text = pytesseract.image_to_string(gray, config=custom_config)


        print(text)
        return text

if __name__ == "__main__":
    F = Rank()

    for files in os.walk(r"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\Problems"):
        for images in files[2]:
            image_load = cv2.imread(
                rf"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\Problems\{images}")
            #F.recog_rank(image_load)
            c_i = F.crop(image_load)
            F.recog_rank(c_i)