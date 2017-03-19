# -*- coding: utf-8 -*-

import asyncio
import janus
import websockets
from proboty.controller import Controller
from proboty.connection_handler import ConnectionHandler

class App(object):
    def __init__(self):
        pass


    def run(self):
        print("Starting proboty...")

        event_loop = asyncio.get_event_loop()
        
        queue = janus.Queue(maxsize=100, loop=event_loop)

        conn_handler = ConnectionHandler(queue.async_q)

        ws_server = websockets.serve(conn_handler.handle, '127.0.0.1', 55777)
        
        controller = Controller(event_loop, queue.sync_q)

        controller.start()

        event_loop.run_until_complete(ws_server)
        
        event_loop.run_forever()
        
        controller.join()

        print("Exiting proboty")
