import os
from django.apps import AppConfig
from chat.send_message_thread import SendMessageThread


class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'

    def ready(self):
        if os.environ.get('RUN_MAIN', None) != 'true':
            SendMessageThread(daemon=True).start()
