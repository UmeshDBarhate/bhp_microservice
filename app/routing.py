from django.urls import re_path
from .consumer import YourAsyncConsumer

websocket_urlpatterns = [
    re_path(r'ws/app/', YourAsyncConsumer.as_asgi()),
]
