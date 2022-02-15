import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 600)
        self.btn = QPushButton(self, text=["Нарисовать круг?", "Нарисовать круг.", "Нарисовать круг!"][1])
        self.btn.clicked.connect(self.set_coords)
        self.btn.setGeometry(250, 250, 100, 25)
        self.coords = 300, 300
        self.size = 10

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor("yellow"))
        qp.drawEllipse(*self.coords, self.size, self.size)

    def set_coords(self):
        self.sender().setText(["Нарисовать круг?", "Нарисовать круг.", "Нарисовать круг!"][randint(0, 2)])
        self.coords = randint(50, 550), randint(50, 550)
        self.size = randint(1, 50)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
