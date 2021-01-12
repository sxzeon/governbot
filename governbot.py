import discord

token = "TOKEN"
text = "**욕설 사용** \n> 욕설이 감지되었습니다."

app = discord.Client()
client = discord.Client()

version = "0.1"

@app.event
async def on_ready():
    print("정상적으로 로그인되었습니다")
    print(app.user.name)
    print(app.user.id)
    print("=========================")

@app.event
async def on_message(message):
    if message.content.startswith("병신"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("시발"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("ㅅㅂ"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("ㅈ"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("ㅈ"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("좆"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("새끼"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("개샊"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("개새끼"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("ㅈㄹ"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("지랄"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("즤랄"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("지랄"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("뒤져"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("디져"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("조ㅈ"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("쉬발"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("존나"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("ㅈㄴ"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("ㅗ"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("뻐큐"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("FUCXING"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("fucxing"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("fuck"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("fucking"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("FUCK"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("FUCKING"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("또라이"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("돌아이"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("돌+I"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("돌I"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("돌i"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("돌+i"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("tlqkf"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("TLQKF"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("!도움말"):
        channel = message.channel
        embed=discord.Embed(title="도움말", description="안녕하세요, 저는 제온님이 개발하신 봇이예요! 기능들을 설명할게요.", color=0x7ad110)
        embed.add_field(name="욕설 검열", value="시X 등의 욕설을 할 시 검열합니다", inline=False)
        embed.add_field(name="그 외의 기능들은...", value="준비 중이예요!", inline=False)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("She발"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("시팔"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("십8"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)

    if message.content.startswith("시8"):
        channel = message.channel
        await message.delete()
        await message.channel.send(text)
        
app.run(token)
