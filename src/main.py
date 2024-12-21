import telebot
import time
from data.loader import load_english_data,load_engineer_data  
from english.utils.keyboard import create_reply_keyboard
from english.index import state_handlers,english_to_handler,text_responses_english
from engineer.index import text_responses_engineer,engineer_to_handler

user_states = {}


@bot.message_handler(func=lambda message: message.text == "🤓 Start Study")
def handle_study_button(message):
    user_states[message.chat.id] = {"state": "study"}
    bot.send_message(
        message.chat.id, "please choose one topic",reply_markup=create_reply_keyboard([["🇬🇧 English", "🛠️ Engineer","🌍 Human"],["❌ Cancel"]]),
    )

@bot.message_handler(func=lambda message: message.text == "❌ Cancel")
def handle_cancel_button(message):
    user_states[message.chat.id] = {"state": "none"}
    bot.send_message(
        message.chat.id,
        "🌟 It was a pleasure to help you with your workout today! 😊💪",
        reply_markup=create_reply_keyboard([["🤓 Start Study"]])
    )

# -------------------------------------- Engineer ----------------------------------------------------------
@bot.message_handler(func=lambda message: message.text in text_responses_engineer)
def handle_text_engineer(message):
    chat_id = message.chat.id
    user_input = message.text
    response_info = text_responses_engineer[user_input]
    if "state" in response_info:
        user_states[chat_id] = {"state": response_info["state"]}
    bot.send_message(
        chat_id,
        response_info["response"],
        reply_markup=create_reply_keyboard(response_info.get("keyboard", lambda: [])())
    )

@bot.message_handler(func=lambda message: message.text in engineer_to_handler)
def handle_dynamic_enginner(message):
    handler_function = engineer_to_handler[message.text]
    handler_function(bot, message, engineer_data, user_states)

# -------------------------------------- ENGLISH ----------------------------------------------------------

@bot.message_handler(func=lambda message: message.text in text_responses_english)
def handle_text_english(message):
    chat_id = message.chat.id
    user_input = message.text
    response_info = text_responses_english[user_input]
    if "state" in response_info:
        user_states[chat_id] = {"state": response_info["state"]}
    bot.send_message(
        chat_id,
        response_info["response"],
        reply_markup=create_reply_keyboard(response_info.get("keyboard", lambda: [])())
    )


@bot.message_handler(func=lambda message: message.text in english_to_handler)
def handle_dynamic_english(message):
    handler_function = english_to_handler[message.text]
    handler_function(bot, message, english_data, user_states)

@bot.message_handler(func=lambda message: user_states.get(message.chat.id, {}).get("state") in state_handlers)
def check_answer(message):
    chat_id = message.chat.id
    state_info = user_states[chat_id]
    current_state = state_info["state"]
    correct_answer = state_info["phrase_info"]["answer"]

    if message.text.strip().lower() in [correct_answer.lower(), "next"]:
        bot.reply_to(message, "Correct! ✅🎉 Moving to the next exercise.")
        handler = state_handlers.get(current_state)
        if handler:
            handler(bot, message, english_data, user_states)
    else:
        bot.reply_to(message, "Wrong, try again.")

def handle_callback(call, field):
    response = user_states[call.message.chat.id]["phrase_info"].get(field, "No information available.")
    if field == "pronunciation":
        audio_message = bot.send_audio(call.message.chat.id, response)
        message_id = audio_message.message_id
        time.sleep(25)
        bot.delete_message(call.message.chat.id, message_id)
    else:
        bot.send_message(call.message.chat.id, response)

@bot.callback_query_handler(func=lambda call: call.data in ["show_answer", "show_pronunciation", "show_translation", "show_why"])
def handle_callbacks(call):
    field_map = {
        "show_answer": "answer",
        "show_pronunciation": "pronunciation",
        "show_translation": "translation",
        "show_why": "why",
    }
    field = field_map[call.data]
    handle_callback(call, field)





if __name__ == "__main__":
    english_data = load_english_data()
    engineer_data = load_engineer_data()
    bot.polling(none_stop=True)
