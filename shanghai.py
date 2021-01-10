import discord,subprocess,asyncio
from time import sleep

client = discord.Client()

token = ""

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.bot and message.author.id != 558919170666790932:
        return
    if message.content.startswith("\"shanghai>") and message.content != "\"shanghai>" and message.author.id == 465104296430796812 or message.content.startswith("\"shanghai>") and message.content != "\"shanghai>" and message.content != "\"shanghai>\"kill":
        await message.channel.send(message.content[10:])
    if message.content == "\"shanghai update" and message.author.id == 465104296430796812:
        await message.channel.send("\"kill")
        await asyncio.sleep(1)
        subprocess.run("start \"ohayou\" py ohayou_d.py",shell=True)
    if message.content == "\"shanghai updatem" and message.author.id == 465104296430796812:
        await message.channel.send("\"kill")
        await asyncio.sleep(1)
        subprocess.run("start \"ohayou\" py ohayou_m.py",shell=True)
    if message.content == "お前が死ぬんやで" and message.author.id == 558919170666790932:
        await message.channel.send("グエー死んだンゴ")
        quit()

client.run(token)
