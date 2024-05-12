import discord
from discord import app_commands
from discord.ext import commands
import os

from core.page_view import PaginationView

class TestRoles(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author == self.bot.user:
            return
    
    @app_commands.command(name="test_roles", description="Access a directory (mainly just the goobie workspace) and edit from here!")
    async def test_roles(self, interaction: discord.Interaction):

        # testing this out

        embeds = []
        for roles in discord.utils.as_chunks(interaction.guild.roles, 3):
            embed = discord.Embed(title="role list (test)")
            for i in roles:
                embed.add_field(name=f'{i.name}', value=f"Members:- ``{len(i.members)}``")
            embeds.append(embed)
        
        view = PaginationView(embeds)
        await interaction.response.send_message(embed=view.initial, view=view)
        