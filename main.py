import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QRectF
import random


class MainWindow(QWidget):
    def __init__(self):

        super().__init__()
        self.do_paint = False
        self.click_btn = 10
        self.setGeometry(300, 300, 280, 170)

        self.setWindowTitle("My App")

        layout = QVBoxLayout()

        self.btn = QPushButton('Draw', self)
        self.btn.move(20, 120)
        self.btn.clicked.connect(self.draw_circle)
        layout.addWidget(self.btn)

        self.setLayout(layout)

    def draw_circle(self):
        self.do_paint = True
        self.click_btn += 10
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circles(qp)
            qp.end()

    def draw_circles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        size = self.size()

        for i in range(1000):
            x = random.randint(1, size.width() - 1)
            y = random.randint(1, size.height() - 1)
            rad = random.randint(1, self.click_btn)
            qp.drawEllipse(QRectF(x, y, rad, rad))

        self.do_paint = False

if __name__ == '__main__':
    app = QApplication([])
    ex = MainWindow()
    ex.show()
    app.exec()
