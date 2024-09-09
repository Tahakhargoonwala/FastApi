import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# JWT settings
JWT_SECRET = os.getenv("JWT_SECRET", "your-secret-key")  # Use environment variable or default
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")      # Default to HS256
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload  # Returns the payload if the token is valid
    except jwt.ExpiredSignatureError:
        # Token has expired
        print("Token has expired")
        return None
    except jwt.InvalidTokenError:
        # Token is invalid
        print("Invalid token")
        return None
