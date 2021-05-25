import discord
import time
import datetime
from discord.ext import commands
import random

class user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(brief="Says hello")
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            await ctx.send('Hello {0.name}~'.format(member))
        else:
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        self._last_member = member

    @commands.command(brief="Info about the current server.")
    async def serverinfo(self, ctx):
        icon = ctx.guild.icon_url
        content = f"Name: {ctx.guild.name}\nID: {ctx.guild.id}\nOwner: <@{ctx.guild.owner_id}>\nBoosts: {ctx.guild.premium_subscription_count}\nCreated: {ctx.guild.created_at}"
        embed = discord.Embed(
            title = ctx.guild.name,
            description = content,
            colour = discord.Colour.green()


        )
        embed.set_footer(text="Hallucinate")
        await ctx.send(embed=embed)
        await ctx.message.add_reaction("✅")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! That took {(round(self.bot.latency*1000, 1))}ms')

def setup(bot):
    bot.add_cog(user(bot))
    print("Cog user loaded")
