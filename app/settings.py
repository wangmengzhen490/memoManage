from functools import lru_cache
from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')
    database_url:str
    app_title:str

@lru_cache()
def get_settings():
    return Settings()
