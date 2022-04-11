from django.urls import path

from chat.views import pong, new_message, reply_message

urlpatterns = [
    path('ping/', pong, name="pong"),
    path('new-message/', new_message, name="new_message"),
    path('reply-message/', reply_message, name="reply_message"),
]
