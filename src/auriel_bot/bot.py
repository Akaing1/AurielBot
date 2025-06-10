import twitchio
from twitchio import Message
from twitchio.ext import commands
from src.config.config import Config


class AurielBot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=Config.BOT_AUTH_TOKEN,
            prefix='!',
            channels=Config.CHANNELS,
            name=Config.BOT_NAME
        )

        self.load_cogs()

    def load_cogs(self):
        # self.load_module()

    async def event_ready(self):
        channel = self.get_channel(Config.CHANNELS)
        await channel.send(f"{self.name} is ready!")

    async def event_message(self, message: Message) -> None:
        # TODO: add when user interacts with the bot
        return