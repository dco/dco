from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Awesome API"
    admin_email: str = "a@b.c"
    items_per_user: int = 50
    index_html: str = "index.html"

    class Config:
        env_file = ".env"
