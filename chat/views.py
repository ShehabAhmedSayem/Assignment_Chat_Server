from inputimeout import inputimeout, TimeoutOccurred

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from chat.constants import RANDOM_MESSAGE_LIST


@csrf_exempt
def pong(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'OK'}, status=200)


@csrf_exempt
def new_message(request):
    if request.method == 'POST':
        message = request.POST.get('message', None)
        sender_client_address = request.POST.get('sender_client_address', None)
        for m in RANDOM_MESSAGE_LIST:
            if m["question"] == message:
                reply = m["reply"]
                break
        print(f"\nNew message : \nFrom : {sender_client_address}\nMessage: {message}\n")
        if not settings.AUTO_REPLY:
            try:
                reply = inputimeout("Please send a reply: ", timeout=9)
            except TimeoutOccurred:
                print(f"Timeout! Sending default reply: {reply}\n")
        return JsonResponse({'reply': reply}, status=200)


@csrf_exempt
def reply_message(request):
    if request.method == 'POST':
        message = request.POST.get('message', None)
        reply = request.POST.get('reply', None)
        sender_client_address = request.POST.get('sender_client_address', None)
        print(f"\nReply : \nFrom: {sender_client_address}\nMessage : {message}\nReply : {reply}\n")
        return JsonResponse({'message': 'OK'}, status=200)
