from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import time


def handle_phrasal_verbs(bot, message, data, user_states):
    phrase_info = random.choice(data["phrasal_verbs"]["phrases"])
    user_states[message.chat.id] = {
        "state": "phrasal_verbs",
        "phrase_info": phrase_info,
    }

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

def handle_movies_sentences(bot, message, data, user_states):
    phrase_info = random.choice(data["movies_sentences"]["phrases"])
    user_states[message.chat.id] = {
        "state": "movies_sentences",
        "phrase_info": phrase_info,
    }

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("📝 Show Answer", callback_data="show_answer"))
    bot.send_video(message.chat.id, phrase_info["video_url"])
    bot.send_message(message.chat.id, phrase_info["translation"], reply_markup=markup)

def handle_audio_exercises(bot, message, data, user_states):
    # Definir los botones para mostrar respuesta y traducción
    buttons = [
        [InlineKeyboardButton("📝 Show Answer", callback_data="show_answer")],
        [InlineKeyboardButton("🌐 Show Translation", callback_data="show_translation")]
    ]
    markup = InlineKeyboardMarkup(buttons)
    phrase_info = random.choice(data["audio_exercises"]["phrases"])
    user_states[message.chat.id] = {
        "state": "audio_exercises",
        "phrase_info": phrase_info,
    }
    audio_message = bot.send_audio(message.chat.id, phrase_info["audio_path"])
    message_id = audio_message.message_id
    bot.send_message(message.chat.id, "Write the previous sentence in English", reply_markup=markup)
    time.sleep(10)
    bot.delete_message(message.chat.id, message_id)

def handle_podcast_exercises(bot, message, data, user_states=None):
    # Definir los botones para mostrar respuesta y traducción
    phrase_info = random.choice(data["podcast_exercises"]["phrases"])
    
    # Si user_states es proporcionado, almacena el estado y la frase seleccionada
    if user_states is not None:
        user_states[message.chat.id] = {
            "state": "podcast_exercises",
            "phrase_info": phrase_info,
        }
    
    txt = f"🎙️ New Podcast: {phrase_info['title']}\n" \
          f"🌐 Download Transcription: [here]({phrase_info['pdf']})"
    
    # Enviar el mensaje con el modo Markdown para el hipervínculo
    bot.send_message(message.chat.id, txt, parse_mode="Markdown")
    
    # Enviar el audio relacionado
    audio_message = bot.send_audio(message.chat.id, phrase_info["audio_path"])
    
    # Guardar el ID del mensaje de audio enviado
    message_id = audio_message.message_id
    
    # Esperar una hora antes de borrar el mensaje de audio
    time.sleep(3600)
    bot.delete_message(message.chat.id, message_id)

