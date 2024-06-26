# from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class WebSocketTestView(APIView):
    def get(self, request):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'test_group',  # Group name
            {
                'type': 'websocket.send',
                'text': 'Hello from WebSocket!'
            }
        )
        return Response({"message": "WebSocket message sent."})