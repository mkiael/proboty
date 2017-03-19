# -*- coding: utf-8 -*-


class ConnectionHandler(object):
    def __init__(self, async_q):
        self.async_q = async_q
        
    async def handle(self, websocket, path):
        print("New connection!")
        while True:
            message = await websocket.recv()
            print("Got message", message)
            self.async_q.put_nowait(message)
    
