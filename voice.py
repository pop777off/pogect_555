import sys
import pyttsx3
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создание экземпляра движка речевого синтеза
        self.engine = pyttsx3.init()

        # Создание виджетов
        self.label = QLabel("Введите текст:")
        self.text_edit = QLineEdit()
        self.button = QPushButton("Произнести")

        # Настройка макета
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.button)

        # Установка макета в главное окно
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        # Подключение событий
        self.button.clicked.connect(self.speak_text)

    def speak_text(self):
        # Получение текста из текстового поля
        text = self.text_edit.text()

        # Произнесение текста
        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == "__main__":
    # Создание экземпляра приложения Qt
    app = QApplication(sys.argv)

    # Создание главного окна
    window = MainWindow()
    window.show()

    # Запуск приложения
    sys.exit(app.exec_())