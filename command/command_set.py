# 命令集
from command_invoker import CommandInvoker


cmd_dict = {
    "None": {"keys": ["None"], "desc": "无效指令。", "value": 0, "func": None},
    "help": {
        "keys": ["帮助", "help"],
        "desc": "获取帮助信息。",
        "value": 1,
        "func": CommandInvoker.cmd_help,
    },
    "gpt4": {
        "keys": ["gpt", "gpt4"],
        "desc": "调用GPT4进行回答。",
        "value": 20,
        "func": CommandInvoker.cmd_gpt4,
    },
    "gpt4-chats": {
        "keys": ["gpt4-chats", "gpt4对话记录"],
        "desc": "列出GPT4对话记录。",
        "value": 21,
        "func": CommandInvoker.cmd_gpt4_chats,
    },
    "gpt4-continue": {
        "keys": ["gpt4-continue", "gpt4继续"],
        "desc": "继续GPT4对话。",
        "value": 22,
        "func": CommandInvoker.cmd_gpt4_continue,
    },
    "gpt4-record": {
        "keys": ["gpt4-record", "gpt4记录"],
        "desc": "获取GPT4对话记录。",
        "value": 23,
        "func": CommandInvoker.cmd_gpt4_record,
    },
    "gpt35": {
        "keys": ["gpt35", "gpt3.5"],
        "desc": "调用GPT3.5进行回答。",
        "value": 30,
        "func": CommandInvoker.cmd_gpt35,
    },
    "github-trending": {
        "keys": ["github趋势", "github-trending"],
        "desc": "获取github趋势。",
        "value": 5,
        "func": CommandInvoker.cmd_github_trending,
    },
    "bili-hot": {
        "keys": ["b站热搜", "bili-hot"],
        "desc": "获取b站热搜。",
        "value": 6,
        "func": CommandInvoker.cmd_bili_hot,
    },
    "zhihu-hot": {
        "keys": ["知乎热搜", "zhihu-hot"],
        "desc": "获取知乎热搜。",
        "value": 7,
        "func": CommandInvoker.cmd_zhihu_hot,
    },
    "weibo-hot": {
        "keys": ["微博热搜", "weibo-hot"],
        "desc": "获取微博热搜。",
        "value": 8,
        "func": CommandInvoker.cmd_weibo_hot,
    },
    "weather": {
        "keys": ["天气", "weather"],
        "desc": "获取天气。",
        "value": 9,
        "func": None,
    },
    "word": {
        "keys": ["word", "单词"],
        "desc": "解释单词(词、成语)。",
        "value": 10,
        "func": CommandInvoker.cmd_word,
    },
    "tran": {
        "keys": ["tran", "翻译"],
        "desc": "翻译英文句子。",
        "value": 11,
        "func": None,
    },
    "people": {
        "keys": ["people", "人民日报"],
        "desc": "发送今天人民日报的PDF。",
        "value": 12,
        "func": None,
    },
    "today-in-history": {
        "keys": ["today-in-history", "历史上的今天"],
        "desc": "历史上的今天。",
        "value": 13,
        "func": CommandInvoker.cmd_today_in_history,
    },
    "douyin-hot": {
        "keys": ["抖音热搜", "douyin-hot"],
        "desc": "获取抖音热搜。",
        "value": 14,
        "func": CommandInvoker.cmd_douyin_hot,
    },
    "pai-post": {
        "keys": ["派早报", "pai-post"],
        "desc": "获取少数派早报。",
        "value": 15,
        "func": CommandInvoker.cmd_pai_post,
    },
    "qrcode": {
        "keys": ["qrcode", "二维码"],
        "desc": "生成二维码。",
        "value": 16,
        "func": CommandInvoker.cmd_qrcode,
    },
    "todo": {
        "keys": ["待办事项", "todo", "待办"],
        "desc": "待办事项。",
        "value": 17,
        "func": CommandInvoker.cmd_todo,
    },
    "rmtd": {
        "keys": ["删除待办事项", "删除待办", "rmtd", "rm-todo", "remove-todo"],
        "desc": "删除待办事项。",
        "value": 18,
        "func": CommandInvoker.cmd_remove_todo,
    },
    "schedule": {
        "keys": ["课程表", "schedule"],
        "desc": "课程表。",
        "value": 19,
        "func": None,
    },
}
