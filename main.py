from fastapi import FastAPI # import from library
from models import Product
from database import sessionLocal, engine
import database_models
app = FastAPI()  #create an object

database_models.Base.metadata.create_all(bind = engine)

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
def get_all_products():

    db = sessionLocal()
    db.query()
    return products

@app.get("/product/{id}")
def get_products_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
        

    return "product not found"


# how to add products
@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product

# how to update a product
@app.put("/product")
def update_product(id: int , product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product updated successfully"
        
    return "No product found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted"

    return "product not found"