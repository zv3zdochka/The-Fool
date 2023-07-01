import time
import sched
from Contur import ScreenContur
from Rank_recog import Rank
from Suit_recog import Suit
from Event import Event


class Play:
    def __init__(self):
        self.recog = ScreenContur() # Recognizer
        self.rank = Rank()
        self.suit = Suit()
        self.player = ""
        self.event = Event()
        self.instructions = []
        self.condition = False

    def find_cards(self): # Recognize cards
        pass

    def what_card(self):
        pass

    def play(self):
        pass

    def is_changes(self):
        if self.condition:
            pass

