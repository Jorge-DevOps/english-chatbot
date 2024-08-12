from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

def handle_questions_IELTS(bot, message, data, user_states):
    phrase_info = random.choice(data["ielts_speakingQuestions"]["phrases"])
    user_states[message.chat.id] = {"state": "ielts_speakingQuestions", "phrase_info": phrase_info}
    
    markup = InlineKeyboardMarkup()
    bot.send_message(message.chat.id, phrase_info["Question"], reply_markup=markup)

def handle_new_vocabulary(bot, message, data, user_states):
    phrase_info = random.choice(data["new_vocabulary"]["phrases"])
    user_states[message.chat.id] = {"state": "new_vocabulary", "phrase_info": phrase_info}
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    markup.add(InlineKeyboardButton("🅰️ Show Spelling", callback_data="show_pronunciation"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

def handle_ielts_vocabulary(bot, message, data, user_states):
    phrase_info = random.choice(data["ielts_vocabulary"]["phrases"])
    user_states[message.chat.id] = {"state": "ielts_vocabulary", "phrase_info": phrase_info}
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    markup.add(InlineKeyboardButton("🌐 Show Translation", callback_data="show_translation"))
    bot.send_audio(message.chat.id, phrase_info["pronunciation"], reply_markup=markup)

def handle_films_vocabulary(bot, message, data, user_states):
    phrase_info = random.choice(data["films_vocabulary"]["phrases"])
    user_states[message.chat.id] = {"state": "films_vocabulary", "phrase_info": phrase_info}
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    markup.add(InlineKeyboardButton("🅰️ Show Spelling", callback_data="show_pronunciation"))
    markup.add(InlineKeyboardButton("🌐 Show Translation", callback_data="show_translation"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

def handle_books_vocabulary(bot, message, data, user_states):
    phrase_info = random.choice(data["books_vocabulary"]["phrases"])
    user_states[message.chat.id] = {"state": "books_vocabulary", "phrase_info": phrase_info}
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    markup.add(InlineKeyboardButton("🅰️ Show Spelling", callback_data="show_pronunciation"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

def handle_day_vocabulary(bot, message, data, user_states):
    phrase_info = random.choice(data["vocabulary"]["phrases"])
    user_states[message.chat.id] = {"state": "new_vocabulary", "phrase_info": phrase_info}
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    markup.add(InlineKeyboardButton("🅰️ Show Spelling", callback_data="show_pronunciation"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

