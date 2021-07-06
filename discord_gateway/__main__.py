import asyncio

from aiohttp.web_runner import AppRunner, TCPSite

from discord_gateway.config import config
from discord_gateway.discord_bot.bot import bot_provider
from discord_gateway.server.app import initialize_application


async def main():
    app = initialize_application()
    runner = AppRunner(app)
    await runner.setup()
    site = TCPSite(runner, config.host, config.port)
    await site.start()

    bot = bot_provider.get_bot()

    try:
        await bot.start(config.token)
    except Exception:
        await bot.close()
        raise
    finally:
        await runner.cleanup()


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
