from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from blog import schemas, oauth2
from blog.database import get_db
from typing import List
from blog.repository import blog

router = APIRouter(prefix='/blog',
        tags=['blogs'])

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.get('/', response_model=List[schemas.ShowBlog])
def all(db: Session=Depends(get_db)):
    return blog.get_all(db)
    
@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id,  db: Session=Depends(get_db)):
    return blog.show(id, db)

    
@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT,)
def destroy_blog(id, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)
    
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id:int, request: schemas.Blog, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)
