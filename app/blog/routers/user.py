from fastapi import APIRouter, Depends
from blog import schemas, database
from sqlalchemy.orm import Session
from blog.repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create(request, db)


@router.get('/{user_id}', response_model=schemas.ShowUser)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return user.get(user_id, db)
