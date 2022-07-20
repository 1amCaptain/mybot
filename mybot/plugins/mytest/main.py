from nonebot.plugin import on_keyword, on_message
from nonebot.adapters.onebot.v11 import Bot,GroupMessageEvent,PrivateMessageEvent
from nonebot.matcher import Matcher
from nonebot.log import logger
from nonebot.adapters.onebot.v11.message import Message
from nonebot import on_command
from .main_computer.computerInfo import computerInfo
from .cod4.cod4 import cod4
async def user_checker(event: GroupMessageEvent) -> bool:
    # 852136096
    # logger.info(event.group_id)
    if str(event.group_id) == "144368524" :
        return True
    return False

# 查看当前内存
check = on_command('com',rule=user_checker) # 必须加上/ test 这样的格式才行
@check.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    try:
        logger.info(event.message)
        get_message = str(event.message) 
        if "mem" in get_message:
            computer_Info = computerInfo()
            used,free = computer_Info.MemInfo()
            await check.finish(Message(f"当前内存已使用{used}GB,空闲内存为{free}GB"))
    except Exception as e:
        logger.warning(e)

# cod4
cod4_command = on_command('cod4',rule=user_checker) # 必须加上/ cod4 这样的格式才行
@cod4_command.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    try:
        # logger.info("cod444444444444")
        cod4_action = cod4()
        fun_name = str(event.message)[6:]
        fun_list = cod4_action.returnFun()
        if fun_name in fun_list.keys():
            logger.info(fun_name)
            cod4_check_status,cod4_check_msg = cod4_action.Check_Server()
            if fun_name == 'start' and cod4_check_status:
                # logger.info("h1-mod运行中,请先输入指令进行关闭/cod4 close")
                await cod4_command.finish(Message(cod4_check_msg))
            cod4_status,cod4_msg = getattr(cod4_action,fun_list[fun_name])()
            if cod4_status:
                logger.info("执行成功")
                await cod4_command.finish(Message(cod4_msg))
            else:
                logger.info("执行失败")
                await cod4_command.finish(Message(cod4_msg))
        # else:
        #     logger.info("h1-mod运行中,请先输入指令进行关闭/cod4 close")
                # await cod4_command.finish(Message("执行失败"))
            # logger.info()
            # logger.info(cod4_fun)
            # logger.info(type(cod4_test))
            
    except Exception as e:
        logger.warning(e)
