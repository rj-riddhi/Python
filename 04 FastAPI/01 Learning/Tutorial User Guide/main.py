from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root_path():
    print("Welcome to the world!!")
    return {"message": "Hello World"}

# Path parameters
@app.get("/items/{item_id}")
def get_item(item_id):
    return {"item_id": item_id}

# Path parameters using typehints to validate input
@app.get("/items/type_hint/{item_id}")
def get_typed_item(item_id: int):
    return {"item_id": item_id}