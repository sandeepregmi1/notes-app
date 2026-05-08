from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

from dotenv import load_dotenv
import os

from app.database import Base
from app import models  # ensures models are loaded

load_dotenv()

config = context.config

DATABASE_URL = os.getenv("DATABASE_URL")

config.set_main_option("sqlalchemy.url", DATABASE_URL)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata