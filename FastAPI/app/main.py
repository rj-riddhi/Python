from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    title: str
    content: str
    is_published: bool

# root path
@app.get("/")
def root():
    return{"message": "Welcome to my FastAPI"}

# Create Post
@app.post("/posts")
def create_posts():
    return {"data": "Post created sucessfully."}

# Get all posts
@app.get("/posts")
def get_posts():
    return{"data": "This is your posts."}

# Get post by id
@app.get("/posts/{id}")
def post_by_id(id: int):
    return{"data": f"This is post id {id}"}

# Update Post
@app.put("/posts/{id}")
def update_posts(id: int, item: Item):
    return{"data": "Post Updated"}

# Delete post
@app.delete("/posts/{id}")
def delete_posts(id: int):
    return{"data": f"Post deleted"}