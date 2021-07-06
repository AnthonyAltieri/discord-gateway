from aiohttp import web

from discord_gateway.config import config
from discord_gateway.server.constants import API_PREFIX


@web.middleware
async def authentication(request: web.Request, handler):
    is_not_health_check_endpoint = request.path != f"{API_PREFIX}/health"
    is_not_authorized = (
        request.headers.get("Authorization")
        != f"Secret {config.server_authorization_secret}"
    )

    if is_not_health_check_endpoint and is_not_authorized:
        return web.Response(status=403)

    return await handler(request)
