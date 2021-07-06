from aiohttp import web
from loguru import logger

from discord_gateway.config import config
from . import middleware
from .routes import setup_routes


def initialize_application() -> web.Application:
    app = web.Application(middlewares=[middleware.authentication])

    setup_routes(app)

    async def on_startup(_: web.Application) -> None:
        logger.info(f"started server on {config.host}:{config.port}")

    app.on_startup.append(on_startup)

    return app
