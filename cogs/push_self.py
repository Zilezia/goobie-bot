import discord
from discord import app_commands
from discord.ext import commands
from git import Repo

class PushSelfCOG(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, msg: discord.Interaction):
        if msg.author == self.bot.user:
            return
        if msg.content == "pushing works?":
            await msg.channel.send("Yep")
    
    @app_commands.command(name="push_yourself", description="Push the bots codes into github")
    async def push_yourself(self, msg: discord.Interaction):
        git_file_path = "."

        repo = Repo(git_file_path)
        
        await msg.response.send_message("Staging changes...")
        repo.git.add('.')
        await msg.channel.send("Committing changes...")
        repo.git.commit('-m', "Log commit")
        
        await msg.channel.send("Pushing changes to remote repository...")
        repo.git.push('origin', 'main')
        
        await msg.channel.send("Finished!")
    