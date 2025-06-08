
# ====================================
# core/consumers.py
# ====================================
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio
import datetime

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.keep_sending = True
        asyncio.create_task(self.send_periodic_updates())

    async def disconnect(self, close_code):
        self.keep_sending = False

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.send(text_data=json.dumps({
            'response': f"✅ Server received your message: {data.get('message')}"
        }))

    async def send_periodic_updates(self):
        counter = 0
        while self.keep_sending:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            counter += 1
            await self.send(text_data=json.dumps({
                'timestamp': now,
                'count': counter,
                'message': f"📡 Live update #{counter}"
            }))
            await asyncio.sleep(1)

