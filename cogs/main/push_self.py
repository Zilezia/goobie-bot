import discord
from discord import app_commands
from discord.ext import commands

from core.git_pushing import git_pushing

class PushSelf(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, msg: discord.Interaction):
        if msg.author == self.bot.user:
            return
        if msg.content == "pushing works?":
            await msg.channel.send("Yep")
    
    @app_commands.command(name="push_self", description="Push the bot's code to GitHub")
    async def push_self(self, msg: discord.Interaction):
        repo_link = 'https://github.com/Zilezia/goobie-bot'
        target_dir = '.'
        await git_pushing(msg, self.bot, repo_link, target_dir)