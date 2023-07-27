import asyncio
import random
import time
import cv2
from Contur import ScreenContur
from Rank import Rank
from Suit import Suit
from Event import Event
from Filter import Filters


class Play:
    def __init__(self):
        self.recog = ScreenContur()  # Recognizer
        self.rank = Rank()
        self.suit = Suit()
        self.filt = Filters()
        self.event = Event()
        self.player = ""
        self.instructions = []
        self.found_cards = []
        self.my_cards = []

    def what_card(self):
        if not self.found_cards:
            print('No cards what card func')
        for i in self.found_cards:
            coords, image = i[0], i[1]

            im_for_rc = self.filt.filter(image)
            #cv2.imshow("im", im_for_rc)
            #cv2.imwrite(rf"C:\Users\batsi\OneDrive\Documents\PycharmProjects\The_Fool_Game\Problems\{random.randrange(0,1000)}.jpg", im_for_rc)
            self.rank.do(im_for_rc)

    async def is_changes(self):
        if self.event.smt_happened():
            await self.play()
        await asyncio.sleep(1)  # FPS

    async def play(self):
        self.found_cards = self.recog.run()
        self.what_card()

    async def play_fool(self):
        time.sleep(3)  # waiting for start
        self.found_cards = self.recog.run()
        # here we need to part cards for mine and козырь also if enemy start we need to check it


async def main():
    game = Play()
    await game.is_changes()


if __name__ == "__main__":
    asyncio.run(main())
