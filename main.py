import discord
from discord.ext import commands
import asyncio
import random

# Masukkan token Discord
TOKEN = input("Masukkan token Discord: ")

# List kata-kata gaul
kata_gaul = [
    "santuy abis bro", "gasken lah", "anjay keren bet", "woles aja sih", "mabar yok",
    "coy slow aja", "gaskeun jangan banyak cingcong", "lu ngapa dah", "wkwk ngakak parah", "asli vibesnya pecah",
    "udah kek sultan aja lu", "cuan terus bro", "nani", "mantul gan", "sabi lah", "gila lu parah",
    "jangan julid mulu bos", "receh banget sih lu", "gila skill dewa", "ggwp", "mantap jiwa", "bocil kematian", 
    "banyak bacot lu", "pecah banget", "serem anjir", "kocak banget sih", "gokil lu", "parah bet dah", 
    "lu slow aja bro", "ini mah auto win", "ketawa mulu wkwk", "ngebut kayak jet", "sultan gaming", 
    "pasti hoki nih", "harusnya gua menang", "ini mah ez", "ngegasss pol", "bikin ngakak banget", "mood naik cuy", 
    "kasian banget sih", "auto lose wkwk", "booyah lets go", "sikat bos", "mantep banget sumpah", "asyik bet dah", 
    "ciyus miapah", "ngabers detected", "aneh bet dah", "bentar gua lagi makan", "ngopi dulu bos", "wah parah ini sih", 
    "udah feeling gua bener", "sumpah gua gak expect", "meledak cuy", "mantep bet dah", "jangan gitu lah", "bakar bakar bakar",
    "dah lah gua capek", "malah bikin kesel", "bukan level kita ini", "gas poll", "tinggal gaskeun aja", "lu pasti bisa bro"
] + ["hi"] * 6000

# Setup bot
client = commands.Bot(command_prefix="!", self_bot=True)
aktif = False
channel_aktif = None

@client.event
async def on_ready():
    print(f'Login sebagai {client.user}')

@client.command()
async def start(ctx):
    global aktif, channel_aktif
    if aktif:
        return

    aktif = True
    channel_aktif = ctx.channel

    kata_terkirim = 0
    while aktif and kata_terkirim < 200:
        random_text = random.choice(kata_gaul)
        await channel_aktif.send(random_text)
        kata_terkirim += 1
        await asyncio.sleep(13)

    aktif = False

@client.command()
async def stop(ctx):
    global aktif
    aktif = False

client.run(TOKEN, bot=False)
