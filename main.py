import os, asyncio

from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='.', self_bot=True)

@bot.event
async def on_ready():
    print('bot started')

@bot.command()
async def c(ctx, limit: int = 1000):
    removed = 0
    tried = 0

    async for msg in ctx.message.channel.history(limit = limit):
        if msg.author.id == bot.user.id:
            if (tried % 15 == 0 and tried != 0):
                print("Sleeping for 3 seconds...")
                await asyncio.sleep(3)
                
            try:
                await msg.delete()
                removed += 1
            except:
                pass
            tried += 1
        asyncio.sleep(0.3)

    print(f"Removed {removed} messages. Now waiting.")

load_dotenv()
bot.run(os.getenv('TOKEN'))