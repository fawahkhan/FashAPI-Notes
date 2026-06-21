from fastapi import FastAPI # import from library
 
app = FastAPI()  #create an object

@app.get("/")
def greet():
    return "Hello World"

