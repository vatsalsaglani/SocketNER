import os
from typing import List, Dict, Union
from fastapi import FastAPI, Header, WebSocket, WebSocketDisconnect
import uvicorn
from config import MODEL_PATH
from predict import NERPredictor

print("LIST DIR: ", os.listdir("./"))
print("LIST DIR: ", os.listdir("./bert-base-NER"))
print("MP: ", MODEL_PATH.path)

app = FastAPI()


# connection manager example from fast api doc
# (https://fastapi.tiangolo.com/advanced/websockets/#handling-disconnections-and-multiple-clients)
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, data: Union[List[Dict], Dict, List],
                                    websocket: WebSocket):
        await websocket.send_json(data)


manager = ConnectionManager()

pred_obj = NERPredictor(MODEL_PATH.path)


@app.get("/health")
async def health():
    return {"ok": True}


@app.websocket("/ws/get-entities")
async def ws_get_entities(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # print(f"RECEIVED: {data}")
            result = pred_obj.predict_result(data)
            # print(f"RESULT: {result}")
            await manager.send_personal_message(result, websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)


if __name__ == "__main__":
    uvicorn.run(app, port=5010, host="0.0.0.0")