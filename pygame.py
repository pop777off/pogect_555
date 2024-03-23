import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QTextDocument

def button_clicked():
    text = line_edit.text()
    if text:
        try:
            with open("введенный_текст.txt", "w") as file:
                file.write(text)
                QMessageBox.information(window, "Успех", "Текст успешно сохранен в файл 'введенный_текст.txt'")
        except IOError:
            QMessageBox.critical(window, "Ошибка", "Не удалось сохранить текст в файл")
    else:
        QMessageBox.warning(window, "Предупреждение", "Поле ввода текста пустое")

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Пример приложения с кнопкой и полем ввода")
window.setGeometry(100, 100, 500, 300)

line_edit = QLineEdit(window)
line_edit.setGeometry(100, 50, 200, 30)

button = QPushButton("Сохранить текст", window)
button.setGeometry(100, 100, 120, 30)
button.clicked.connect(button_clicked)

window.show()

sys.exit(app.exec_())