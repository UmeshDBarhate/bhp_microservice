from channels.generic.websocket import AsyncConsumer
import asyncio
import json
import requests


class YourAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        message = event['text']
        api_url = "http://localhost:8000/bookings/?action=getAllSlots&clinic_id=1&backend=True&date=2024-06-23T18:30:00Zto2024-06-24T18:29:00Z&doctor_id=5&session=True"
        
        response_message = await self.fetch_data(api_url)

        await self.send({
            "type": "websocket.send",
            "text": response_message
        })

    async def fetch_data(self, api_url):
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(None, requests.get, api_url)

        if response.status_code == 200:
            api_response = response.json()  # Assuming the API returns JSON
            response_message = json.dumps(api_response)  # Convert the response to JSON string
        else:
            response_message = f"Error: {response.status_code}"

        return response_message

    async def websocket_disconnect(self, event):
        pass