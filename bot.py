import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

zap_frases = ['É o baitas',
              'Bate e corre', 'Caguei nas calças',
              'Quem mora em pernambuco é pernambucano...',
              'Mano?! Tá ficando doido?',
              'Morra atedessauro',
              'Êta boba da peste',
              'Comi tua mãe',
              'Próximo drag é alma deles',
              '',
              ]


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'mano?':
        response = random.choice(zap_frases)
        await message.channel.send(response)

    if message.content.lower() == 'chá':
        await message.channel.send('Pra dois')


@client.event
async def on_member_join(member):
    print('teste')
    member.create_dm()
    member.dm_channel.send('Hi')


client.run(TOKEN)
