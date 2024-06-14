import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello!')

@bot.command()
async def greet(ctx, name: str):
    await ctx.send(f'Xin chào, {name}!')

@bot.event
async def on_message(message):
    # Nếu tin nhắn được gửi bởi bot thì bỏ qua
    if message.author == bot.user:
        return

    # Ví dụ: Phản hồi "Hello" nếu tin nhắn chứa từ "xin chào"
    if 'bot' in message.content.lower():
        await message.channel.send(f'hả , {message.author.name}!')

    # Ví dụ: Phản hồi với "Tạm biệt" nếu tin nhắn chứa từ "tạm biệt"
    if 'tạm biệt' in message.content.lower():
        await message.channel.send('Tạm biệt! Hẹn gặp lại!')

    # Xử lý tin nhắn chứa cụm từ "bot quà hằng ngày pixelmon"
    if 'bot pixelmon' in message.content.lower():
        # Danh sách các giá trị quà tặng
        rewards = [20000, 30000,30000,30000, 50000]
        # Chọn ngẫu nhiên một giá trị từ danh sách
        reward = random.choice(rewards)
        admin_id = 539647978131161099
        admin_mention = f'<@{admin_id}>'
        # Gửi tin nhắn phản hồi
        await message.channel.send(f'Quà đăng nhập hôm nay của {message.author.mention} là {reward}POKEDOLAR!')
        await message.channel.send(f'{admin_mention} vô phát quà đi m!')

    # Đảm bảo bot vẫn xử lý các lệnh khác nếu có
    await bot.process_commands(message)

bot.run('MTI1MDgyNDgwNTg5MzAxNzc4MQ.GM_iNk.9YlxzqgnbRdGoHTtbhVBRhGbTPcEjHC3wXqC-A')
