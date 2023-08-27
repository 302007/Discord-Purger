import os, asyncio

from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix='.', self_bot=True, help_command=None)

@bot.event
async def on_ready():
    print('bot started')

@bot.command()
async def c(ctx, limit: int = 1000):
    removed = 0
    async for msg in ctx.channel.history(limit = limit):
        if msg.author == bot.user:
            try:
                await msg.delete()
                removed += 1
            except:
                pass

    print(f"Successfully Removed {removed} messages.")

load_dotenv()
bot.run(os.getenv('TOKEN'))
