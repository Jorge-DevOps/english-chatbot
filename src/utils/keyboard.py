from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

def create_reply_keyboard(buttons):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for row in buttons:
        markup.row(*[KeyboardButton(button) for button in row])
    return markup

def create_inline_keyboard(buttons):
    markup = InlineKeyboardMarkup()
    for row in buttons:
        markup.row(*[InlineKeyboardButton(button[0], callback_data=button[1]) for button in row])
    return markup