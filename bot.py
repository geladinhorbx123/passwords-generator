import discord
from password import senha
from discord.ext import commands
# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def Senhas(ctx,count = 5):
    await ctx.send(f'Aqui estão algumas senhas que você pode usar: {senha(count)}')

bot.run("TOKEN HERE")
