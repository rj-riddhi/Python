from fastapi import FastAPI
from .database import Base, engine
from .routes import post, user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
def root():
    return({"message": "Welcome to the Fast API."})


