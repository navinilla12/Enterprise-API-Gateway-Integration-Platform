
from datetime import datetime, timedelta

from jose import jwt

from passlib.context import CryptContext



SECRET_KEY = "enterprise-secret-key"

ALGORITHM = "HS256"



pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)



def hash_password(password):

    return pwd_context.hash(password)




def verify_password(
    plain_password,
    hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )




def create_token(data):

    payload = data.copy()


    expire = (
        datetime.utcnow()
        +
        timedelta(minutes=60)
    )


    payload["exp"] = expire


    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )
