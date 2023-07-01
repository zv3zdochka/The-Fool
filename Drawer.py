import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QColor, QPen
from PyQt5.QtCore import Qt, QTimer, QRect
import random
from Contur import ScreenContur as Recognizer

class DrawingWindow(QMainWindow):
    def __init__(self, coordinates):
        super().__init__()
        self.setWindowTitle("Transparent Drawing Window")
        self.setGeometry(0, 0, QApplication.desktop().screenGeometry().width(),
                         QApplication.desktop().screenGeometry().height())
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.painter = QPainter()
        self.painter.setRenderHint(QPainter.Antialiasing)

        self.pen_color = QColor(255, 0, 0)
        self.pen_width = 4

        self.coordinates = coordinates

        self.draw_timer = QTimer()

        self.draw_timer.start(10)  # upd every 10 milliseconds

    def paintEvent(self, event):
        self.painter.begin(self)
        self.painter.setPen(Qt.NoPen)
        self.painter.setBrush(QBrush(Qt.transparent))
        self.painter.drawRect(QRect(0, 0, self.width(), self.height()))  #transparent background

        self.painter.setPen(QPen(QColor(self.pen_color), self.pen_width))
        self.painter.setBrush(QBrush(Qt.transparent))

        for coord in self.coordinates:
            x, y, width, height = coord
            self.painter.drawRect(x, y, width, height)  #

        self.painter.end()

        self.update_coord()
        QTimer.singleShot(1000, self.update)

    def update_coord(self):
        new_coord = R.run()
        if new_coord is list:
            self.coordinates = new_coord
        else:
            self.coordinates = list(new_coord)


if __name__ == "__main__":
    s_coordinates = [(524, 474, 818-524, 689-474), (524, 367, 818-524, 473-367)]

    app = QApplication(sys.argv)
    R = Recognizer()
    window = DrawingWindow(s_coordinates)
    window.show()

    sys.exit(app.exec_())
