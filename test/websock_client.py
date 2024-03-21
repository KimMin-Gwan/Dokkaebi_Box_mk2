import asyncio
import websockets

async def client():
    uri = "ws://127.0.0.1:5555"

    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello from client")
        response = await websocket.recv()
        print(f"Received: {response}")

asyncio.get_event_loop().run_until_complete(client())