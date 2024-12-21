from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

def handle_past_tense(bot, message, data, user_states):
    phrase_info = random.choice(data["past_tense"]["phrases"])
    user_states[message.chat.id] = {
        "state": "past_tense",
        "phrase_info": phrase_info,
    }

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    markup.add(InlineKeyboardButton("🤔 Show Why", callback_data="show_why"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

def handle_present_tense(bot, message, data, user_states):
    phrase_info = random.choice(data["present_tense"]["phrases"])
    user_states[message.chat.id] = {
        "state": "present_tense",
        "phrase_info": phrase_info,
    }

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    markup.add(InlineKeyboardButton("🤔 Show Why", callback_data="show_why"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

def handle_future_tense(bot, message, data, user_states):
    phrase_info = random.choice(data["futuro_tense"]["phrases"])
    user_states[message.chat.id] = {
        "state": "futuro_tense",
        "phrase_info": phrase_info,
    }

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    markup.add(InlineKeyboardButton("🤔 Show Why", callback_data="show_why"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

def handle_modal_verbs(bot, message, data, user_states):
    phrase_info = random.choice(data["modal_verbs"]["phrases"])
    user_states[message.chat.id] = {
        "state": "modal_verbs",
        "phrase_info": phrase_info,
    }

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

def handle_conditional(bot, message, data, user_states):
    phrase_info = random.choice(data["conditional_setence"]["phrases"])
    user_states[message.chat.id] = {"state": "conditional_setence", "phrase_info": phrase_info}
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

def handle_ielts_linked_words(bot, message, data, user_states):
    phrase_info = random.choice(data["ielts_linked_words"]["phrases"])
    user_states[message.chat.id] = {"state": "ielts_linked_words", "phrase_info": phrase_info}
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)
