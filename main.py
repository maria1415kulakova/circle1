import sys, random
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor


class Circle(QMainWindow):
    def __init__(self):
        super(Circle, self).__init__()
        self.flag = False
        uic.loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.draw_circle)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(255, 255, 0))
            a = random.randint(10, self.width() // 3)
            qp.drawEllipse(self.width() // 2 - a, self.height() // 2 - a, a * 2, a * 2)
            qp.end()

    def draw_circle(self):
        self.flag = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())
