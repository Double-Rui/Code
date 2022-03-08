from channels.routing import ProtocolTypeRouter,URLRouter
from chats.urls import websocket_url

application=ProtocolTypeRouter({
    "websocket":URLRouter(
        websocket_url
    )
})