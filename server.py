# -*- coding: UTF-8 -*-
import asyncio
import websockets

async def accept(websocket, path):
    while True:
        data = await websocket.recv();
        print("receive : " + data); 
        await websocket.send(data); 
		
# 웹 소켓 서버 생성
start_server = websockets.serve(accept, "0.0.0.0", 8002);

# 비동기로 서버를 대기한다.
asyncio.get_event_loop().run_until_complete(start_server);
asyncio.get_event_loop().run_forever();
