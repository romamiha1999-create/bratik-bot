import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

word_count = 0
target_words = ["братик", "братику", "братика"]

@bot.event
async def on_ready():
    print(f'✅ Бот запущений як {bot.user}')

@bot.event
async def on_message(message):
    global word_count
    if message.author.bot:
        return

    msg = message.content.lower()
    if any(word in msg for word in target_words):
        word_count += 1
        await message.channel.send(f"🔢 Слово «братик» зустрілося вже {word_count} разів!")

    await bot.process_commands(message)

bot.run(os.getenv("TOKEN"))
