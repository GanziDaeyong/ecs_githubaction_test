from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "root"}

@app.get("/hello")
async def hello():
    return "hello"

@app.get("/ping")
async def ping():
    return "pong"
