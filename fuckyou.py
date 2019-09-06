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
       
      elif ("poop" in message.content.lower()):
        await channel.send("I'M SHIDDING. SHIDDING AND FARDING.")
      
      elif ("dick" in message.content.lower()):
        await channel.send(file=discord.File("hmmm.jpg"))
      
      elif ("milk" in message.content.lower()):
        await channel.send("milk me hard")
      
      elif ("castor" in message.content.lower()):
        await channel.send("Pussy.")
       
      elif ("teito" in message.content.lower()):
        await channel.send("i'm so proud of you teito")
      
      elif ("r-slur" in message.content.lower()):
        await channel.send("Rasetsu.")
      
      elif ("lab" in message.content.lower()):
        await channel.send("my dick is fucking MASSIVE and i can benchpress you and your entire family")
       
      elif ("capella" in message.content.lower()):
        await channel.send("my tiny son!!!!!!!!!!!!!!!!")
      
      elif ("idil" in message.content.lower()):
        await channel.send("oh my alpha dom 🤤")
        
      elif ("kona" in message.content.lower()):
        await channel.send("step on me omega queen 😍🤪")
      
      elif ("yaoi" in message.content.lower()):
        await channel.send("i love yaoi so much i want a big dom alpha bear to eat me out")
      
      elif ("hito wa mata" in message.content.lower()):
        await channel.send("""hito wa mata oroka na sentaku wo kitto kurikaeshite iku darou
tsumibukaku fujiyuu sou ni, soredemo asu wo sutekirezu kao wo ageru
umareochita kono sekai de

toki no kanata mimi wo sumasu musuu no Pieces of History
katari kakeru koe naki koe
tooi hi no kaze no nioi musekaeru netsu no kioku wa
ikari wo hodoki arasoi nado hajime kara nakatta you ni

nagashita chi mo namida mo wasure sararete iku
daichi wa nando demo kagayaki wo torimodoshi

hito wa mata oroka na sentaku wo kitto kurikaeshite iku darou
tsumibukaku fujiyuu sou ni, soredemo asu wo sutekirezu kao wo ageru
umareochita kono sekai de

sasae aeta hi mo aru darou negawakuba Pieces of History
warai kakeru kao naki kao
taiyou to yume no nagori tamentai no kokoro no mama ni
ayumi tsudzuketa odayakasa mo hageshisa mo kakae nagara

subete wo tsutsumi konde toki wa nagarete iku
matataku hoshi no ne ni ichinichi wo owarasete

hito wa mata kanashii honnou de kitto machigaete shimau kedo
sono tabi ni yari naoseru to shinjiru chikara mune no oku utagawanai
umareochita sono toki kara

hito wa mata oroka na sentaku wo kitto kurikaeshite iku darou
tsumibukaku fujiyuu sou ni, soredemo asu wo sutekirezu ni
hito wa mata kanashii honnou de kitto machigaete shimau kedo
sono tabi ni yari naoseru to shinjiru chikara mune no oku utagawanai
umareochita sono toki kara""")

token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
