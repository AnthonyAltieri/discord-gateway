from aiohttp import web

from discord_gateway.server.constants import API_PREFIX
from . import channel, health


def url(endpoint: str) -> str:
    return f"{API_PREFIX}{endpoint if endpoint.startswith('/') else f'/{endpoint}'}"


def setup_routes(app: web.Application) -> None:
    # Health
    app.router.add_get(url("/health"), health.health)

    # Channel
    app.router.add_post(url("/channel/message"), channel.send_message)
