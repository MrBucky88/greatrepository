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

@bot.command()
async def ekologia(ctx):
    with open('images/eco1.jpg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
    await ctx.send(f'Ekologia to nauka o strukturze i funkcjonowaniu przyrody, zajmująca się badaniem oddziaływań pomiędzy organizmami a ich środowiskiem oraz wzajemnie między tymi organizmami (czyli strukturą ekosystemów).')
    await ctx.send(f'Po więcej informacji użyj komendy $jakbyceko')


@bot.command()
async def jakbyceko(ctx):
    with open('images/eco2.jpg', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
    await ctx.send(f'Jak być eco #gogreen!')
    await ctx.send(f'-Segreguj odpady. \n -Oszczędzaj wodę i prąd. \n -Interesuj się eko wydarzeniami. \n -Naprawiaj uszkodzone sprzęty elektroniczne. \n -Korzystaj z ekologicznych środków transportu. \n -Nie pal w piecu śmieciami. \n -Kupuj przedmioty używane.')
    await ctx.send(f'By zobaczyć wspaniałe ekologiczne arcydzieła użyj komendy $greenart')


@bot.command()
async def ecoart(ctx):
    with open('images/statue.png', 'rb') as f:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
    await ctx.send(f'To jest przepiękne dzieło stworzone z niedopałków papierosów. Niemożliwe prawda?!?')
    
    with open('images/statue2.png', 'rb') as g:
        # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
        picturetwo = discord.File(g)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picturetwo)
    await ctx.send(f'To jest hełm Dartha Vadera stworzony z puszek po napojach.')
    
@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem kapibarą botem o_0!')

@bot.command()
async def help(ctx):
    await ctx.send(f'Lista komend! \n $ekologia - wyjaśnia pojęcie \n jakbyceko - pomysły na bycie eko \n $ecoart - pokazuje przykłady bycia eko ')

bot.run("MTE3NzkyMjM3NzU1Mjc2NDk2OA.Gv9dQG.26l80eSznCIpYEeDO6wiDy5IstBk0A4yPNeDyo")



