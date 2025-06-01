from fastapi import APIRouter, Depends, HTTPException, status, Response
from typing import List
from .. import models, schemas, database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/posts',
    tags = ['Posts']
)
def get_post(id: int, db: Session):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    return [post, post_query]

# Get Post
@router.get("/", response_model = List[schemas.Post], status_code=status.HTTP_200_OK)
def get_posts(db: Session = Depends(database.get_db)):
    posts = db.query(models.Post)
    return posts

@router.get("/{id}", response_model = schemas.Post, status_code=status.HTTP_200_OK)
def show_post(id: int, db: Session = Depends(database.get_db)):
    post, _ = get_post(id, db)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return post

# Create post
@router.post("/", response_model = schemas.Post, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db)):
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Delete post
@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(database.get_db)):
    post, _ = get_post(id, db)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    
    db.delete(post, synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# Update post
@router.put("/{id}", response_model = schemas.Post, status_code = status.HTTP_200_OK)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(database.get_db)):
    post, post_query = get_post(id, db)
    print(updated_post.dict())
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post

