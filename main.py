import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import sys, traceback


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def get_prefix(bot, message):

    prefixes = ['lol ', '!']

    if not message.guild:
        return '!'

    return commands.when_mentioned_or(*prefixes)(bot, message)

initial_extensions = ['cogs.IceCreamStuff','cogs.OtherStuff']

bot = commands.Bot(command_prefix=get_prefix, description='Your local ice-cream bot')

bot.remove_command('help')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('ice'):
        await message.add_reaction('🍨')

    await bot.process_commands(message)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')


bot.run(TOKEN, bot=True, reconnect=True)
