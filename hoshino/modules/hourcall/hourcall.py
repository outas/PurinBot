import pytz
from datetime import datetime
from hoshino import util
from hoshino.res import R
from hoshino.service import Service

# 设置不生效，优先读取配置文件设置
sv = Service('hourcall', enable_on_default=True)

def get_hour_call():
    """从HOUR_CALLS中挑出一组时报，每日更换，一日之内保持相同"""
    config = util.load_config(__file__)
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    hc_groups = config["HOUR_CALLS"]
    g = hc_groups[ now.day % len(hc_groups) ]
    return config[g]

@sv.scheduled_job('cron', hour='*', )
async def hour_call():
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    if now.hour == 23:
        await sv.broadcast(str(R.img('睡觉.jpg').cqcode), 'hourcall', 0)
        return

    if not now.hour % 6 == 0:
        return
        
    await sv.broadcast(str(R.img('买药.jpg').cqcode), 'hourcall', 0)
