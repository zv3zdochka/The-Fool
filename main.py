import time
import sched
from Contur import ScreenContur


class Play:
    def __init__(self):
        self.recog = ScreenContur() # Recognizer
        self.rank = ""
        self.suit = ''
        self.player = ""


    def find_cards(self): # Recognize cards
        pass

    def what_card(self):
        pass