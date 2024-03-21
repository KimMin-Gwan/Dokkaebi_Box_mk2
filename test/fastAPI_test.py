from fastapi import FastAPI
import uvicorn

import numpy

numpy.random()

app = FastAPI()

@app.get('/{item}')
def home(item:str):
    print(item)
    print("get data")
    return "hello server"


uvicorn.run(app=app, host="127.0.0.1", port=5000)


