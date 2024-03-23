import sys
from PyQt5.QtCore import QRectF, Qt, QPointF, QTimer
from PyQt5.QtGui import QBrush, QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsView, QGraphicsScene


class AnimationView(QGraphicsView):
    def __init__(self, parent):
        super().__init__(parent)
        self.setSceneRect(QRectF(0, 0, 300, 200))
        self.setBackgroundBrush(QBrush(QColor(255, 255, 255)))
        self.setRenderHint(QPainter.Antialiasing)

        self.circle = QRectF(100, 75, 100, 100)
        self.target_circle = QRectF(100, 75, 100, 100)
        self.animation_step = 0
        self.animation_steps_total = 100

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(20)

    def paintEvent(self, event):
        painter = QPainter(self.viewport())
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(QColor(0, 0, 255)))
        painter.drawEllipse(self.circle)

    def animate(self):
        if self.animation_step >= self.animation_steps_total:
            return

        self.animation_step += 1
        progress = self.animation_step / self.animation_steps_total

        x = self.circle.x() + (self.target_circle.x() - self.circle.x()) * progress
        y = self.circle.y() + (self.target_circle.y() - self.circle.y()) * progress
        width = self.circle.width() + (self.target_circle.width() - self.circle.width()) * progress
        height = self.circle.height() + (self.target_circle.height() - self.circle.height()) * progress

        self.circle = QRectF(x, y, width, height)
        self.viewport().update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Пример PyQt5")
        self.setGeometry(100, 100, 300, 300)

        self.animation_view = AnimationView(self)
        self.animation_view.setGeometry(0, 0, 300, 200)

        button1 = QPushButton("Анимация 1", self)
        button1.setGeometry(50, 220, 100, 30)
        button1.clicked.connect(self.animateButton1)

        button2 = QPushButton("Анимация 2", self)
        button2.setGeometry(150, 220, 100, 30)
        button2.clicked.connect(self.animateButton2)

    def animateButton1(self):
        self.animation_view.target_circle = QRectF(50, 50, 200, 200)
        self.animation_view.animation_step = 0

    def animateButton2(self):
        self.animation_view.target_circle = QRectF(100, 75, 100, 100)
        self.animation_view.animation_step = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())