from loguru import logger

from wechatter.commands.handlers import command
from wechatter.models.message import SendMessage, SendMessageType, SendTo
from wechatter.sender import Sender
from wechatter.utils import get_request_json


@command(
    command="weibo-hot",
    keys=["微博热搜", "weibo-hot"],
    desc="获取微博热搜。",
    value=130,
)
def weibo_hot_command_handler(to: SendTo, message: str = "") -> None:
    try:
        response = get_weibo_hot_str()
        Sender.send_msg(to, SendMessage(SendMessageType.TEXT, response))
    except Exception as e:
        error_message = f"获取微博热搜失败，错误信息: {str(e)}"
        logger.error(error_message)
        Sender.send_msg(to, SendMessage(SendMessageType.TEXT, error_message))


def get_weibo_hot_str() -> str:
    r_json = get_request_json(
        url="https://m.weibo.cn/api/container/getIndex?containerid=106003%26filter_type%3Drealtimehot"
    )
    try:
        hot_list = r_json.get("data").get("cards")[0].get("card_group")[:20]
    except (ValueError, AttributeError):
        logger.error("微博列表返回值格式错误")
        raise Exception("微博列表返回值格式错误")

    if not hot_list:
        return "微博热搜列表为空"

    hot_search_str = "✨=====微博热搜=====✨\n"
    for i, hot_search in enumerate(hot_list[:20]):
        hot_search_str += f"{i + 1}. {hot_search.get('desc')}\n"
    return hot_search_str
