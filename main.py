from fastapi import Depends, FastAPI # import from library
from models import Product
from database import sessionLocal, engine
import database_models
from sqlalchemy.orm import Session
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
# if anyone wants to use the db he will just inject this method and use the db 
def get_db():
    db = sessionLocal() # to create the connection once
    try:
        yield db # the connection will be closed after you are done with what you wanted to do with the db
    finally:
        db.close() # to close the connection

# now i want to add fresh data into my database . 
def init_db():
    db = sessionLocal()

    # Note : i only want to initialise when my database is completely empty
    count = db.query(database_models.Product).count
    if count == 0:

        for product in products:
            db.add(database_models.Product(**product.model_dump()))  # model dump gives you a dictionary
        db.commit()
init_db( )

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)): #means db of type Session depends upon get_db method.

    # now we can use the db directly since we have injected it into get_all_products.
    db_products = db.query(database_models.Product).all()
    return db_products

@app.get("/product/{id}")
def get_products_by_id(id:int, db: Session = Depends(get_db)):
    # for product in products:
    #     if product.id == id:
    #         return product
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product      
    return "product not found"


# how to add products
@app.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    # products.append(product) -- not needed anymore we will just do db.add
    db.add(database_models.Product(**product.model_dump()))  # model dump gives you a dictionary
    db.commit() # we have to do it while doing any change in a db
    return product

# how to update a product
@app.put("/product{id}")
def update_product(id: int , product: Product, db: Session = Depends(get_db)):
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         products[i] = product
    #         return "Product updated successfully"
    # firstly check if the product exists
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product updated"
    else:
        return "No product found"

@app.delete("/product{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         del products[i]
    #         return "product deleted"
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted"
    else:
        return "product not found"