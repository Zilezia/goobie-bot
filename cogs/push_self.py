from datetime import datetime
import discord
from discord import app_commands
from discord.ext import commands
from git import Repo

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
        git_file_path = "."
        current_time = datetime.now().strftime("%d/%m/%Y-%H:%M")


        repo = Repo(git_file_path)

        await msg.response.send_message("Staging changes...")
        repo.git.add('.')
        await msg.channel.send("Committing changes...")
        repo.git.commit('-m', f"Log commit - {current_time}")

        await msg.channel.send("Pulling changes from remote repository...")
        repo.git.pull('origin', 'main')

        await msg.channel.send("Pushing changes to remote repository...")
        repo.git.push('origin', 'main')

        await msg.channel.send("Finished!")
        await msg.channel.send("https://github.com/Zilezia/goobie-bot")

    