import tkinter as tk
import pyttsx3

def speak():
    text = text_entry.get(1.0, tk.END).strip()
    engine = pyttsx3.init()

    # Определение детского голоса
    voices = engine.getProperty('voices')
    child_voice_id = None
    for voice in voices:
        if 'child' in voice.name.lower():
            child_voice_id = voice.id
            break
    if child_voice_id:
        engine.setProperty('voice', child_voice_id)

    engine.say(text)
    engine.runAndWait()

# Создание графического интерфейса
window = tk.Tk()
window.title("Синтезатор голоса")

# Создание виджетов
text_entry = tk.Text(window, height=5, width=30)
speak_button = tk.Button(window, text="Произнести", command=speak)

# Размещение виджетов
text_entry.pack(pady=10)
speak_button.pack(pady=5)

# Запуск приложения
window.mainloop()