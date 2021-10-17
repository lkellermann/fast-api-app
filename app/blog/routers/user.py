from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from blog import schemas
from blog.database import get_db
from blog.repository import user

router = APIRouter(prefix='/user',
                   tags=['users'])

@router.post('/', response_model=schemas.ShowUser)
def create(request: schemas.User, db: Session=Depends(get_db)):
    return user.create(request, db)

@router.get('/',status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def show(id, db: Session=Depends(get_db)):
    return user.show(id, db) 