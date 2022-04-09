import requests

from django.conf import settings


def send_request_to_message_server(url, data=None, timeout=5):
    status_code = 200
    response_text = ''
    try:
        headers = {'Client-Port': settings.CHAT_SERVER_PORT}
        if data:
            r = requests.post(url=url, data=data, timeout=timeout, headers=headers)
        else:
            r = requests.get(url=url, timeout=timeout, headers=headers)
        status_code = r.status_code
        response_text = r.text
    except requests.exceptions.Timeout:
        status_code = 408
    except requests.exceptions.ConnectionError:
        status_code = 503
    except Exception as e:
        status_code = 500
    return status_code, response_text


def connect_with_message_server():
    url = "http://" + settings.MESSAGE_SERVER_IP + "/connect/"
    return send_request_to_message_server(url, timeout=5)


def send_new_message_to_message_server(message):
    url = "http://" + settings.MESSAGE_SERVER_IP + "/incoming-message/"
    data = {'message': message}
    return send_request_to_message_server(url, data=data, timeout=5)
