from data.loader import load_exercise_data  
from handlers.start_handlers import welcome,grammar,vocabulary,IETLS
from handlers.vocabulary_handlers import (handle_questions_IELTS,handle_ielts_vocabulary,handle_films_vocabulary,handle_books_vocabulary,handle_day_vocabulary)
from handlers.daily_handlers import (handle_daily_vocabulary,handle_daily_Englishtip,handle_daily_IETLStip,handle_daily_phrasalVerb,handle_daily_verb)
from handlers.grammar_handlers import handle_past_tense, handle_present_tense, handle_future_tense, handle_modal_verbs, handle_conditional,handle_ielts_linked_words
from handlers.activity_handlers import handle_audio_exercises,handle_movies_sentences,handle_phrasal_verbs,handle_podcast_exercises
from utils.keyboard import create_reply_keyboard
import telebot
import time
import threading
from datetime import datetime, timedelta

bot = telebot.TeleBot("7398395154:AAEguy0doM7Bb8K4dZFm5XDwdDIHWIvIpJo")

user_states = {}

@bot.message_handler(func=lambda message: message.text == "❌ Cancel")
def handle_cancel_button(message):
    user_states[message.chat.id] = {"state": "none"}
    bot.send_message(message.chat.id, "🌟 It was a pleasure to help you with your English today! 😊📚", reply_markup=create_reply_keyboard(welcome()))

@bot.message_handler(func=lambda message: message.text == "▶️ Start" or message.text == "/start")
def handle_start_button(message):
    bot.send_message(message.chat.id, "👋 Hi, I'm your English Trainer Bot! 😊 I'm here to help you improve your English skills. Let's get started! 🚀📚", reply_markup=create_reply_keyboard(welcome()))


#----------------------------------------------------------------------------------------------------------------------------------------

@bot.message_handler(func=lambda message: message.text == "💭 Phrasal Verbs")
def handle_phrasal_verbs_wrapper(message):
    handle_phrasal_verbs(bot, message, data, user_states)

@bot.message_handler(func=lambda message: message.text == "🎬 Movie Exercises")
def handle_movies_sentences_wrapper(message):
    handle_movies_sentences(bot, message, data, user_states)

@bot.message_handler(func=lambda message: message.text == "🎧 Listening Exercises")
def handle_audio_exercises_wrapper(message):
    handle_audio_exercises(bot, message, data, user_states)


@bot.message_handler(func=lambda message: message.text == "🎙️ Podcast Exercises")
def handle_podcast_exercises_wrapper(message):
    handle_podcast_exercises(bot, message, data, user_states)

#----------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == "🆕 Vocabulary")
def handle_vocabulary(message):
    bot.send_message(message.chat.id, "Choose a topic:", reply_markup=create_reply_keyboard(vocabulary()))
    user_states[message.chat.id] = {"state": "grammar"}


#----------------------------------------------------------------------------------------------------------------------------------------

@bot.message_handler(func=lambda message: message.text == "📚 Grammar")
def handle_grammar(message):
    bot.send_message(message.chat.id, "Choose a topic:", reply_markup=create_reply_keyboard(grammar()))
    user_states[message.chat.id] = {"state": "grammar"}

@bot.message_handler(func=lambda message: message.text == "🕰️ Past")
def handle_past_tense_wrapper(message):
    handle_past_tense(bot, message, data, user_states)

@bot.message_handler(func=lambda message: message.text == "🎁 Present")
def handle_present_tense_wrapper(message):
    handle_present_tense(bot, message, data, user_states)

@bot.message_handler(func=lambda message: message.text == "🔮 Future")
def handle_future_tense_wrapper(message):
    handle_future_tense(bot, message, data, user_states)

@bot.message_handler(func=lambda message: message.text == "🗯️ Modal Verbs")
def handle_modal_verbs_wrapper(message):
    handle_modal_verbs(bot, message, data, user_states)

@bot.message_handler(func=lambda message: message.text == "🔍 Conditional")
def handle_conditional_wrapper(message):
    handle_conditional(bot, message, data, user_states)

@bot.message_handler(func=lambda message: message.text == "🔗 Linking Words")
def handle_ielts_linked_words_wrapper(message):
    handle_ielts_linked_words(bot, message, data, user_states)

#----------------------------------------------------------------------------------------------------------------------------------------

@bot.message_handler(func=lambda message: message.text == "📜 IELTS")
def handle_IELTS(message):

    bot.send_message(
        message.chat.id, "Choose a topic:", reply_markup=create_reply_keyboard(IETLS())
    )
    user_states[message.chat.id] = {"state": "grammar"}
    print(message.chat.id)

@bot.message_handler(func=lambda message: message.text == "🗣️ Speaking Questions")
def handle_questions_IELTS_wrapper(message):
    handle_questions_IELTS(bot, message, data, user_states)

@bot.message_handler(func=lambda message: message.text == "🆕 Daily Word")
def handle_new_vocabulary_wrapper(message):
    handle_day_vocabulary(bot, message, data, user_states)

@bot.message_handler(func=lambda message: message.text == "📜 IELTS Vocabulary")
def handle_ielts_vocabulary_wrapper(message):
    handle_ielts_vocabulary(bot, message, data, user_states)

@bot.message_handler(func=lambda message: message.text == "🎬 Films Vocabulary")
def handle_films_vocabulary_wrapper(message):
    handle_films_vocabulary(bot, message, data, user_states)

@bot.message_handler(func=lambda message: message.text == "📚 Books Vocabulary")
def handle_books_vocabulary_wrapper(message):
    handle_books_vocabulary(bot, message, data, user_states)

    
@bot.message_handler(
    func=lambda message: user_states.get(message.chat.id, {}).get("state")
    in [
        "new_words",
        "past_tense",
        "present_tense",
        "futuro_tense",
        "phrasal_verbs",
        "movies_sentences",
        "audio_exercises",
        "modal_verbs",
        "conditional_setence",
        "ielts_vocabulary",
        "ielts_linked_words",
        "new_vocabulary",
        "ielts_vocabulary",
        "films_vocabulary",
        "books_vocabulary",
        "questions_IELTS"
    ]
)
def check_answer(message):
    state_info = user_states[message.chat.id]
    correct_answer = state_info["phrase_info"]["answer"]

    if message.text.strip().lower() == correct_answer.lower() or message.text.strip().lower() == "next":
        bot.reply_to(message, "Correct! ✅🎉 Moving to the next exercise.")

        if state_info["state"] == "phrasal_verbs":
            handle_phrasal_verbs(bot, message, data, user_states)
        elif state_info["state"] == "movies_sentences":
            handle_movies_sentences(message)
        elif state_info["state"] == "audio_exercises":
            handle_audio_exercises(bot, message, data, user_states)
        elif state_info["state"] == "past_tense":
            handle_past_tense(bot, message, data, user_states)
        elif state_info["state"] == "present_tense":
            handle_present_tense(bot, message, data, user_states)
        elif state_info["state"] == "future_tense":
            handle_future_tense(bot, message, data, user_states)
        elif state_info["state"] == "present_tense":
            handle_audio_exercises(bot, message, data, user_states)
        elif state_info["state"] == "modal_verbs":
            handle_modal_verbs(bot, message, data, user_states)
        elif state_info["state"] == "conditional_setence":
            handle_conditional(bot, message, data, user_states)
        elif state_info["state"] == "ielts_vocabulary":
            handle_ielts_vocabulary(bot, message, data, user_states)
        elif state_info["state"] == "ielts_linked_words":
            handle_ielts_linked_words(bot, message, data, user_states)
        elif state_info["state"] == "new_vocabulary":
            handle_day_vocabulary(bot, message, data, user_states)
        elif state_info["state"] == "ielts_vocabulary":
            handle_ielts_vocabulary(bot, message, data, user_states)
        elif state_info["state"] == "films_vocabulary":
            handle_films_vocabulary(bot, message, data, user_states)
        elif state_info["state"] == "books_vocabulary":
            handle_books_vocabulary(bot, message, data, user_states)
        elif state_info["state"] == "questions_IELTS":
            handle_questions_IELTS(bot, message, data, user_states)

    else:
        bot.reply_to(message, "Wrong, try again.")


@bot.callback_query_handler(func=lambda call: call.data == "show_answer")
def show_answer(call):
    correct_answer = user_states[call.message.chat.id]["phrase_info"]["answer"]
    bot.send_message(call.message.chat.id, f"{correct_answer}")

@bot.callback_query_handler(func=lambda call: call.data == "show_pronunciation")
def show_pronunciation(call):
    correct_pronunciation = user_states[call.message.chat.id]["phrase_info"]["pronunciation"]
    audio_message = bot.send_audio(call.message.chat.id, correct_pronunciation)
    message_id = audio_message.message_id
    time.sleep(25)
    bot.delete_message(call.message.chat.id, message_id)

@bot.callback_query_handler(func=lambda call: call.data == "show_translation")
def show_translation(call):
    translation = user_states[call.message.chat.id]["phrase_info"]["translation"]
    bot.send_message(call.message.chat.id, f"{translation}")

@bot.callback_query_handler(func=lambda call: call.data == "show_why")
def show_why(call):
    why = user_states[call.message.chat.id]["phrase_info"]["why"]
    bot.send_message(call.message.chat.id, f"{why}")



# Mapeo de funciones a días de la semana
daily_functions = [
    handle_daily_vocabulary,  # Enviar verbo
    handle_daily_phrasalVerb,  # Enviar consejo sobre phrasal verbs
    handle_daily_IETLStip,  # Enviar consejo sobre IELTS
    handle_daily_Englishtip,  # Enviar consejo sobre inglés
    handle_daily_verb
]

# Función para enviar un verbo cada hora
def send_verbo_hourly(chat_id):
    handle_daily_verb(chat_id, bot, data)
    # time.sleep(20)
    handle_daily_vocabulary(chat_id, bot, data)

# Función para enviar tips tres veces al día
def send_daily_tips(chat_id, tip_type):
    if tip_type == 1:
        handle_daily_phrasalVerb(chat_id, bot, data)
    elif tip_type == 2:
        handle_daily_IETLStip(chat_id, bot, data)
    elif tip_type == 3:
        handle_daily_Englishtip(chat_id, bot, data)

# Función principal para manejar el envío automático
def auto_message_sender():
    tip_sent_count = 0
    last_tip_time = datetime.now()
    chat_id="7167361570"
    while True:
        # Enviar verbo cada hora
        send_verbo_hourly(chat_id)
        time.sleep(1800)  # Espera 1 hora antes de enviar el siguiente verbo

        # Enviar 3 tips durante el día
        if tip_sent_count < 3 and datetime.now() - last_tip_time >= timedelta(hours=4):
            send_daily_tips(chat_id, tip_sent_count + 1)
            tip_sent_count += 1
            last_tip_time = datetime.now()

        # Reiniciar el contador de tips después de las 24 horas
        if tip_sent_count >= 3 and datetime.now().hour == 0:
            tip_sent_count = 0


def start_polling():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(15)

if __name__ == "__main__":
    data = load_exercise_data()

    # Crear y empezar el hilo para enviar mensajes automáticos
    auto_message_thread = threading.Thread(target=auto_message_sender)
    auto_message_thread.start()

    # Crear y empezar el hilo para el polling del bot
    polling_thread = threading.Thread(target=start_polling)
    polling_thread.start()