import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

def main():
    uvicorn.run("docz_backend:app", host="0.0.0.0", port=5000)