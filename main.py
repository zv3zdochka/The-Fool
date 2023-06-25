import time
import sched
from Contur import ScreenContur


class Play:
    def __init__(self):
        self.recog = ScreenContur()
        self.scheduler = sched.scheduler(time.time, time.sleep)
    def cards_co(self):


    def my_function():
        print("Вызвана функция")



    def schedule_function():
        my_function()
        scheduler.enter(0.01, 1, schedule_function)  # Планируем вызов функции через 0.01 секунды (10 миллисекунд)

    scheduler.enter(0, 1, schedule_function)

    scheduler.run()
