import asyncio
import time
import cv2
from Contur import ScreenContur
from Rank_recog import Rank
from Suit_recog import Suit
from Event import Event


class Play:
    def __init__(self):
        self.recog = ScreenContur()  # Recognizer
        self.rank = Rank()
        self.suit = Suit()
        self.player = ""
        self.event = Event()
        self.instructions = []
        self.found_cards = []
        self.my_cards = []

    def what_card(self):
        for i in self.found_cards:
            coords, image = i[0], i[1]


    async def is_changes(self):
        if self.event.smt_happened():
            await self.play()
        await asyncio.sleep(1)  # FPS

    async def play(self):
        self.found_cards = self.recog.run()
        #print(self.found_cards)
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
