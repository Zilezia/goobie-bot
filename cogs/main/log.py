# Libraries
from datetime import datetime
import discord
from discord import app_commands
from discord.ext import commands
import re
# Files
from core.git_pushing import git_pushing

class Log(commands.Cog):
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
        target_dir = r"..\..\goobie"
        repo_link = 'https://github.com/Zilezia/goobie'
        line_number = 10
        current_time = datetime.now().strftime("%d/%m/%Y-%H:%M")

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

        await git_pushing(self.bot, msg, repo_link, target_dir)

        # put publishing onto github