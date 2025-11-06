import json
import logging
from pathlib import Path
from typing import ClassVar, Optional, Union

from dotenv import load_dotenv
from pydantic import Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

from core.utils.settings import getenv

load_dotenv()

ENVIRONMENT_FILENAME: str = getenv("ENVIRONMENT_NAME", ".env")
FILE_ENCODING: str = "utf-8"


class Settings(BaseSettings):
    """
    Application settings configuration
    """

    # ClassVar for non-field attributes
    BASE_DIR: ClassVar[Path] = Path(__file__).resolve().parent.parent
    PROJECT_ROOT: ClassVar[str] = str(Path(__file__).resolve().parent.parent)
    DEBUG: bool = Field(default=True, env="DEBUG")
    SECRET_KEY: str = Field(
        default="django-insecure-change-this-in-production",
        env="SECRET_KEY",
    )
    STATIC_URL: str = Field(
        env="STATIC_URL",
        default="/static/",
    )
    ALLOWED_HOSTS: Union[str, list[str]] = Field(default="")
    CSRF_TRUSTED_ORIGINS: Union[str, list[str]] = Field(default="")
    LOG_LEVEL: int = Field(default=logging.INFO, env="LOG_LEVEL")
    DATABASE_URL: str = Field(
        default="postgresql://postgres:postgres@localhost:5432/mydb",
        env="DATABASE_URL",
    )
    GRAPHQL_CONNECTION_MAX_RESULTS: int = Field(
        env="GRAPHQL_CONNECTION_MAX_RESULTS",
        default=200,
    )
    MEDIA_URL: str = Field(default="/media/", env="MEDIA_URL")
    ENVIRONMENT: str = Field(env="ENVIRONMENT", default="dev")
    APPLICATION_VERSION: str = Field(env="APPLICATION_VERSION", default="dev")
    APPLICATION_NAME: str = Field(
        env="APPLICATION_NAME", default="django-graphql-federation"
    )
    APPLICATION_NAMESPACE: Optional[str] = Field(
        env="APPLICATION_NAMESPACE", default=None
    )

    FLUENT_HOST: Optional[str] = Field(env="FLUENT_HOST", default=None)
    FLUENT_PORT: int = Field(env="FLUENT_PORT", default=24224)

    # Add your custom configuration here
    # Example:
    # API_KEY: str = Field(env="API_KEY", default="")

    @model_validator(mode='after')
    def parse_list_fields(self):
        """Convert comma-separated strings to lists for ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS"""
        # Parse ALLOWED_HOSTS
        if isinstance(self.ALLOWED_HOSTS, str):
            if self.ALLOWED_HOSTS.strip():
                self.ALLOWED_HOSTS = [host.strip() for host in self.ALLOWED_HOSTS.split(',') if host.strip()]
            else:
                self.ALLOWED_HOSTS = []
        
        # Parse CSRF_TRUSTED_ORIGINS
        if isinstance(self.CSRF_TRUSTED_ORIGINS, str):
            if self.CSRF_TRUSTED_ORIGINS.strip():
                self.CSRF_TRUSTED_ORIGINS = [origin.strip() for origin in self.CSRF_TRUSTED_ORIGINS.split(',') if origin.strip()]
            else:
                self.CSRF_TRUSTED_ORIGINS = []
        
        return self

    model_config = SettingsConfigDict(
        env_prefix="",
        case_sensitive=False,
        env_file=ENVIRONMENT_FILENAME,
        env_file_encoding=FILE_ENCODING,
        extra="ignore",
    )


conf = Settings()

logger = logging.getLogger(__name__)
logger.debug(conf.model_dump())
