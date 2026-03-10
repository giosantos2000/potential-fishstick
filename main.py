from fastapi import FastAPI

app = FastAPI()

# 127.0.0.1:60290
@app.get("/")
async def root():
    return {"message": "Hello World"}

#127.0.0.1:60290/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": "deu certo"}
