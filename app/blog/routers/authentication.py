from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from blog import database, models
from sqlalchemy.orm import Session
from blog.hashing import Hash
from . import token
router = APIRouter(prefix='/login',tags=['authentication'])

@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session=Depends(database.get_db)):
    email=db.query(models.User).filter(models.User.email==request.username).first()
    
    if not email:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid email or password.")
        
    if not Hash.verify(request.password, email.password):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid email or password.")
        
    access_token = token.create_access_token(
        data={"sub": email.email},
    )
    return {"status":"sucess", "access_token": access_token, "token_type": "bearer"}