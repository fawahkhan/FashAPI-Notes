from fastapi import FastAPI # import from library
from models import Product

app = FastAPI()  #create an object

@app.get("/")
def greet():
    return "Hello World"

products = [
    Product(1, "Phone", "budget phone", 99, 10),
    Product(2, "Laptop", "budget laptop", 999, 6)
]

@app.get("/products")
def getallProducts():
    return products

