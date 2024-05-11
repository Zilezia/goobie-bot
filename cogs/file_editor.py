import asyncio
from datetime import datetime
import discord
from discord import app_commands
from discord.ext import commands
from git import Repo
import re
import os

from core.page_view import PaginationView

class FileEditor(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return
        if msg.content == "ide work?":
            await msg.channel.send("Yep")
    
    @app_commands.command(name="edit_file", description="Access a directory (mainly just the goobie workspace) and edit from here!")
    async def edit_file(self, interaction: discord.Interaction):
        file_path = r"..\..\goobie"

        # testing this out
        current_dir = os.path.dirname(os.path.realpath(__file__))
        
        test_fp = os.path.join(current_dir, "testing_dir")
        
        files = os.listdir(test_fp)
        files.sort(key=lambda x: int(x.split("random")[1].split(".")[0]))
        
        # print("Sorted files:", files) # debugging
        
        embeds = []
        for file_name in files:
            fn_path = os.path.join(test_fp, file_name)
            embed = discord.Embed(title="List of files")
            # print("Reading file:", fn_path) # debugging
            with open(fn_path, "r") as file:
                line = file.readlines()
            embed.add_field(name=file_name, value=line)
            embeds.append(embed)
        
        view = PaginationView(embeds)
        await interaction.response.send_message(embed=view.initial, view=view)
        