import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(game=discord.Game(name="porno make me horno"))


token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
