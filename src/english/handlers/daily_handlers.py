import random
import time


def handle_daily_vocabulary(chat_id, bot, data):
    phrase_info = random.choice(data["daily_Vocabulary"]["phrases"])
    
    bot.send_message(chat_id, {phrase_info['word']}, parse_mode="MarkdownV2")
    # audio_message = bot.send_audio(chat_id, phrase_info["pronunciation"])
    # message_id = audio_message.message_id
    # bot.send_message(chat_id, f"Translation 🌐: {phrase_info['translation']}")
    # time.sleep(10)
    # bot.delete_message(chat_id, message_id)

def handle_daily_Englishtip(chat_id, bot, data):
    phrase_info = random.choice(data["english_tips"]["phrases"])
    bot.send_message(chat_id, phrase_info["rule"])

def handle_daily_IETLStip(chat_id, bot, data):
    phrase_info = random.choice(data["IELTS_tips"]["phrases"])
    bot.send_message(chat_id, phrase_info["rule"])

def handle_daily_phrasalVerb(chat_id, bot, data):
    phrase_info = random.choice(data["daily_PhrasalVerbs"]["phrases"])
    bot.send_message(chat_id, {phrase_info['phrasal_verb']}, parse_mode="MarkdownV2")

def handle_daily_verb(chat_id, bot, data):
    phrase_info = random.choice(data["daily_Verbs"]["phrases"])
    bot.send_message(chat_id, {phrase_info['word']}, parse_mode="MarkdownV2")
