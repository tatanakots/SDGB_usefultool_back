# This file contains the config of the whole project.
# DO NOT share your crtical info to others.
# Change the file name from .settings.py to settings.py.

# 程序设置

app_debug = False
app_host = "0.0.0.0"
app_port = 5600

# 游戏设置

game_title_ver = "1.41"
game_rom_ver = "1.41.00"
game_data_ver = "1.40.11"

# 机厅信息

regionId = 1                    # 地区ID
regionName = "北京"             # 地区名
placeId = 1234                  # 机厅ID
placeName = "舞萌DX超级科技店"   # 机厅名
clientId = "A63E01E1145"        # 客户端ID（狗号去掉最后四位）

# 数据库信息

db_type = "sqlite"
db_host = "127.0.0.1"
db_port = 3306
db_username = "root"
db_password = "123456"
db_name = "maimai"
db_sqlite_path = "default.db"
db_setdb_lock = False