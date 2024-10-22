import threading
import time

import websockets
import asyncio
import json
import cards, players, philosophers, effects
import fields
import logging
import sys
import queue

# 加载配置文件
with open("configuration.cfg", "r") as config_file:
    config = json.load(config_file)
    port = config.get("port", 11001)  # 默认端口11001如果没有

Field = fields.getField()


async def handle_client(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        response = {"response": "Message received"}
        await websocket.send(json.dumps(response))


def Admin():
    print("Admin console started. Type 'exit' to quit.")
    command_queue = queue.Queue()

    def read_commands():
        while True:
            command = command_queue.get()
            if command == 'exit':
                break
            try:
                exec(command)
            except Exception as e:
                print(f"Error executing command: {e}")
            command_queue.task_done()

    def write_commands():
        while True:
            time.sleep(0.05)
            command = input("Admin> ")
            command_queue.put(command)
            if command == 'exit':
                break

    read_thread = threading.Thread(target=read_commands)
    write_thread = threading.Thread(target=write_commands)

    read_thread.start()
    write_thread.start()


async def Judge():
    print("Game is running...")
    while Field.state == 1:
        # Perform game logic here
        await asyncio.sleep(1)  # Sleep for a short period to avoid busy waiting

    print("Game is over.")


async def main(port):
    # 同时运行WebSocket服务器和Judge函数
    server = await websockets.serve(handle_client, "0.0.0.0", port)

    judge_task = asyncio.create_task(Judge())
    Admin()

    # 等待服务器关闭和Judge函数完成
    await asyncio.gather(server.wait_closed(), judge_task)


if __name__ == "__main__":
    asyncio.run(main(port=port))
