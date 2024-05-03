import asyncio
from datetime import datetime
import discord
from discord import app_commands
from discord.ext import commands
from git import Repo
import re

class LogCOG(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return
        if msg.content == "logs work?":
            await msg.channel.send("Yep")
    
    @app_commands.command(name="message_log", description="Log a message")
    async def message_log(self, msg: discord.Interaction, log: str):
        log_file_path = r"..\..\goobie\src\pages\log\Log.tsx"
        git_file_path = r"..\..\goobie"
        line_number = 10
        current_time = datetime.now().strftime("%d/%m/%Y-%H:%M")
        status = "Success"

        url_pattern = r'https?://\S+'
        
        urls = re.findall(url_pattern, log)
        
        for url in urls: 
            log = log.replace(url, f"<Link to=\"{url}\"><TextWave>{url}</TextWave></Link>")
        
        
        
        lines = []
        with open(log_file_path, "r") as file:
            lines = file.readlines()
        
        if line_number <= len(lines):
            lines.insert(line_number - 1,
                f'''
      <section className="log" id="{current_time}">
        <h3 className="date-n-time">{current_time}:</h3>
        <p className="log-text">
        {log}.
        </p>
      </section>''')
        
        with open(log_file_path, "w") as file:
            file.writelines(lines)
            
        # fucked something other here after changing from cra to vite
        # or someting with my mouse events that had errors for some reason
            
        try:
            repo = Repo(git_file_path)
            status_output = repo.git.status()
    
            # if f"Changes to be committed:\n  (use \"git restore --staged <file>...\" to unstage)\n\tmodified:   {log_file_path}\n" in status_output:
            #     await msg.response.send_message("Staging changes...")
            #     repo.git.add('.')
            # else:
            #     await msg.response.send_message("Changes staged already.")
                    
            # await msg.response.send_message("Committing changes...")
            # repo.git.commit('-m', f"Log commit - {current_time}")
            
            await msg.response.send_message("Pushing changes to remote repository...")
            repo.git.push('origin', 'main')
            
                    
        except Exception as e:
            await msg.response.send_message(f"Error: {e}")

        try:
            if status == "Success":
                success_message = "Log made!"
                await msg.response.send_message(success_message)
            else:
                error_message = "An error occurred during the logging process."
                await msg.response.send_message(error_message)
        except discord.errors.NotFound:
            pass