from passlib.context import CryptContext

PWD_CTX = CryptContext(schemes=['bcrypt'], deprecated='auto')

class Hash():
    def bcrypt(password:str):
        return PWD_CTX.hash(password)
        
    def verify(plain_password, hashed_password):
        return PWD_CTX.verify(plain_password, hashed_password)