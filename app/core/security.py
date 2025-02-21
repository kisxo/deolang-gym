from authx import AuthX, AuthXConfig
from app.core.config import settings
import bcrypt

security_config = AuthXConfig(
     JWT_ALGORITHM = "RS256",
     JWT_PRIVATE_KEY= settings.JWT_PRIVATE,
     JWT_PUBLIC_KEY= settings.JWT_PUBLIC,
     JWT_TOKEN_LOCATION = ["headers"],
)

security = AuthX(config=security_config)

# Hash a password using bcrypt
def hash_password(password) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password.decode('utf-8')

# Check if the provided password matches the stored hashed_password
def verify_password(plain_password, hashed_password) -> bool:
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password_byte_enc = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password = password_byte_enc , hashed_password = hashed_password_byte_enc)