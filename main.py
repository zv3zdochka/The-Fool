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
        self.condition = False


    def find_cards(self):  # Recognize cards
        pass


    def what_card(self):
        pass

    async def is_changes(self):
        if self.event.smt_happened():
            asyncio.ensure_future(self.play())
        await asyncio.sleep(1)#FPS

    async def play(self):
        print("Функция play() запущена")



game = Play()
game.condition = True
game.is_changes()
loop = asyncio.get_event_loop()
loop.run_forever()
loop.close()
