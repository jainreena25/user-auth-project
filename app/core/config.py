from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "user-auth-project"
    database_url: str
    debug_mode: bool = False
    admin_email: str = "admin1@example.com"
    items_per_user: int = 150

    model_config = SettingsConfigDict(
        env_file=".env",  # Default .env file
        env_file_encoding='utf-8',
        extra='ignore'  # Ignore extra fields in .env files
    )

settings = Settings()