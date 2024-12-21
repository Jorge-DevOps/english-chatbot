
# # Mapeo de funciones a días de la semana
# daily_functions = [
#     handle_daily_vocabulary,  # Enviar verbo
#     handle_daily_phrasalVerb,  # Enviar consejo sobre phrasal verbs
#     handle_daily_IETLStip,  # Enviar consejo sobre IELTS
#     handle_daily_Englishtip,  # Enviar consejo sobre inglés
#     handle_daily_verb
# ]

# # Función para enviar un verbo cada hora
# def send_verbo_hourly(chat_id):
#     handle_daily_verb(chat_id, bot, data)
#     # time.sleep(20)
#     handle_daily_vocabulary(chat_id, bot, data)

# # Función para enviar tips tres veces al día
# def send_daily_tips(chat_id, tip_type):
#     if tip_type == 1:
#         handle_daily_phrasalVerb(chat_id, bot, data)
#     elif tip_type == 2:
#         handle_daily_IETLStip(chat_id, bot, data)
#     elif tip_type == 3:
#         handle_daily_Englishtip(chat_id, bot, data)

# # # Función principal para manejar el envío automático
# # def auto_message_sender():
# #     tip_sent_count = 0
# #     last_tip_time = datetime.now()
# #     chat_id="7167361570"
# #     while True:
# #         # Enviar verbo cada hora
# #         send_verbo_hourly(chat_id)
# #         time.sleep(1800)  # Espera 1 hora antes de enviar el siguiente verbo

# #         # Enviar 3 tips durante el día
# #         if tip_sent_count < 3 and datetime.now() - last_tip_time >= timedelta(hours=4):
# #             send_daily_tips(chat_id, tip_sent_count + 1)
# #             tip_sent_count += 1
# #             last_tip_time = datetime.now()

# #         # Reiniciar el contador de tips después de las 24 horas
# #         if tip_sent_count >= 3 and datetime.now().hour == 0:
# #             tip_sent_count = 0




# if __name__ == "__main__":
#     data = load_exercise_data()
#     bot.polling(none_stop=True)

# #     # # Crear y empezar el hilo para enviar mensajes automáticos
# #     # # auto_message_thread = threading.Thread(target=auto_message_sender)
# #     # # auto_message_thread.start()

# #     # # Crear y empezar el hilo para el polling del bot
# #     # polling_thread = threading.Thread(target=start_polling)
# #     # polling_thread.start()
# # def start_polling():
# #     while True:
# #         try:
# #             bot.polling(none_stop=True)
# #         except Exception as e:
# #             print(f"Error: {e}")
# #             time.sleep(15)