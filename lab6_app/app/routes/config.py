import os
from dotenv import load_dotenv

load_dotenv()


class AppConfig:
    """Static configuration that only changes on app restart."""

    def __init__(
        self,
        app_name: str = os.getenv("APP_NAME", "Green Infrastructure API"),
        app_version: str = os.getenv("APP_VERSION", "1.0.0"),
        app_description: str = os.getenv("APP_DESCRIPTION", "API for analyzing infrastructure accessibility for green spaces (trees)"),
        app_authors: list = ["ViolettaZim"],
        contact_email: str = "violetta@greeninfra.com",
        license_name: str = "MIT",
    ):
        self._app_name = app_name
        self._app_version = app_version
        self._app_description = app_description
        self._app_authors = app_authors
        self._contact_email = contact_email
        self._license_name = license_name

    @property
    def app_name(self) -> str:
        return self._app_name

    @property
    def app_version(self) -> str:
        return self._app_version

    @property
    def app_description(self) -> str:
        return self._app_description

    @property
    def app_authors(self) -> list:
        return self._app_authors

    @property
    def contact_email(self) -> str:
        return self._contact_email

    @property
    def license_name(self) -> str:
        return self._license_name

    def to_dict(self) -> dict:
        return {
            "app_name": self._app_name,
            "app_version": self._app_version,
            "app_description": self._app_description,
            "app_authors": self._app_authors,
            "contact_email": self._contact_email,
            "license_name": self._license_name,
        }


app_config = AppConfig()

