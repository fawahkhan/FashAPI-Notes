from fastapi import FastAPI # import from library
from models import Product

app = FastAPI()  #create an object

@app.get("/")
def greet():
    return "Hello World"

products = [
    Product(id= 1, name= "Phone", description= "budget phone", price= 99, quantity= 10),
    Product(id= 2, name= "laptop", description= "laptop", price= 999, quantity= 20),
    Product(id= 3, name= "pen", description= "budget pen", price= 9, quantity= 100),
    Product(id= 4, name= "table", description= "best table", price= 100, quantity= 20)
]

@app.get("/products")
def getallProducts():
    return products

@app.get("/product/{id}")
def get_products_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
        

    return "product not found"