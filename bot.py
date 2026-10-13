import discord
from password import senha

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('oi'):
        await message.channel.send("Olá!")
    elif message.content.startswith('tchau'):
        await message.channel.send("Até mais! XD")
    elif message.content.startswith('senha'):
        await message.channel.send(senha(tamanho=16))
    elif message.content.startswith('me de qualquer senha'):
        await message.channel.send(f"aqui sua senhas qualquer: {senha(tamanho=16)}")
    else:
        await message.channel.send("Desculpe, não fui programado para responder a isso.")

client.run("TOKEN HERE!")
