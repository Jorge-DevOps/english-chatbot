from engineer.handlers.start_handlers import tech
from engineer.handlers.activity_handlers import handle_delete_button, handle_linuxEssentials, handle_stop_button


text_responses_engineer = {
    "🛠️ Engineer": {"response": "Choose one topic 📚","state": "tech","keyboard": tech,},
}

engineer_to_handler = {
    "🐧 Linux Essentials":handle_linuxEssentials ,
    "🛑 Stop":handle_stop_button,
    "🗑️ Delete":handle_delete_button,
    # "🛠️ Terraform":handle_Terraform ,
    # "☁️ AWS":handle_AWS ,
    # "🐧 LPI LPIC-1":handle_ ,
    # "🚢 Kubernetes":handle_Kubernetes ,
    # "🌐 Networking":handle_Networking ,
    # "🐍 Python":handle_Python ,
}




