from twitchio.ext import commands
import random


class GambleBread(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.points = 0  # TODO: add points system class

    @commands.command()
    async def bread(self, ctx: commands.Context):
        points = self.points
        await ctx.send(f"{ctx.author.name} has accumulated {points} stale bread!")

    @commands.command()
    async def gambleBread(self, ctx: commands.Context, amount: str):

        result = random.randint(0, 100)
        resultFlag = result > 50

