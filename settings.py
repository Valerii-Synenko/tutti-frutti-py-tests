from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_FILE = Path(__file__).resolve().parent / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")

    base_api_url: str
    base_ui_url: str
    admin_email: str
    admin_password: str
    admin_name: str
    user_db_url: str
    qase_api_url: str
    qase_testops_api_token: str
    qase_testops_project: str
    qase_mode: str
    qase_testops_run_complete: bool


settings = Settings()
