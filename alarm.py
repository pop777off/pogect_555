import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QTextEdit, QPushButton, QCalendarWidget, QMessageBox
from PyQt5.QtCore import QDate, Qt, QTime, QTimer


class NoteWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Заметки к врачу")
        self.resize(500, 400)

        # Создание виджетов
        self.note_label = QLabel("Заметка:")
        self.note_edit = QTextEdit()
        self.reminder_label = QLabel("Напоминание:")
        self.reminder_calendar = QCalendarWidget()
        self.reminder_time_label = QLabel("Время:")
        self.reminder_time_edit = QTextEdit()
        self.save_button = QPushButton("Сохранить")

        # Настройка макета
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.note_label)
        self.layout.addWidget(self.note_edit)
        self.layout.addWidget(self.reminder_label)
        self.layout.addWidget(self.reminder_calendar)
        self.layout.addWidget(self.reminder_time_label)
        self.layout.addWidget(self.reminder_time_edit)
        self.layout.addWidget(self.save_button)

        # Создание центрального виджета и установка макета
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        # Подключение событий
        self.save_button.clicked.connect(self.save_note)

    def save_note(self):
        note = self.note_edit.toPlainText()
        reminder_date = self.reminder_calendar.selectedDate()
        reminder_time = QTime.fromString(self.reminder_time_edit.toPlainText())

        current_date_time = QDate.currentDate().toString(Qt.ISODate) + " " + QTime.currentTime().toString(Qt.ISODate)
        reminder_date_time = reminder_date.toString(Qt.ISODate) + " " + reminder_time.toString(Qt.ISODate)

        if reminder_date_time <= current_date_time:
            QMessageBox.warning(self, "Ошибка", "Выберите корректное напоминание.")
            return

        # Здесь можно добавить логику сохранения заметки и установки напоминания

        QMessageBox.information(self, "Успех", "Заметка сохранена и напоминание установлено.")


if __name__ == "__main__":
    # Создание экземпляра приложения Qt
    app = QApplication(sys.argv)

    # Создание главного окна
    window = NoteWindow()
    window.show()

    # Запуск приложения
    sys.exit(app.exec_())