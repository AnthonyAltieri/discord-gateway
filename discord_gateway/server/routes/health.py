from aiohttp import web


async def health(_: web.Request) -> web.Response:
    return web.Response(status=200)
