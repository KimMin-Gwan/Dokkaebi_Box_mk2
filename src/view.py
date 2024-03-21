from fastapi import FastAPI
import uvicorn
import controller



app = FastAPI()

@app.get('/{item}')
def home(item:str):
    print(item)
    test = controller.Data_Add_Controller()
    data = test.get_data()
    print(data)
    str_data = str(data)
    return str_data


uvicorn.run(app=app, host="127.0.0.1", port=5000)