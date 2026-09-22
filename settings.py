from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    base_api_url: str
    base_ui_url: str
    admin_email: str
    admin_password: str
    admin_name: str


settings = Settings()
