from pydantic_settings import BaseSettings


class PostgresqlSettings(BaseSettings):
    POSTGRES_URL: str


postgresql_settings = PostgresqlSettings()  # type:ignore
