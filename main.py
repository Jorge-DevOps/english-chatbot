import telebot
import time
import threading
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
import json
import random
import openai

# Función para cargar los datos desde archivos JSON
def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

# Cargar todos los datos de ejercicios
def load_exercise_data():
    return {
        "movies_sentences": load_json("dictionaries/movies_sentences.json"),
        "phrasal_verbs": load_json("dictionaries/phrasal_verbs.json"),
        "writing_exercises": load_json("dictionaries/writing_exercises.json"),
        "audio_exercises": load_json("dictionaries/listening/audio_exercises.json"),
        "modal_verbs": load_json("dictionaries/grammar/modalVerbs/modal_verbs.json"),
        "conditional_setence": load_json("dictionaries/grammar/conditional/conditional_setence.json"),
        "ielts_linked_words": load_json("dictionaries/IELTS/ielts_linked_words.json"),
        "ielts_vocabulary": load_json("dictionaries/vocabulary/ielts_vocabulary.json"),
        "ielts_speakingQuestions": load_json("dictionaries/IELTS/ielts_speakingQuestions.json"),
        "new_vocabulary": load_json("dictionaries/vocabulary/new_vocabulary.json"),
        "films_vocabulary": load_json("dictionaries/vocabulary/films_vocabulary.json"),
        "books_vocabulary": load_json("dictionaries/vocabulary/books_vocabulary.json"),
        ### Grammar
        "past_tense": load_json(
            "dictionaries/grammar/timeTense/past_sentences.json"
        ),
        "present_tense": load_json(
            "dictionaries/grammar/timeTense/present_tense.json"
        ),
        "futuro_tense": load_json(
            "dictionaries/grammar/timeTense/future_tense.json"
        ),
        
    }


# Inicializar el bot con el token de Telegram proporcionado
bot = telebot.TeleBot("djaskbgvjlsrz;fodj")

user_states = {}

def create_reply_keyboard(buttons):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for row in buttons:
        markup.row(*[KeyboardButton(button) for button in row])
    return markup

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    buttons = [
        ["▶️ Start", "❌ Cancel"],
        ["🆕 Vocabulary", "📚 Grammar",],
        ["💭 Phrasal Verbs", "📜 IELTS"],
        ["🎬 Movie Exercises", "🎧 Listening Exercises"],
    ]
    bot.send_message(message.chat.id, "👋 Hi, I'm your English Trainer Bot! 😊 I'm here to help you improve your English skills. Let's get started! 🚀📚", reply_markup=create_reply_keyboard(buttons))


@bot.message_handler(func=lambda message: message.text == "❌ Cancel")
def handle_cancel_button(message):
    user_states[message.chat.id] = {"state": "none"}
    buttons = [
        ["▶️ Start", "❌ Cancel"],
        ["🆕 Vocabulary", "📚 Grammar"],
        ["💭 Phrasal Verbs","📜 IELTS"],
        ["🎬 Movie Exercises", "🎧 Listening Exercises"],
    ]
    bot.send_message(message.chat.id, "🌟 It was a pleasure to help you with your English today! 😊📚", reply_markup=create_reply_keyboard(buttons))

    send_welcome(message)

@bot.message_handler(func=lambda message: message.text == "▶️ Start")
def handle_start_button(message):
    send_welcome(message)

#----------------------------------------------------------------------------------------------------------------------------------------

@bot.message_handler(func=lambda message: message.text == "📚 Grammar")
def handle_grammar(message):
    buttons = [
        ["🕰️ Past", "🎁 Present", "🔮 Future"],
        ["🔍 Conditional", "🔄 Passive Voice", "👥 Pronouns"],
        ["🔗 Linking Words", "🗯️ Modal Verbs", "❌ Cancel"],
    ]
    bot.send_message(
        message.chat.id, "Choose a topic:", reply_markup=create_reply_keyboard(buttons)
    )
    user_states[message.chat.id] = {"state": "grammar"}

@bot.message_handler(func=lambda message: message.text == "💭 Phrasal Verbs")
def handle_phrasal_verbs(message):
    phrase_info = random.choice(data["phrasal_verbs"]["phrases"])
    user_states[message.chat.id] = {
        "state": "phrasal_verbs",
        "phrase_info": phrase_info,
    }

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🎬 Movie Exercises")
def handle_movies_sentences(message):
    phrase_info = random.choice(data["movies_sentences"]["phrases"])
    user_states[message.chat.id] = {
        "state": "movies_sentences",
        "phrase_info": phrase_info,
    }

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    print(phrase_info)
    bot.send_video(message.chat.id, phrase_info["video_url"])
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🎧 Listening Exercises")
def handle_audio_exercises(message):
    buttons = [
        [InlineKeyboardButton("📝 Show Answer", callback_data="show_answer")],
        [InlineKeyboardButton("🌐  Show Translation", callback_data="show_translation")]
    ]

    # Crear el markup con los botones
    markup = InlineKeyboardMarkup(buttons)

    # Enviar el mensaje con los botones

    # Escoger una frase aleatoria para el ejercicio
    phrase_info = random.choice(data["audio_exercises"]["phrases"])
    user_states[message.chat.id] = {
        "state": "audio_exercises",
        "phrase_info": phrase_info,
    }

    bot.send_audio(message.chat.id, phrase_info["audio_path"])
    bot.send_message(message.chat.id, "write the previous sentence in English", reply_markup=markup)

#----------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == "🆕 Vocabulary")
def handle_vocabulary(message):
    buttons = [
      ["🆕 Daily Word"],
      ["🎬 Films Vocabulary", "📚 Books Vocabulary"],
      ["❌ Cancel"]
    ]
    bot.send_message(
        message.chat.id, "Choose a topic:", reply_markup=create_reply_keyboard(buttons)
    )
    user_states[message.chat.id] = {"state": "grammar"}

@bot.message_handler(func=lambda message: message.text == "🆕 Daily Word")
def handle_new_vocabulary(message):
    phrase_info = random.choice(data["new_vocabulary"]["phrases"])
    user_states[message.chat.id] = {"state": "new_vocabulary", "phrase_info": phrase_info}
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    markup.add(InlineKeyboardButton("🅰️ Show Spelling", callback_data="show_pronunciation"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "📜 IELTS Vocabulary")
def handle_ielts_vocabulary(message):
    phrase_info = random.choice(data["ielts_vocabulary"]["phrases"])
    user_states[message.chat.id] = {"state": "ielts_vocabulary", "phrase_info": phrase_info}
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    markup.add(InlineKeyboardButton("🌐  Show Translation", callback_data="show_translation"))
    bot.send_audio(message.chat.id, phrase_info["pronunciation"], reply_markup=markup)
    # markup.add(InlineKeyboardButton("🅰️ Show Spelling", callback_data="show_pronunciation"))
    # bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "🎬 Films Vocabulary")
def handle_films_vocabulary(message):
    phrase_info = random.choice(data["films_vocabulary"]["phrases"])
    user_states[message.chat.id] = {"state": "films_vocabulary", "phrase_info": phrase_info}
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    markup.add(InlineKeyboardButton("🅰️ Show Spelling", callback_data="show_pronunciation"))
    markup.add(InlineKeyboardButton("🌐  Show Translation", callback_data="show_translation"))

@bot.message_handler(func=lambda message: message.text == "📚 Books Vocabulary")
def handle_books_vocabulary(message):
    phrase_info = random.choice(data["books_vocabulary"]["phrases"])
    user_states[message.chat.id] = {"state": "books_vocabulary", "phrase_info": phrase_info}
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    markup.add(InlineKeyboardButton("🅰️ Show Spelling", callback_data="show_pronunciation"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

#----------------------------------------------------------------------------------------------------------------------------------------

@bot.message_handler(func=lambda message: message.text == "🕰️ Past")
def handle_past_tense(message):
    phrase_info = random.choice(data["past_tense"]["phrases"])
    user_states[message.chat.id] = {
        "state": "past_tense",
        "phrase_info": phrase_info,
    }

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🎁 Present")
def handle_present_tense(message):
    phrase_info = random.choice(data["present_tense"]["phrases"])
    user_states[message.chat.id] = {
        "state": "present_tense",
        "phrase_info": phrase_info,
    }

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🔮 Future")
def handle_future_tense(message):
    phrase_info = random.choice(data["futuro_tense"]["phrases"])
    user_states[message.chat.id] = {
        "state": "futuro_tense",
        "phrase_info": phrase_info,
    }

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🗯️ Modal Verbs")
def handle_modal_verbs(message):
    phrase_info = random.choice(data["modal_verbs"]["phrases"])
    user_states[message.chat.id] = {
        "state": "modal_verbs",
        "phrase_info": phrase_info,
    }

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "🔍 Conditional")
def handle_conditional(message):
    phrase_info = random.choice(data["conditional_setence"]["phrases"])
    user_states[message.chat.id] = {"state": "conditional_setence", "phrase_info": phrase_info}
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

#----------------------------------------------------------------------------------------------------------------------------------------

@bot.message_handler(func=lambda message: message.text == "📜 IELTS")
def handle_IELTS(message):
    buttons = [
        ["🗃️ Vocabulary", "🗣️ Speaking Questions", "📖 Reading"],
        ["🎧 Listening", "🧠 Tips","❌ Common Mistakes"],
        ["❌ Cancel"]
    ]
    bot.send_message(
        message.chat.id, "Choose a topic:", reply_markup=create_reply_keyboard(buttons)
    )
    user_states[message.chat.id] = {"state": "grammar"}
    print(message.chat.id)


@bot.message_handler(func=lambda message: message.text == "🔗 Linking Words")
def handle_ielts_linked_words(message):
    phrase_info = random.choice(data["ielts_linked_words"]["phrases"])
    user_states[message.chat.id] = {"state": "ielts_linked_words", "phrase_info": phrase_info}
    
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

#----------------------------------------------------------------------------------------------------------------------------------------
@bot.message_handler(func=lambda message: message.text == "🗣️ Speaking Questions")
def handle_questions_IELTS(message):
    phrase_info = random.choice(data["ielts_speakingQuestions"]["phrases"])
    user_states[message.chat.id] = {"state": "ielts_speakingQuestions", "phrase_info": phrase_info}
    
    markup = InlineKeyboardMarkup()
    bot.send_message(message.chat.id, phrase_info["Question"], reply_markup=markup)


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

    if message.text.strip().lower() == correct_answer.lower():
        bot.reply_to(message, "Correct! ✅🎉 Moving to the next exercise.")

        if state_info["state"] == "phrasal_verbs":
            handle_phrasal_verbs(message)
        elif state_info["state"] == "movies_sentences":
            handle_movies_sentences(message)
        elif state_info["state"] == "audio_exercises":
            handle_audio_exercises(message)
        elif state_info["state"] == "past_tense":
            handle_past_tense(message)
        elif state_info["state"] == "present_tense":
            handle_present_tense(message)
        elif state_info["state"] == "future_tense":
            handle_future_tense(message)
        elif state_info["state"] == "present_tense":
            handle_audio_exercises(message)
        elif state_info["state"] == "modal_verbs":
            handle_modal_verbs(message)
        elif state_info["state"] == "conditional_setence":
            handle_conditional(message)
        elif state_info["state"] == "ielts_vocabulary":
            handle_ielts_vocabulary(message)
        elif state_info["state"] == "ielts_linked_words":
            handle_ielts_linked_words(message)
        elif state_info["state"] == "new_vocabulary":
            handle_new_vocabulary(message)
        elif state_info["state"] == "ielts_vocabulary":
            handle_ielts_vocabulary(message)
        elif state_info["state"] == "films_vocabulary":
            handle_films_vocabulary(message)
        elif state_info["state"] == "books_vocabulary":
            handle_books_vocabulary(message)
        elif state_info["state"] == "questions_IELTS":
            handle_questions_IELTS(message)

    else:
        bot.reply_to(message, "Wrong, try again.")


@bot.callback_query_handler(func=lambda call: call.data == "show_answer")
def show_answer(call):
    correct_answer = user_states[call.message.chat.id]["phrase_info"]["answer"]
    bot.send_message(call.message.chat.id, f"{correct_answer}")

@bot.callback_query_handler(func=lambda call: call.data == "show_pronunciation")
def show_pronunciation(call):
    correct_pronunciation = user_states[call.message.chat.id]["phrase_info"]["pronunciation"]
    bot.send_audio(call.message.chat.id, f"{correct_pronunciation}")

@bot.callback_query_handler(func=lambda call: call.data == "show_translation")
def show_translation(call):
    translation = user_states[call.message.chat.id]["phrase_info"]["translation"]
    bot.send_message(call.message.chat.id, f"{translation}")



# Función para enviar un mensaje automáticamente
def send_auto_message(chat_id, text):
    bot.send_message(chat_id, text)

# Obtener el chat_id del usuario al que deseas enviar el mensaje automáticamente
CHAT_ID = '7167361570'
# Mensaje que deseas enviar automáticamente
message_text = "Este es un mensaje automático."

# Intervalo de tiempo en segundos (por ejemplo, 60 segundos)
interval = 3600

# Función para enviar mensajes automáticos en un hilo separado
def auto_message_sender():
    while True:
        send_auto_message(CHAT_ID, message_text)
        time.sleep(interval)

# Función para manejar el polling del bot en un hilo separado
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
