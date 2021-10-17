from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from blog.routers import token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") # Token URL is the rout we are using to authenticate.

async def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    return token.verify_token(data, credentials_exception)
