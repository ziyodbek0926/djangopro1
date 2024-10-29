from django.urls import path
from .views import send_message, message_history, change_name

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('history/', message_history, name='message_history'),
    path('change-name/', change_name, name='change_name'),
]
