import asyncio
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

    def find_cards(self):  # Recognize cards
        pass

    def what_card(self):
        pass

    async def is_changes(self):
        if self.event.smt_happened():
            await self.play()
        await asyncio.sleep(1)  # FPS

    async def play(self):
        self.found_cards = self.recog.run()
        print(self.found_cards)
        # self.what_card()


async def main():
    game = Play()
    await game.is_changes()


if __name__ == "__main__":
    asyncio.run(main())
