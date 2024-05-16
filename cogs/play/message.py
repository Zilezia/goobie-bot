import discord
from discord.ext import commands

class Message(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
            
    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        if msg.author == self.bot.user:
            return
                
        content = msg.content.lower()
        
        if content == "messages work?":
            await msg.channel.send("Yeah")  
            
        if content == "goobie stop":
            await msg.channel.send("Pa pa!")
            await self.bot.close()
        
        if content == "hey":
            await msg.channel.send("Hello!")
        elif content == "good boy":
            await msg.channel.send("mmph...")
        elif content == "ayo":
            await msg.channel.send("What?")
        elif content == "fire" or content == "nice":
            await msg.channel.send("ik")
          