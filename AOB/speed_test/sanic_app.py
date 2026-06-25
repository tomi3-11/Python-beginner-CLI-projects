from sanic import Sanic
from sanic.response import json

app = Sanic("test")

@app.get("/")
async def home(request):
    return json({"status": "ok"})


