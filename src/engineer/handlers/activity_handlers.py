import json
from engineer.handlers.start_handlers import tech
from engineer.handlers.utils_handlers import create_question_keyboard
from telebot.types import ReplyKeyboardRemove
import random

from english.handlers.start_handlers import welcome
from english.utils.keyboard import create_reply_keyboard



def handle_linuxEssentials(bot, message, data, user_states):
    shuffled_data = data.get("linuxEssentials",{})[:]  # Crear una copia de la lista de preguntas
    random.shuffle(shuffled_data)
    user_states[message.chat.id] = {
        "state": "quiz",
        "current_question": 0,
        "score": 0,
        "user_answers": [],
        "questions": shuffled_data,  # Guardar la lista mezclada
        "index": 0
    }
    send_next_question(bot,message.chat.id,data, user_states)

def send_next_question(bot,chat_id,data, user_states):
    state = user_states.get(chat_id)
    if state:
        current_index = state["current_question"]
        questions = state["questions"]  # Recuperar las preguntas mezcladas
        if current_index < len(questions):
            question_data = questions[current_index]
            bot.send_message(
                chat_id,
                question_data["question"],
                reply_markup=create_question_keyboard(question_data["options"])
            )
        else:
            # Fin del cuestionario
            bot.send_message(
                chat_id,
                f"Quiz completed! Your score: {state['score']}/{len(data)}",
                reply_markup=ReplyKeyboardRemove()
            )
            user_states.pop(chat_id)  # Limpiar estado del usuario

def handle_stop_button(bot, message, data, user_states):
    # Obtener el puntaje del usuario
    score = user_states.get(message.chat.id, {}).get("score", 0)
    index = user_states.get(message.chat.id, {}).get("index", 0)
    # Enviar un mensaje al usuario con emojis
    bot.send_message(
        message.chat.id,
        f"🏆 Your final score is: {score} of {index} 🎉\n"
        "Thank you for participating! 😊",
        reply_markup=create_reply_keyboard(tech()),
    )
    
    # Reiniciar el estado del usuario
    user_states[message.chat.id] = {"state": "none"}

def handle_delete_button(bot, message, data, user_states):
    try:
        # Obtener el ID actual de la pregunta
        question_id = user_states.get(message.chat.id, {}).get("current_question", 0)

                # Cargar datos del archivo JSON
        with open("src/data/LPI/linuxEssentials/data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        
        # Buscar y eliminar la pregunta con el ID
        updated_data = [q for q in data if q.get("id") != question_id]
        
        # Guardar los datos actualizados
        with open("src/data/LPI/linuxEssentials/data.json", "w", encoding="utf-8") as file:
            json.dump(updated_data, file, indent=4, ensure_ascii=False)
        
        # Enviar un mensaje de confirmación al usuario
        bot.send_message(
            message.chat.id,
            f"❌ The question with ID {question_id} has been successfully deleted!",
            reply_markup=create_reply_keyboard(welcome()),
        )
        
        # Reiniciar el estado del usuario
        user_states[message.chat.id] = {"state": "none"}
    
    except Exception as e:
        # Manejar errores
        bot.send_message(
            message.chat.id,
            f"⚠️ An error occurred while deleting the question: {str(e)}",
            reply_markup=create_reply_keyboard(welcome()),
        )