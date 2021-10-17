from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..import schemas, models
from ..database import get_db

def get_all(db: Session):
    return db.query(models.Blog).all() 


def create(request: schemas.Blog, db: Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id,  db: Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with ID {id} is not available YET.")
    else:
        return blog
    
def destroy(id, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} is not available")
    
    blog.delete(synchronize_session=False)
    db.commit()
    return {
            "status": f"Finish with status code {status.HTTP_404_NOT_FOUND}"
        }

def update(id:int, request: schemas.Blog, db: Session=Depends(get_db)):
    request = request.dict()
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"Blog with ID {id} is not available")
    
    blog.update(request, synchronize_session=False)
    db.commit()
    return request