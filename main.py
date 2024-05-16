# Libraries
import asyncio
import discord
from discord.ext import commands
# Files
import settings
from cogs import * # bs cog import

def main():
    intents = discord.Intents.all()
    intents.members = True
    
    myID = 711938734987411470 # helloey
    bot = commands.Bot(intents=intents, command_prefix='&')
    
    def is_me(interaction: discord.Interaction):
        return interaction.user.id == myID # chuj

    @bot.event
    async def on_ready():        
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
        print(f'{bot.user.name} is online')
        channel = bot.get_channel(1233687647302455309) # personal text channel
        await channel.send(f"I'm online! <@{myID}>")
    
    async def load_cogs(): # idk how to load them better than like this
        for cog in [
        # main
            Log,
            PushSelf,
            FileEditor,
        # play
            Message,
            Kick,
        # tests
            TestRoles,
        ]:
            await bot.add_cog(cog(bot))
    
    asyncio.run(load_cogs()) # bs cog loading finger
        
    bot.run(settings.BOT_SECRET)
                
if __name__ == "__main__":
    main()
