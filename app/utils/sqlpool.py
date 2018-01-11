import time
import pymysql
import threading
from DBUtils.PooledDB import PooledDB, SharedDBConnection

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=5,  # 链接池中最多闲置的链接，0和None不限制
    maxshared=3,
    # 链接池中最多共享的链接数量，0和None表示全部共享。PS: 无用，因为pymysql和MySQLdb等模块的 threadsafety都为1，所有值无论设置为多少，_maxcached永远为0，所以永远是所有链接都共享。
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    host='47.93.252.50',
    port=3306,
    user='root',
    password='123456',
    database='userinfo',
    charset='utf8'
)


# def SQLHelper():
#     conn = POOL.connection()
#     cursor = conn.cursor()
#     cursor.execute('select * from user')
#     result = cursor.fetchall()
#     # print(result)
#     conn.close()
#     return result
class SQLHelper(object):

    def __init__(self):
        self.conn = None
        self.cursor = None

    def open(self,cursor=pymysql.cursors.DictCursor):
        self.conn = POOL.connection()
        self.cursor = self.conn.cursor(cursor=cursor)

    def close(self):
        self.cursor.close()
        self.conn.close()

    def fetchone(self,sql,params):
        cursor = self.cursor
        cursor.execute(sql,params)
        result = cursor.fetchone()

        return result

    def fetchall(self, sql, params):
        cursor = self.cursor
        cursor.execute(sql, params)
        result = cursor.fetchall()
        return result

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()