import time
import json
from threading import Thread
from random import randint

from django.conf import settings

from chat.helpers import connect_with_message_server, send_new_message_to_message_server
from chat.constants import RANDOM_MESSAGE_LIST


class SendMessageThread(Thread):

    def connect_with_server(self):
        connected = False
        retry = 0
        time.sleep(2)
        print("\nConnecting with message server ... ... ...\n")
        while retry < 10000:
            status_code, response = connect_with_message_server()
            if status_code == 200:
                connected = True
                print(f"\nConnected!\nClient List : {json.loads(response)['client_list']}\n")
                break
            elif status_code == 408:
                print("Request Timed Out!\n")
                time.sleep(5)
            elif status_code == 503:
                print("Server is Unavailable!\n")
                time.sleep(5)
            elif status_code == 405:
                print("Method Not Allowed!\n")
                break
            else:
                print("Internal Server Error!\n")
                time.sleep(5)
            retry += 1
        return connected

    def send_message(self):
        print("Sending random message to message server...\n")
        size = len(RANDOM_MESSAGE_LIST) - 1
        repeat_previous_message = False
        retry = 0
        while retry < 10000:
            time.sleep(settings.MESSAGE_SENDING_GAP_IN_SECONDS)
            if not repeat_previous_message:
                message = RANDOM_MESSAGE_LIST[randint(0, size)]["question"]
            print(f"\nSending message : {message}\n")
            status_code, _ = send_new_message_to_message_server(message)
            if status_code != 200:
                repeat_previous_message = True
                retry += 1
            else:
                repeat_previous_message = False
                retry = 0

    def run(self):
        connected = self.connect_with_server()
        if connected:
            self.send_message()
        else:
            print("Could not connect with the message server!\n")
