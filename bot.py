import discord
from discord.ext import commands
import aiohttp
import random
import os
import threading
from dotenv import load_dotenv
from flask import Flask, jsonify

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Flask app for health checks
app = Flask(__name__)

@app.route('/')
@app.route('/health')
def health_check():
    """Health check endpoint for uptime monitoring"""
    bot_status = "online" if bot.is_ready() else "connecting"
    return jsonify({
        "status": "ok",
        "bot_status": bot_status,
        "uptime": "running"
    })

# --- API Fetch Function ---
async def get_image(api: str, endpoint: str = None):
    async with aiohttp.ClientSession() as session:
        if api == "waifu":
            url = f"https://api.waifu.pics/nsfw/{endpoint}"
            async with session.get(url) as resp:
                data = await resp.json()
                return data["url"]

        elif api == "nekos":
            url = f"https://nekos.best/api/v2/{endpoint}"
            async with session.get(url) as resp:
                data = await resp.json()
                return data["results"][0]["url"]

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
async def blowjob(ctx, member: discord.Member):
    img_url = await get_nsfw_image("blowjob")
    
    # Create a single embed with title, description, color, and image
    embed = discord.Embed(
        title="🔞 BlowJob",
        description=f"🔥 {ctx.author.mention} gives a blowjob to {member.mention}",
        color=discord.Color.purple()
    )
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

@bot.command()
async def pat(ctx, member: discord.Member = None):
    img_url = await get_image("nekos", "pat")
    if member:
        embed = discord.Embed(description=f"🤗 {ctx.author.mention} pats {member.mention}", color=discord.Color.green())
    else:
        embed = discord.Embed(description=f"🤗 {ctx.author.mention} needs pats!", color=discord.Color.green())
    embed.set_image(url=img_url)
    await ctx.send(embed=embed)


def run_flask():
    """Run Flask server in a separate thread"""
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    # Start Flask server in background thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    # Start Discord bot
    bot.run(os.getenv("DISCORD_TOKEN"))
