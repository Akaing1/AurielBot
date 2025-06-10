from twitchio.ext import commands


class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #  !help command -> lists out custom commands
    @commands.command()
    async def help(self, ctx: commands.Context):
        help_message = (f"Here are the list of commands you can use with {self.bot.name}: \n"
                        f"Add commands here")
        await ctx.send(help_message)