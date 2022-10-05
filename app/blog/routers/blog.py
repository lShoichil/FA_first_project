from typing import List
from fastapi import APIRouter, Depends, status
from blog import schemas, database, oauth2
from sqlalchemy.orm import Session
from blog.repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
get_db = database.get_db


@router.get("/", response_model=List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db),
              current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)


@router.get("/{blog_id}", status_code=200,
            response_model=schemas.ShowBlog)
def show_blog(blog_id, db: Session = Depends(get_db),
              current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(blog_id, db)


@router.delete('/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(blog_id, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(blog_id, db)


@router.put('/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(blog_id, request: schemas.Blog, db: Session = Depends(get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(blog_id, request, db)
