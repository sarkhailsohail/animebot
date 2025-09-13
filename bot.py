import discord
from discord.ext import commands
import aiohttp
import random
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# --- API Fetch Function ---
async def get_nsfw_image(endpoint):
    url = f"https://api.waifu.pics/nsfw/{endpoint}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return data["url"]

# --- Commands ---
@bot.command()
@commands.is_nsfw()
async def hentai(ctx):
    img_url = await get_nsfw_image("waifu")
    embed = discord.Embed(title="🔞 Hentai Waifu", color=discord.Color.purple())
    embed.set_image(url=img_url)
    await ctx.send(embed=embed)

@bot.command()
@commands.is_nsfw()
async def blowjob(ctx):
    img_url = await get_nsfw_image("blowjob")
    embed = discord.Embed(title="🔞 Blowjob", color=discord.Color.purple())
    embed.set_image(url=img_url)
    await ctx.send(embed=embed)

@bot.command()
@commands.is_nsfw()
async def neko(ctx):
    img_url = await get_nsfw_image("neko")
    embed = discord.Embed(title="😼 Neko Lewd", color=discord.Color.purple())
    embed.set_image(url=img_url)
    await ctx.send(embed=embed)

@bot.command()
@commands.is_nsfw()
async def thighs(ctx):
    # Custom category images
    thighs_list = [
        "https://example.com/thigh1.jpg",
        "https://example.com/thigh2.jpg"
    ]
    img_url = random.choice(thighs_list)
    embed = discord.Embed(title="🍑 Anime Thighs", color=discord.Color.purple())
    embed.set_image(url=img_url)
    await ctx.send(embed=embed)

@bot.command()
@commands.is_nsfw()
async def spank(ctx, member: discord.Member):
    gifs = [
        "https://media.tenor.com/X4M6tiyAvJYAAAAC/anime-spank.gif",
        "https://media.tenor.com/aaMzyC4N2SwAAAAC/spank.gif"
    ]
    gif = random.choice(gifs)
    embed = discord.Embed(description=f"🔥 {ctx.author.mention} spanks {member.mention}",
                          color=discord.Color.red())
    embed.set_image(url=gif)
    await ctx.send(embed=embed)

bot.run("YOUR_BOT_TOKEN")
