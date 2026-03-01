from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    app_name: str
    model_path: str
    database_url: str
    record_on_db: str


settings = Settings()  # ← instantiate once