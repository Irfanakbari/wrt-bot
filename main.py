import discord
from scrap import *


client = discord.Client()

scrap = simple_get()
print(scrap)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('!help'):
        await message.channel.send('Hello!')
    if message.content.startswith('!scrap'):
        await message.channel.send(scrap[0])


@client.event
async def on_message(message):
    if message.content.startswith('!apk'):
        await message.channel.send('Kamu Bisa Download Aplikasi Android WRT Disini : https://wrt.my.id/aplikasi-android-wrt/')


client.run('OTI3OTU2NTk0NTQzNjk3OTgw.YdRw7A.wPKhY0d3v-NubjLcj8gWW9-fq2g')
