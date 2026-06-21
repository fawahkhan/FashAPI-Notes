# used to represent data
# for validation we will use pydanticc
from pydantic import BaseModel 
# now we will just inherit this baseModel and then we wont even need this constructor it will be taken care of itself 
class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    quantity: int

    # # constructor -- not needed now since we are using pydantic now 
    # def __init__(self,id: int, name: str, description: str, price: float, quantity: int ):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity