import websockets
import asyncio
import json

async def echo(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        response = {"response": "Message received"}
        await websocket.send(json.dumps(response))

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("WebSocket server is running on ws://localhost:8765")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
