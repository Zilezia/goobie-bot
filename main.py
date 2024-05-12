import asyncio
import discord
from discord.ext import commands
import os

import settings

# cogs vvv

from cogs import * # bs cog import


def main():
    intents = discord.Intents.all()
    intents.members = True
    
    myID = 711938734987411470 # helloey
    bot = commands.Bot(intents=intents, command_prefix='&')
    
    def is_me(interaction: discord.Interaction):
        return interaction.user.id == myID    # your own user id so only you are able to interact with the bot
                                        # (kinda pointless when you have it on a private server for yourself only but just in case ehh)
    @bot.event
    async def on_ready():        
        synced = await bot.tree.sync()
        if len(synced) == 1:
            print(f"Synced {len(synced)} command")
        else:
            print(f"Synced {len(synced)} commands")
        
        print(f'{bot.user.name} is online')
        
        channel = bot.get_channel(1233687647302455309) # idk if this should not be shared when pushed onto github prob it can be 🤷‍♀️
        await channel.send(f"I'm online! <@{myID}>")
    
    async def load_cogs(): # idk how to load them better than like this
        for cog in [
            # main cogs? 
            Log,
            PushSelf,
            FileEditor,
            
            # just play cogs
            Message,
            Kick,

            # test cogs
            TestRoles,
        ]:
            await bot.add_cog(cog(bot))
    
    asyncio.run(load_cogs()) # bs cog loading finger
        
    bot.run(settings.BOT_SECRET)
                

if __name__ == "__main__":
    main()
