import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "MTU1ODQ3NDEwMjY5ODk0MjUzNA.GbLT50.qGQCMXzZUtHScdZfu2NJqgVgl0GxQI9cPN0co4"
CHANNEL_ID = 1552709039811727370


@bot.event
async def on_ready():
  print(f"Bot connected as {bot.user}")
  channel = bot.get_channel(CHANNEL_ID)
  if channel:
    try:
      await channel.connect(reconnect=True, self_deaf=True)
      print("Voice Channel-e join koreche!")
    except Exception as e:
      print(f"Connection error: {e}")


bot.run(TOKEN)