# dbconfig.py

import os
from settings import db_type, db_host, db_port, db_username, db_password, db_name, db_sqlite_path

class Config:
    # 默认使用 SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+str(db_sqlite_path)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class MySQLConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://'+str(db_username)+':'+str(db_password)+'@'+str(db_host)+':'+str(db_port)+'/'+str(db_name)

class MariaDBConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'+str(db_username)+':'+str(db_password)+'@'+str(db_host)+':'+str(db_port)+'/'+str(db_name)

# 你可以在运行时动态选择配置
def get_database_config():
    if db_type == "mysql":
        return MySQLConfig
    elif db_type == "mariadb":
        return MariaDBConfig
    else:
        return Config
