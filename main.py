import asyncio
import discord
from discord.ext import commands

from cogs import * # bs cog import

def botToken():
    try:
        with open("../../bot-tokens/goobie_token.txt", "r") as file: # 🤓 so lame
            token = file.read().strip()
        return token
    except FileNotFoundError:
        print("Token not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def run():
    token = botToken()

    intents = discord.Intents.all()
    intents.members = True
    bot = commands.Bot(intents=intents, command_prefix='&')
    myID = 711938734987411470 # helloey

    def is_me(interaction: discord.Interaction):
        return interaction.user.id == myID    # your own user id so only you are able to interact with the bot
                                        # (kinda pointless when you have it on a private server for yourself only but just in case ehh)
    @bot.event
    async def on_ready():        
        try:
            synced = await bot.tree.sync()
            if len(synced) == 1:
                print(f"Synced {len(synced)} command")
            else:
                print(f"Synced {len(synced)} commands")
        except Exception as e:
            print(e)
            
        print(f'{bot.user.name} is online')
        
        channel = bot.get_channel(1233687647302455309) # idk if this should not be shared when pushed onto github prob it can be 🤷‍♀️
        await channel.send(f"I'm online! <@{myID}>")

    async def load_cogs():
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
    bot.run(token)

if __name__ == "__main__":
    run()