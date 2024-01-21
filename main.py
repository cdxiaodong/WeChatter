# 项目启动文件
import uvicorn

from wechatter.bot.bot_info import BotInfo
from wechatter.config.config_reader import ConfigReader
from wechatter.sqlite.sqlite_manager import SqliteManager
from wechatter.utils.file_manager import FileManager

# 启动命令：python main.py


cr = ConfigReader("config.ini")


def main():
    # TODO: 检测command_set文件配置是否合理
    BotInfo.update_name(cr.bot_name)
    # 创建文件夹
    FileManager.check_and_create_folder("data/qrcodes")
    FileManager.check_and_create_folder("data/todos")
    FileManager.check_and_create_folder("data/text_image")
    # 创建文件
    FileManager.check_and_create_file("data/wechatter.sqlite")
    # 创建数据库表
    sqlite_manager = SqliteManager("data/wechatter.sqlite")
    sqlite_manager.excute_folder("wechatter/sqlite/sqls")

    from wechatter.app.app import app

    uvicorn.run(app, host="0.0.0.0", port=cr.recv_port)


if __name__ == "__main__":
    main()
