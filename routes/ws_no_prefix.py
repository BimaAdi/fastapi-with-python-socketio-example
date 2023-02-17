import socketio
from core.socket_io import sio


class NoPrefixNamespace(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        print("connect ", sid)

    async def on_message(self, sid, data):
        print("message ", data)
        await sio.emit("response", "hi " + data)

    def on_disconnect(self, sid):
        print("disconnect ", sid)
