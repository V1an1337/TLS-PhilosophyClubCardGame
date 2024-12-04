import websockets
import asyncio
import tkinter as tk
import json

def decodeInfo(response):
    round = response["round"]
    print(f"-----currentRound = {round}-----\n")
    players = response["players"]
    for p in players:
        name = p["name"]
        cardPile = p["cardPile"]
        validCardPile = p["validCardPile"]
        print(f"Player {name} has cardPile:\n{cardPile},\nwith validCards: {validCardPile}")
        philosophers = p["philosophers"]
        print(f"Player {name} has philosophers: {philosophers}")
        for ph in philosophers:
            phil = philosophers[ph]
            print(f"Philosopher {ph} has hp: {phil['hp']}\nenergyCards: {phil['energyCards']}\nvalidEnergyCards: {phil['validEnergyCards']}")
        print()
    print(f"-----currentRound = {round}-----\n")
async def main():
    async with websockets.connect('ws://localhost:11001') as websocket:
        while True:
            await websocket.send(json.dumps({"getInfo":"getInfo"}))
            print("sent")
            response = await websocket.recv()
            print("received")
            response = json.loads(response)
            decodeInfo(response)
            input()

# start the server
asyncio.get_event_loop().run_until_complete(main())
# start the GUI
root = tk.Tk()
root.mainloop()
# close the server
asyncio.get_event_loop().close()