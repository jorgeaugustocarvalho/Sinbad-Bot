import discord
import emoji
from deep_translator import GoogleTranslator
from discord.ext import commands
import random
import asyncio
import time

client = commands.Bot(command_prefix = "$", case_insensitive = True)

@client.event
async def on_ready():
    print(' "Humanos são como oceanos, e não há ondas que eu não possa superar!" '.format(client))

@client.command()
async def sinbad(x):
    await x.send(emoji.emojize('''
===============
    SINBAD BOT :sailboat:
===============
                            
"Humanos são como oceanos!! 
   E não há ondas que eu não 
            possa superar!!!"

$ajuda para ver os comandos
'''))

@client.command()
async def ajuda(x):
    await x.send('''==============$$COMANDOS$$==============

====================================

$ajuda => abre essa aba aqui ;)

====================================

$translate => o tradutor mais eficaz dos sete mares! Para traduzir uma palavra basta utilizar essa sintaxe:

    $translate oceano en => ocean (para palavras)

    $translate "O mundo nos espera!" en => The world awaits us (para frases)

====================================

$sort => para fazer sorteios rápidos para algum jogo ;P

    ex: $sort 10 => algum número aleatório entre 1 e 10

====================================

$super_flood => mete um numero se aloprar na potenciação

    ex: $super_flood 2 100 => um mega numero imprimido

==================================== 
    ''')

@client.command()
async def ola(x):
    await x.send(f'Olá, {x.author}')

@client.command()
async def sort(x, numero):
    sorteio = random.randint(1, int(numero))
    await x.send(f'O número sorteado foi: {sorteio}')

@client.command()
async def super_flood(x, i, j):
    s = int(i) ** int(j)
    await x.send(f'{s}')

# função tradutor de palavras para o bot
@client.command()
async def translate(x, palavra, lingua):
    trad = GoogleTranslator(source = 'auto', target = lingua).translate(palavra)
    await x.send("Pode confiar! Já estive por todos os 4 cantos do mundo e posso traduzir sua mensagem com facilidade!")
    time.sleep(2)
    await x.send(f"{trad}")

@client.command()
async def adivinha(x, numero: int):
    """Adivinhe o numero de 1 a 6"""
    valor = random.randint(1, 6)
    if numero == valor:
        await x.send("Acertou")
    else:
        await x.send("Errou")

client.run('tokenHere')