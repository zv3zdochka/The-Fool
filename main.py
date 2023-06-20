import subprocess
from Drawer import RectangleAnimator
def run_recognition():
    process = subprocess.Popen(['python', 'Recog.py'], stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            # Преобразование вывода в список координат
            co_list = eval(output.decode())
            # Создание экземпляра класса RectangleAnimator и передача списка координат
            animator = RectangleAnimator(co_list)
            # Запуск отрисовки
            animator.start()

run_recognition()
