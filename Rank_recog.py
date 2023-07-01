import cv2
import pytesseract


path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract


class Rank:
    def recog_rank(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 3)
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        data = pytesseract.image_to_boxes(gray, config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789AKQJ')


        boxes = data.splitlines()
        digits = []
        for box in boxes:
            digit = box.split(' ')[0]
            digits.append(digit)


        if '1' in digits and '0' in digits:
            digits.remove('1')
            digits.remove('0')
            digits.append('10')


        return digits
