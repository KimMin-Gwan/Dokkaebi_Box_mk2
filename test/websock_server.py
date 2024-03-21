import asyncio
import websockets
import time
import threading

PORT = 5555

global_message = [""]



async def handler(websocket):
    try:
        while True:
            message = await websocket.recv()
            
            global_message[0] = message


            print(f"Received: {message}")
            await websocket.send("Hello from server")
        
    except asyncio.CancelledError:
        print("Connection dropped! 3")

    except websockets.exceptions.ConnectionClosedOK:
        print("connection error 3")

    finally:
        print("socket close 3")


def start_server(loop, task):

    try:
        loop.run_until_complete(task)
        loop.run_forever()
    except KeyboardInterrupt:
        print("Got Signal: SIGINT 2")
    except asyncio.CancelledError:
        print("Connection dropped! 2")
    except websockets.exceptions.ConnectionClosedOK:
        print("connection error 2 ")

async def main():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        server = websockets.serve(handler, "", PORT)

        server_thread = threading.Thread(target=start_server, args=(loop, server))
        print("Server Started")
        server_thread.start()

        while True:
            if global_message[0] == 'q':
                tasks = asyncio.all_tasks(loop=loop)
                for t in tasks:
                    t.cancel()
                futures = asyncio.gather(*tasks, return_exceptions=True)
                await futures  # await here

                loop.close()
                while loop.is_closed():
                    print("Wait.. ")
                
                print("close")
                break

    except KeyboardInterrupt:
        print("Got Signal: SIGINT 1")
    except asyncio.CancelledError:
        print("Connection dropped! 1")
        if global_message[0] == 'q':
            loop.close()
            while loop.is_closed():
                print("Closing... Wait.. ")
            
            print("system going close")
    except websockets.exceptions.ConnectionClosedOK:
        print("connection error 1")
    finally:
        print("System out")

if __name__ == "__main__":
    asyncio.run(main())

