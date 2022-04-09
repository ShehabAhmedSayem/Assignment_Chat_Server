from django.urls import path

from chat.views import new_message, reply_message

urlpatterns = [
    path('new-message/', new_message, name="new_message"),
    path('reply-message/', reply_message, name="reply_message"),
]
