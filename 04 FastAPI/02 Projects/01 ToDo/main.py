from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pdb

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False


# Get Todos
@app.get("/todos", response_model=List[Todo])
def get_todos():
    return todos


# Create Todo
@app.post("/todo", response_model=Todo)
def add_todo(todo: Todo):
    if any(t.id == todo.id for t in todos):
        raise HTTPException(status_code = 400, detail =  "Todo with same id is already exist")
    todos.append(todo)
    return todo

# Delete Todo
@app.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    todo = next((todo for todo in todos if todo.id == todo_id), None)
    pdb.set_trace()
    if todo == None:
        raise HTTPException(status_code = 404, detail = "Todo not found!!")
    todos.remove([todo])
    return {"message": "Todo deleted"}
