from fastapi import FastAPI

app = FastAPI(title="Hello")

@app.get("/")
async def home():
    return {"status": "ok"}
