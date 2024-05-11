import discord
from discord import app_commands
from discord.ext import commands

from typing import List
from collections import deque

class PaginationView(discord.ui.View):
    def __init__(self, embeds: List[discord.Embed]) -> None:
        super().__init__(timeout=30)
        self._embeds = embeds
        self._queue = deque(embeds)
        self._initial = embeds[0]
        self._len = len(embeds)
        self._current_page = 1
        self.children[0].disabled = True
        self._queue[0].set_footer(text=f"Pages of {self._current_page}/{self._len}")
        
    async def update_buttons(self, interaction: discord.Interaction) -> None:
        
        # for i in self._queue:
        #     i.set_footer(text=f"Pages of {self._current_page}/{self._len}")
        
        self._queue[0].set_footer(text=f"Pages of {self._current_page}/{self._len}")
        
        if self._current_page == self._len:
            self.children[1].disabled = True
        else:
            self.children[1].disabled = False
            
        if self._current_page == 1:
            self.children[0].disabled = True
        else:
            self.children[0].disabled = False
            
        await interaction.message.edit(view=self)
        
        
    
    @discord.ui.button(emoji='◀')
    async def previous_btn(self, interaction: discord.Interaction, _):
        self._queue.rotate(-1)
        embed = self._queue[0]
        self._current_page -= 1
        await self.update_buttons(interaction)
        await interaction.response.edit_message(embed=embed)
        
    @discord.ui.button(emoji='▶')
    async def next_btn(self, interaction: discord.Interaction, _):
        self._queue.rotate(1)
        embed = self._queue[0]
        self._current_page += 1
        await self.update_buttons(interaction)
        await interaction.response.edit_message(embed=embed)
        
    @discord.ui.button(label="close",emoji='✖', style=discord.ButtonStyle.danger)
    async def close_btn(self, interaction: discord.Interaction, _):
        message = await interaction.channel.fetch_message(interaction.message.id)
        await message.edit(view=None)
        await interaction.response.send_message("View closed.")
        
    
    @property
    def initial(self) -> discord.Embed:
        return self._initial