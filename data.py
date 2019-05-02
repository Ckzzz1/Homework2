import sqlite3
from collector import *


class DATA():
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.selection = None

    # 初始化数据库
    def init(self):
        self.conn = sqlite3.connect('./data/data.db')
        print("Opened database successfully")
        self.cursor = self.conn.cursor()

    # 创建数据库
    def create(self):
        self.cursor.execute('''CREATE TABLE INFO
                                   (YEAR                INT      NULL,
                                    年末总人口           FLOAT    NULL,
                                    男性人口             INT      NULL,
                                    女性人口             INT      NULL,
                                    经济活动人口         INT      NULL,
                                    农业总产值           INT      NULL,
                                    林业总产值           INT      NULL,
                                    牧业总产值           INT      NULL,
                                    渔业总产值           INT      NULL);''')
        print("Table created successfully")
        for year in range(1999, 2019):
            self.conn.execute("INSERT INTO INFO (YEAR) VALUES (" + str(year) + ")")

        print("Table init successfully")

    # 更新数据库
    def update(self, name, dict):
        for year in dict.keys():
            self.cursor.execute(
                "UPDATE INFO set " + name.upper() + " = " + str(dict[year]) + " where YEAR=" + str(year))
        self.conn.commit()
        print("Total number of rows updated :", self.conn.total_changes)

    # 选择数据
    def select(self, name):
        self.selection = {}
        cursor = self.cursor.execute("SELECT YEAR, " + name.upper() + "  from INFO")
        for row in cursor:
            self.selection[row[0]] = row[1]

    # 保存数据
    def save(self):
        self.conn.commit()
        self.conn.close()