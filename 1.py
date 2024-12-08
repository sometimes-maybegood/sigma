import sys
import random
from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication

class CircleDrawer(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Drawer")
        self.setGeometry(100, 100, 800, 600)
        self.circles = []
        self.btnDrawCircles = QtWidgets.QPushButton("Нарисовать окружности", self)
        self.btnDrawCircles.clicked.connect(self.draw_circles)
        self.btnDrawCircles.setGeometry(10, 10, 200, 40)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for circle in self.circles:
            color = QtGui.QColor(circle[3])
            painter.setBrush(color)
            painter.drawEllipse(circle[0], circle[1], circle[2], circle[2])

    def draw_circles(self):
        self.circles.clear()
        for _ in range(10):
            diameter = random.randint(20, 100)
            x = random.randint(0, self.width() - diameter)
            y = random.randint(0, self.height() - diameter)
            color = f'#{random.randint(0, 0xFFFFFF):06x}'
            self.circles.append((x, y, diameter, color))
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CircleDrawer()
    ex.show()
    sys.exit(app.exec())