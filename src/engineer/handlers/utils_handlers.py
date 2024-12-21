import random
from telebot.types import (ReplyKeyboardMarkup)

# Enviar teclado de opciones para una pregunta
def create_question_keyboard(options):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    shuffled_options = options[:]
    random.shuffle(shuffled_options)  # Mezclar el orden de las opciones
    shuffled_options.append("❌ Cancel")
    shuffled_options.append("🛑 Stop")
    shuffled_options.append("🗑️ Delete")
    for option in shuffled_options:
        keyboard.add(option)
    return keyboard
