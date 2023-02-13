from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name : str
    price : float
    category : Optional[str] = None

@app.get("/")
def home():
    return {"Data" : "Test"}


@app.get("/about")
def about():
    return {"Data" : "About"}

@app.get("/item/{item_id}/{name}")
def get_item(item_id : int = Path(None, description = "The Id of the item you'd like to view")): 
    return inventory[item_id]
    #Path parameter
    # : (type data to push) -> set the parameter to send out # specify the type of data
    # Path() -> add more detail, enforcement, constraints
    # None means if don't send some value, it will be none # Set the default
    
    # Query Parameter
    # Ex. facebook.com/home?reidrect=/

@app.get("/get-by-name")
def get_item(*, item_id : int , test : int, name : Optional[str] = None ):
    for item in inventory:
        if inventory[item]["name"] == name:
            return inventory[item]
    return {"Data":"Not found"}

# Endpoint parameter
inventory = {
    1:{
        "name" : "Pepsi",
        "price" : 1.5,
        "category" : "beverage"
    }
}

@app.post("/create-item/{item_id}")
def create_item(item_id : int, item : Item):
    if item_id in inventory:
        return {"Error" : "Item Id already exists."}

    inventory[item_id] = {"name": item.name, "price" : item.price ,"category" : item.category}