import threading
import time
import websockets
import asyncio
import json
import cards, players, philosophers, effects
import fields
import logging
import queue

# 加载配置文件
with open("configuration.cfg", "r") as config_file:
    config = json.load(config_file)
    port = config.get("port", 11001)  # 默认端口11001如果没有

Field = fields.getField()


def handle_request(message, addr):
    message = json.loads(message)

    response = {"response": "Message received"}

    if "admin" in message:
        if message["admin"] == "start_game":  # setting up
            start_game_result, content = Field.startGame()
            if start_game_result:
                response = {"response": "Game started"}
            else:
                response = {"response": "Failed", "reason": content}
        if message["admin"] == "add_player":
            name = message["name"]
            add_player_result, content = Field.addPlayer(name)
            if add_player_result:
                response = {"response": "Player added", "player": content}
            else:
                response = {"response": "Failed", "reason": content}

    print(f"response to {addr}: {response}")
    return response


async def handle_client(websocket, path):
    async for message in websocket:
        addr = websocket.remote_address
        print(f"Received message: {message} from {addr}")
        response = handle_request(message, addr)
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
        print(f"Admin terminal closed.")

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


def startGameUnitTest():
    result, player1_id = Field.addPlayer("player1")
    result, player2_id = Field.addPlayer("player2")

    player1 = Field.getPlayer(player1_id)
    player2 = Field.getPlayer(player2_id)

    player1.addPhilosopher(philosophers.testPhilosopher)
    player2.addPhilosopher(philosophers.testPhilosopher)

    Field.startGame()


async def Judge():
    print("Game is running...")

    print("Game is waiting to start...")
    while Field.state == 0:  # setup
        """
        玩家连接服务器
        玩家选择哲学家
        玩家选择卡组
        初始化哲学家，卡组
        """
        startGameUnitTest()
        await asyncio.sleep(1)

    print("Game started")
    while Field.state == 1:
        """
        遍历players, 选出currentPlayer作为出牌者 -> 一个player的出牌回合视为一回合
        
        # 待更新：伤害结算，装备结算
        
        使用结算前：
        选择目标时 - 五秒内等待出牌者选定要出的牌，以及选定牌的对象，返回Card id，以及target id(playerID)，接着检测选定的牌是否合法（是否符合能量卡消耗要求，目标是否合法），若合法，则进入“使用时”，若非，则继续等待
        使用时 - 消耗对应能量，Card进入处理区
        指定目标时 - ？？不明确
        成为目标时 - 当target具备响应的权力时（e.g 转移目标），target可以响应此牌，若响应，则进入"new target-成为目标时“，若非，则进入”指定目标后“
        指定目标后 - target无法再被更改
        成为目标后 - 当target具备响应的权力时（e.g 无懈可击），target可以响应此牌，若响应，则进入”target-选择目标时“，若非，则进入”处理区“
        
        使用结算时：此时，所有牌不可被响应
        使用结算开始 - 遵循First in last out原则，从后往前遍历“处理区”中的卡牌
        使用结算开始 - 检测对目标有效性，若无效，则跳过(e.g 遍历顺序为 “闪躲” -> “攻击”，则“闪躲”有效，“攻击”无效)
        使用结算 - 卡牌对应效果在此时结算
        使用结算结束 - ？？不明确
        
        使用结算后：
        使用结算后 - 若使用的卡牌为新的有效装备牌，则进入装备区，否则从处理区移除，进入“墓地”
        
        状态结算：
        状态结算开始 - 遍历玩家的哲学家们，并检测他们Effects合法性，若非则移除
        状态结算 - Effects对应效果在此时更新
        状态结算结束 - 未定义
        
        """
        await asyncio.sleep(1)  # Sleep for a short period to avoid busy waiting

    print("Game is over.")
    server.close()
    print("Server closed")


async def main(port):
    global server
    # 同时运行WebSocket服务器和Judge函数
    address = "0.0.0.0"
    server = await websockets.serve(handle_client, "localhost", port)

    judge_task = asyncio.create_task(Judge())
    Admin()

    # 等待服务器关闭和Judge函数完成
    await asyncio.gather(server.wait_closed(), judge_task)


if __name__ == "__main__":
    asyncio.run(main(port=port))
