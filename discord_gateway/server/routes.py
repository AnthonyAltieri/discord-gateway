from typing import Optional, cast, Union

import discord
from aiohttp import web
from aiohttp.web_routedef import RouteTableDef
from loguru import logger
from pydantic import BaseModel, ValidationError

from discord_gateway.discord_bot.bot import bot_provider
from .constants import API_PREFIX

routes = RouteTableDef()


class ChannelMessage(BaseModel):
    # the message to send to the discord channel
    message: str
    # the id of the discord channel
    channel_id: int


@routes.post(f"{API_PREFIX}/channel/message")
async def send_message(request: web.Request) -> web.Response:
    try:
        message = ChannelMessage(**(await request.json()))
    except ValidationError as error:
        logger.error("post body validation error", error=error)
        return web.Response(status=400)

    bot = bot_provider.get_bot()

    guild_channel: Optional[discord.abc.GuildChannel] = bot.get_channel(
        message.channel_id
    )
    if guild_channel is None:
        logger.error("channel not found", channel_id=message.channel_id)
        return web.Response(status=404)

    if not callable(getattr(guild_channel, "send")):
        logger.error("channel not message-able", channel_id=message.channel_id)
        return web.Response(status=404)

    # assume if the guild channel has a send function it can be sent a message
    message_channel = cast(
        Union[discord.abc.GuildChannel, discord.abc.Messageable], guild_channel
    )

    await message_channel.send(message.message)
    logger.info("sent message", message=message)

    return web.Response(status=201)
