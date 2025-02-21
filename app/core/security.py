from authx import AuthX, AuthXConfig
from app.core.config import settings

security_config = AuthXConfig(
     JWT_ALGORITHM = "RS256",
     JWT_PRIVATE_KEY= settings.JWT_PRIVATE,
     JWT_PUBLIC_KEY= settings.JWT_PUBLIC,
     JWT_TOKEN_LOCATION = ["headers"],
)

security = AuthX(config=security_config)