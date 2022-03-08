import json
from channels.generic.websocket import WebsocketConsumer
user_dict ={}
list = []

# 这里除了 WebsocketConsumer 之外还有
# JsonWebsocketConsumer
# AsyncWebsocketConsumer
# AsyncJsonWebsocketConsumer
# WebsocketConsumer 与 JsonWebsocketConsumer 就是多了一个可以自动处理JSON的方法
# AsyncWebsocketConsumer 与 AsyncJsonWebsocketConsumer 也是多了一个JSON的方法
# AsyncWebsocketConsumer 与 WebsocketConsumer 才是重点
# 看名称似乎理解并不难 Async 无非就是异步带有 async / await
# 是的理解并没有错,但对与我们来说他们唯一不一样的地方,可能就是名字的长短了,用法是一模一样的
# 最夸张的是,基类是同一个,而且这个基类的方法也是Async异步的

class ChatService(WebsocketConsumer):
    # 当Websocket创建连接时
    def connect(self):
        self.accept()
        username = self.scope.get("url_route").get("kwargs").get("username")
        user_dict[username] = self
        print(user_dict)

    # 当Websocket接收到消息时
    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        print(data)
        to_user = data.get("to_user")
        message = data.get("message")

        ws = user_dict.get(to_user)
        print(to_user)
        print(message)
        print(ws)
        ws.send(text_data)

    # 当Websocket发生断开连接时
    def disconnect(self, code):
        pass
