import os
from dotenv import load_dotenv
from twitchio.ext import commands

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
TWITCH_TOKEN = os.getenv('TWITCH_TOKEN')
TWITCH_CLIENT_ID = os.getenv('TWITCH_CLIENT_ID')
BOT_NICK = os.getenv('BOT_NICK', 'AurielBot')
CHANNEL = os.getenv('CHANNEL', 'your_channel_name')

# Create bot instance
bot = commands.Bot(
    token=TWITCH_TOKEN,
    client_id=TWITCH_CLIENT_ID,
    nick=BOT_NICK,
    prefix='!',
    initial_channels=[CHANNEL]
)

@bot.event
async def event_ready():
    """Event triggered when the bot connects to Twitch."""
    print(f'Connected to Twitch as {bot.nick}')

@bot.event
async def event_message(message):
    """Event triggered when a message is sent in the channel."""
    # Don't respond to bot's own messages
    if message.echo:
        return
    
    print(f'{message.author.name}: {message.content}')
    
    # Process commands
    await bot.handle_commands(message)

@bot.command(name='hello')
async def hello_command(ctx):
    """Simple hello command."""
    await ctx.send(f'Hello {ctx.author.name}!')

@bot.command(name='ping')
async def ping_command(ctx):
    """Ping command."""
    await ctx.send('Pong!')

if __name__ == '__main__':
    bot.run()
