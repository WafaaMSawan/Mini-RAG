from fastapi import FastAPI
app = FastAPI()

@app.get("/welcome") #app.type of reqest(name of request) يعني لو حد كتبه هينفذ ال func
def welcome():
    return{
        "message":"Hello Digilians!"
    }