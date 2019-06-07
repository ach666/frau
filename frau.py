import discord
import os
import random

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(game=discord.Game(name="please help me get a date with nito"))

@client.event
async def on_message(message):
    

    
    if message.author != client.user:
      msg = message.content.lower()
      if ("training" in msg) or ("sister doll" in msg) or ("frau" in msg) or ("sex" in msg):
        await client.send_message(message.channel,"OHHHHHHHHHHHHHHH YEAHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!")

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
