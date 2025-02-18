import discord
import asyncio
import random

# Masukkan token melalui terminal
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
] + ["hi"] * 50

intents = discord.Intents.default()
intents.message_content = True  # Biarkan bot membaca pesan
client = discord.Client(intents=intents)

aktif = False  # Status loop
channel_aktif = None

@client.event
async def on_ready():
    print(f'Login sebagai {client.user}')

@client.event
async def on_message(message):
    global aktif, channel_aktif
    if message.author.id != client.user.id:
        return
    
    if message.content.lower() == "!start":
        if aktif:
            return
        
        aktif = True
        channel_aktif = message.channel  # Simpan channel tempat command dieksekusi
        
        kata_terkirim = 0
        while aktif and kata_terkirim < 200:
            random_text = random.choice(kata_gaul)
            await channel_aktif.send(random_text)
            kata_terkirim += 1
            await asyncio.sleep(12)  # Kirim setiap 12 detik
        
        aktif = False
    
    elif message.content.lower() == "!stop":
        if not aktif:
            return
        
        aktif = False
        channel_aktif = None

client.run(TOKEN, bot=False)
