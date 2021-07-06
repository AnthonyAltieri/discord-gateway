import discord.ext.commands


class BotProvider:
    def __init__(self):
        self.__bot = discord.ext.commands.Bot(command_prefix="$")

    def get_bot(self) -> discord.ext.commands.Bot:
        return self.__bot


bot_provider = BotProvider()
