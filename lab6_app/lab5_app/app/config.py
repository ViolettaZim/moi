class AppConfig:
    """Static configuration that only changes on app restart."""

    def __init__(
        self,
        app_name: str = "Green Infrastructure API",
        app_version: str = "0.1.0",
        app_description: str = "API for analyzing infrastructure accessibility for green spaces (trees)",
        app_authors: list = ["ViolettaZim"],
        contact_email: str = "viozim@ya.ru",
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
        """Return configuration as dictionary."""
        return {
            "app_name": self._app_name,
            "app_version": self._app_version,
            "app_description": self._app_description,
            "app_authors": self._app_authors,
            "contact_email": self._contact_email,
            "license_name": self._license_name,
        }
   
    
app_config = AppConfig()

