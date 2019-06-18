import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  await client.change_presence(activity = discord.Game(name="porno make me horno"))

@client.event
async def on_message(message):

    if message.author != client.user:
      channel = message.channel

      if ("training" in message.content.lower()) or ("frau" in message.content.lower()) or ("sex" in message.content.lower()):
        await channel.send("OHHHHHHHHHHHHHHH YEAHHHHHHHHH!!!!!!!!!!!!!!!!!!!!!!")
       
      if ("poop" in message.content.lower()):
        await channel.send("I'M SHIDDING. SHIDDING AND FARDING.")

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
