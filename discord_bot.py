import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.') #serve a definire il prefisso dei comandi


#EVENTI
@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_member_join(member):
    print(f'{member} è **ENTRATO**')

@client.event
async def on_member_left(member):
    print(f'{member} è **USCITO**')

@client.event
async def on_member_banned(member):
    print(f'{member} è stato **BANNATO**')

#COMANDI
try:
    @client.command()
    async def commands(ctx):
        await ctx.send('''**This is the list of all my commands!** 
        •hello ---> to write "Hi"
        •HappyBirthday ---> to wish an happy birthday!
        •ping ---> to check your ping 
        *ps: use the prefix '.' before the commands*
        ''')

    @client.command()
    async def hello(ctx):
        await ctx.send("Hi")

    @client.command()
    async def HappyBirthday(ctx):
        await ctx.send("Happy Birthday!!! :partying_face: :confetti_ball: :tada:\n" * 5)

    @client.command()
    async def ping(ctx):
        await ctx.send(f'Il tuo ping è di **{round(client.latency * 100*2)}ms**')

    @client.command(pass_context = True)
    async def join(ctx):
        channel = ctx.message.author.voice.voice_channel
        await client.join_voice_channel(channel)

except discord.ext.commands.errors.CommandNotFound:
    print("Comando non valido!")


#serve per collegarsi al bot ---> preleva il suo TOKEN
client.run("ODExNTQyNjcyNDkzNTEwNjg3.YCzuAg.gDOs9gRHBrEbGjlXyMTfC2wsO1w")