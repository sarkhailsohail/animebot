import discord
from discord.ext import commands
import aiohttp

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

# --- API Fetch Functions ---
async def get_nsfw_image(endpoint):
    url = f"https://api.waifu.pics/nsfw/{endpoint}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return data["url"]

async def get_sfw_image(endpoint):
    url = f"https://api.waifu.pics/sfw/{endpoint}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return data["url"]

# --- Helper for SFW actions ---
async def sfw_action(ctx, action: str, emoji: str, color: discord.Color, member: discord.Member = None):
    img_url = await get_sfw_image(action)
    if member:
        desc = f"{emoji} {ctx.author.mention} {action}s {member.mention}"
    else:
        desc = f"{emoji} {ctx.author.mention} does {action}!"
    embed = discord.Embed(description=desc, color=color)
    embed.set_image(url=img_url)
    await ctx.send(embed=embed)

# --- NSFW Commands ---
@bot.command()
@commands.is_nsfw()
async def blowjob(ctx, member: discord.Member = None):
    img_url = await get_nsfw_image("blowjob")
    desc = f"🔥 {ctx.author.mention} gives {member.mention} a blowjob" if member else f"🔥 {ctx.author.mention} is feeling naughty..."
    embed = discord.Embed(description=desc, color=discord.Color.red())
    embed.set_image(url=img_url)
    await ctx.send(embed=embed)

# --- SFW Commands ---
@bot.command()
async def cry(ctx):
    await sfw_action(ctx, "cry", "😭", discord.Color.blue())

@bot.command()
async def cuddle(ctx, member: discord.Member = None):
    await sfw_action(ctx, "cuddle", "🤗", discord.Color.pink(), member)

@bot.command()
async def hug(ctx, member: discord.Member = None):
    await sfw_action(ctx, "hug", "🤗", discord.Color.green(), member)

@bot.command()
async def lick(ctx, member: discord.Member = None):
    await sfw_action(ctx, "lick", "👅", discord.Color.orange(), member)

@bot.command()
async def pat(ctx, member: discord.Member = None):
    await sfw_action(ctx, "pat", "🙃", discord.Color.purple(), member)

@bot.command()
async def smug(ctx):
    await sfw_action(ctx, "smug", "😏", discord.Color.dark_orange())

@bot.command()
async def smile(ctx):
    await sfw_action(ctx, "smile", "😊", discord.Color.teal())

@bot.command()
async def yeet(ctx, member: discord.Member = None):
    await sfw_action(ctx, "yeet", "💨", discord.Color.blue(), member)

@bot.command()
async def bonk(ctx, member: discord.Member = None):
    await sfw_action(ctx, "bonk", "🔨", discord.Color.dark_red(), member)

@bot.command()
async def wave(ctx):
    await sfw_action(ctx, "wave", "👋", discord.Color.gold())

@bot.command()
async def highfive(ctx, member: discord.Member = None):
    await sfw_action(ctx, "highfive", "🙌", discord.Color.green(), member)

@bot.command()
async def handhold(ctx, member: discord.Member = None):
    await sfw_action(ctx, "handhold", "🤝", discord.Color.blurple(), member)

@bot.command()
async def dance(ctx):
    await sfw_action(ctx, "dance", "💃", discord.Color.purple())

@bot.command()
async def bite(ctx, member: discord.Member = None):
    await sfw_action(ctx, "bite", "🦷", discord.Color.dark_blue(), member)

@bot.command()
async def slap(ctx, member: discord.Member = None):
    await sfw_action(ctx, "slap", "🖐️", discord.Color.red(), member)

@bot.command()
async def kill(ctx, member: discord.Member = None):
    await sfw_action(ctx, "kill", "☠️", discord.Color.dark_gray(), member)

@bot.command()
async def wink(ctx):
    await sfw_action(ctx, "wink", "😉", discord.Color.magenta())

@bot.command()
async def kick(ctx, member: discord.Member = None):
    await sfw_action(ctx, "kick", "🦵", discord.Color.dark_gold(), member)

@bot.command()
async def happy(ctx):
    await sfw_action(ctx, "happy", "😄", discord.Color.green())

@bot.command()
async def poke(ctx, member: discord.Member = None):
    await sfw_action(ctx, "poke", "👉", discord.Color.orange(), member)

@bot.command()
async def nom(ctx):
    await sfw_action(ctx, "nom", "🍴", discord.Color.light_gray())

@bot.command()
async def blush(ctx):
    await sfw_action(ctx, "blush", "😊", discord.Color.pink())

@bot.command()
async def glomp(ctx, member: discord.Member = None):
    await sfw_action(ctx, "glomp", "💥", discord.Color.dark_purple(), member)

@bot.command()
async def cringe(ctx):
    await sfw_action(ctx, "cringe", "😬", discord.Color.dark_magenta())

@bot.command()
async def bully(ctx, member: discord.Member = None):
    await sfw_action(ctx, "bully", "😈", discord.Color.dark_red(), member)


# --- Run the Bot ---
bot.run("YOUR_TOKEN_HERE")
