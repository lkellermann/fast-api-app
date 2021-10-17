from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from blog import schemas, models
from blog.database import get_db
from blog.hashing import Hash

def create(request: schemas.User, db: Session=Depends(get_db)):
    hashed_password = Hash.bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id, db: Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"User ID {id} is not available YET.")
    else:
        return user