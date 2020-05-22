import random
from datetime import timedelta

from nonebot import on_command
from hoshino import util
from hoshino.res import R
from hoshino.service import Service, Privilege as Priv

# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'))
async def say_hello(session):
    await session.send(R.img('看手机.jpg').cqcode)


sv = Service('chat', manage_priv=Priv.SUPERUSER, visible=False)

@sv.on_command('沙雕机器人', aliases=('沙雕機器人',), only_to_me=False)
async def say_sorry(session):
    pic_index = random.randint(1, 2)
    await session.send(R.img(f"sbot{pic_index}.jpg").cqcode)

@sv.on_command('老婆', aliases=('waifu', 'laopo'), only_to_me=True)
async def chat_waifu(session):
    if not sv.check_priv(session.ctx, Priv.SUPERUSER):
        await session.send(R.img('laopo.jpg').cqcode)
    else:
        await session.send('mua~')

@sv.on_command('老公', only_to_me=True)
async def chat_laogong(session):
    await session.send(R.img('爬.jpg').cqcode , at_sender=True)

@sv.on_command('mua', only_to_me=True)
async def chat_mua(session):
    if not sv.check_priv(session.ctx, Priv.SUPERUSER):
        pic = R.img('偷笑.jpg').cqcode
        await session.send(f'四斋蒸鹅心\n{pic}', at_sender=True)
    else:
        pic = R.img('得意.jpg').cqcode
        await session.send(f'笨蛋~\n{pic}', at_sender=True)

@sv.on_command('来份布丁', aliases=('来份一布丁','来点布丁'), only_to_me=False)
async def seina(session):
    await session.send(R.img('purin.jpg').cqcode)

@sv.on_command('我有个朋友说他好了', aliases=('我朋友说他好了', ), only_to_me=False)
async def ddhaole(session):
    pic = R.img('疑问.jpg').cqcode
    await session.send(f'那个朋友是不是你弟弟？\n{pic}')

@sv.on_command('我好了', only_to_me=False)
async def nihaole(session):
    await session.send('不许好，憋回去！')
    await util.silence(session.ctx, 30)

@sv.on_command('?', aliases=('？'), only_to_me=False)
async def question(session):
    await session.send(R.img('问号.jpg').cqcode)
    await util.silence(session.ctx, 30)

@sv.on_command('🍮', aliases=('🍮🍮','🍮🍮🍮'), only_to_me=False)
async def purin(session):
    await session.send(R.img('吃布丁.jpg').cqcode)
# ============================================ #

@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.50:
        await bot.send(ctx, R.img('确实.jpg').cqcode)

@sv.on_keyword(('会战', '刀'))
async def chat_clanba(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, R.img('我的天啊你看看都几点了.jpg').cqcode)

@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.20:
        await bot.send(ctx, R.img('内鬼.png').cqcode)
