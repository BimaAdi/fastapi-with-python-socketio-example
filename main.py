import socketio
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.socket_io import sio
from routes.ws_no_prefix import NoPrefixNamespace

app = FastAPI()

sio.register_namespace(NoPrefixNamespace("/"))
sio_asgi_app = socketio.ASGIApp(socketio_server=sio, other_asgi_app=app)

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_route("/socket.io/", route=sio_asgi_app, methods=["GET", "POST"])
app.add_websocket_route("/socket.io/", sio_asgi_app)


@app.get("/hello")
async def root():
    await sio.emit("response", "hello everyone")
    return {"message": "hello"}
