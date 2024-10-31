# test for websocket communication

import asyncio
import websockets
import json


async def connect_and_send(uri, message):
    async with websockets.connect(uri) as websocket:
        print(f"Connected to server at {uri}")

        # Send message to the server
        await websocket.send(json.dumps(message))
        print(f"Sent message: {message}")

        # Wait for a response from the server
        response = await websocket.recv()
        print(f"Received response: {response}")


async def main():
    # Set the WebSocket server URI based on the server's configuration
    uri = "ws://localhost:11001"  # Adjust if the server is on a different host or port

    # Define a message to send
    message = {"admin": "start_game"}

    # Connect and send message
    await connect_and_send(uri, message)


# Run the client
if __name__ == "__main__":
    asyncio.run(main())
