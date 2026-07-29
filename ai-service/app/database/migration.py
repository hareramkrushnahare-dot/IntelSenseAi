from alembic import command
from alembic.config import Config


def run_migrations(alembic_ini: str = "alembic.ini"):
    config = Config(alembic_ini)
    command.upgrade(config, "head")
