from django.urls import path
from chats.chatService import ChatService
websocket_url = [
    path("ws/",ChatService)
]
