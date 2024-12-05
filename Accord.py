import sounddevice as sd
import numpy as np
import time
import random

# Частоти нот для акордів (на основі стандартного настроювання)
chord_frequencies = {
    "C": [261.63, 329.63, 392.00],  # C, E, G
    "G": [196.00, 246.94, 392.00],  # G, B, D
    "D": [146.83, 293.66, 392.00],  # D, F#, A
    "Am": [220.00, 261.63, 440.00], # A, C, E
    "E": [164.81, 329.63, 659.25],  # E, G#, B
    "F": [174.61, 349.23, 440.00],  # F, A, C
}

# Генерація звуку акорду
def generate_chord(frequencies, duration=2, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    chord = sum(np.sin(2 * np.pi * freq * t) for freq in frequencies)
    return chord * 0.5  # Зменшення гучності

# Відтворення акорду
def play_chord(chord):
    sd.play(chord, samplerate=44100)
    sd.wait()

# Табулатура акордів
chords = {
    "C": "e|-0-\nB|-1-\nG|-0-\nD|-2-\nA|-3-\nE|-X-\n",
    "G": "e|-3-\nB|-0-\nG|-0-\nD|-0-\nA|-2-\nE|-3-\n",
    "D": "e|-2-\nB|-3-\nG|-2-\nD|-0-\nA|-X-\nE|-X-\n",
    "Am": "e|-0-\nB|-1-\nG|-2-\nD|-2-\nA|-0-\nE|-X-\n",
    "E": "e|-0-\nB|-0-\nG|-1-\nD|-2-\nA|-2-\nE|-0-\n",
    "F": "e|-1-\nB|-1-\nG|-2-\nD|-3-\nA|-3-\nE|-1-\n",
}

# Функція для навчання
def guitar_trainer():
    print("🎸 Вітаю у тренажері гри на гітарі! 🎶")
    print("Виберіть опцію:")
    print("1. Вивчити акорд")
    print("2. Практика випадкових акордів")
    print("3. Вийти")

    while True:
        choice = input("\nВаш вибір (1-3): ")
        if choice == "1":
            chord_name = input("Введіть назву акорду (C, G, D, Am, E, F): ").strip()
            if chord_name in chords:
                print(f"\nТабулатура для акорду {chord_name}:\n")
                print(chords[chord_name])
                if chord_name in chord_frequencies:
                    print("🎵 Відтворення звуку акорду...")
                    chord = generate_chord(chord_frequencies[chord_name])
                    play_chord(chord)
                else:
                    print("⛔ Для цього акорду немає частот.")
            else:
                print("⛔ Акорд не знайдено. Спробуйте ще раз.")
        elif choice == "2":
            print("\nПрактика випадкових акордів. Натисніть Ctrl+C для виходу.\n")
            try:
                while True:
                    chord_name = random.choice(list(chords.keys()))
                    print(f"Зіграйте акорд {chord_name}!")
                    print(chords[chord_name])
                    if chord_name in chord_frequencies:
                        chord = generate_chord(chord_frequencies[chord_name])
                        play_chord(chord)
                    else:
                        print("⛔ Для цього акорду немає частот.")
                    time.sleep(2)
            except KeyboardInterrupt:
                print("\n🎸 Практику завершено!")
        elif choice == "3":
            print("🎶 До зустрічі! Успіхів у грі на гітарі! 🎵")
            break
        else:
            print("⛔ Невірний вибір. Спробуйте ще раз.")

# Запуск тренажера
guitar_trainer()
