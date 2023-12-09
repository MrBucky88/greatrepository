import discord
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import coinflip
# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
    for guild in bot.guilds:
        channel = guild.system_channel
        if channel is not None:
            await channel.send("Hello!ツ")

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem kapibarą botem o_0!')

@bot.command()
async def greenday(ctx):
    await ctx.send(f'I walk a lonely route, the only one that I have ever known')

@bot.command()
async def flip(ctx):
    await ctx.send(coinflip())


@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} właśnie dołączył {discord.utils.format_dt(member.joined_at)}')

bot.run("yeah no token for u guys, sry")



