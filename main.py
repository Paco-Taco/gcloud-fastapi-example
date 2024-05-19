from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Hello World!"
    }
    
@app.get("/whoareyou")
def whoami():
    return {
        "message": "I'm an API bro"
    }