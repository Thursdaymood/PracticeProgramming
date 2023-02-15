from fastapi import FastAPI, Path, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
# Endpoint parameter
inventory = {
    1:{
        "name" : "Pepsi",
        "price" : 1.5,
        "category" : "beverage"
    }
}

class Item(BaseModel):
    name : str
    price : float
    category : Optional[str] = None

class updateItem(BaseModel):
    name : str = None
    price : float = None
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
def get_item(*, item_id : int , price : float, name : Optional[str] = None ):
    for item in inventory:
        if inventory[item]["name"] == name:
            return inventory[item]
    #return {"Data":"Not found"}
    #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    raise HTTPException(status_code=404, detail ="Item name not found.")


@app.post("/create-item/{item_id}")
def create_item(item_id : int, item : Item):
    if item_id in inventory:
        #return {"Error" : "Item Id already exists."}
        raise HTTPException(status_code=404, detail ="Item ID already exists.")

    inventory[item_id] = {"name": item.name, "price" : item.price ,"category" : item.category}


# Update item
@app.put("/update-item/{item_id}")
def update_item(item_id : int, item: Item):
    if item_id is not inventory:
        #return {"Error" : "Item ID does not already exist."}
        raise HTTPException(status_code=404, detail ="Item does not exist.")
    if item.name != None:
        inventory[item_id].name = item.name # keep the data in dictionary
    
    if item.price != None:
        inventory[item_id].name = item.name # keep the data in dictionary
        
    if item.brand != None:
        inventory[item_id].name = item.name # keep the data in dictionary

    return inventory[item_id]

#Delete item
@app.delete("/delete-item")
def delete_item(item_id : int = Query(..., description="The ID of the item to delete")):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail ="Item name not found.")
    
    del inventory[item_id]
    return {"Success" : "Item delete!"}


#return http code error

