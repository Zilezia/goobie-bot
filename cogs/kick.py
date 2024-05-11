# this for fun
import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        if msg.author == self.bot.user:
            return
        
        content = msg.content.lower()
        
        if content.startswith("kick "):
            if msg.author.id == 711938734987411470:
                mentioned_user = msg.mentions[0] if msg.mentions else None
                if mentioned_user:
                    await mentioned_user.kick(reason="Kicked by bot")
                    await msg.channel.send(f"{mentioned_user.mention} has been kicked.")
            else:
                await msg.channel.send("Lol you aint doin nothin buddy")