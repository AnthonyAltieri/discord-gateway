import os
import pathlib

from dotenv import load_dotenv
from pydantic import BaseModel

from .environment import get_required_environment_variable

# load .env file if it exists
DOTENV_PATH = pathlib.Path(__file__).parent.parent / ".env"
if DOTENV_PATH.exists():
    load_dotenv(str(DOTENV_PATH))

DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8080


class Config(BaseModel):
    # discord bot token
    token: str
    # the secret used to authenticate a request to the server
    server_authorization_secret: str
    # the server host
    host: str
    # the server port
    port: int


config = Config(
    token=get_required_environment_variable("DISCORD_TOKEN"),
    server_authorization_secret=get_required_environment_variable(
        "SERVER_AUTHORIZATION_SECRET"
    ),
    host=os.environ.get("HOST", DEFAULT_HOST),
    port=os.environ.get("PORT", DEFAULT_PORT),
)
