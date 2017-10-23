# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
# 保存到 MySQL 关系型数据库中

import pymysql

class save_coupons_to_mysql:
    def __init__(self, path):
        self.path = path
        print(self.path)

    def __connect(self):
        try:
            # 创建连接
            conn = pymysql.Connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                passwd='123456',
                db='python',
                charset='utf8'
            )
            print(conn)
            return conn
        except IOError:
            print('link mysql error')

    def save_to_mysql(self):
        conn = self.__connect()
        path = self.path
        #创建游标
        cursor = conn.cursor()
        cursor.execute('drop table if exists coupons_keys')
        cursor.execute('create table coupons_keys (id int(8) primary key, coupons_keys varchar(50))')
        row = 0
        with open('coupons.txt', 'r') as f:
            for line in f.readlines():
                coupons_keys = line.rstrip()
                cursor.execute('insert into coupons_keys (id, coupons_keys) values (%s, %s)', [row, coupons_keys])
                row += 1
        conn.commit()
        cursor.close()
        conn.close()

    def see_all(self):
        conn = self.__connect()
        cursor = conn.cursor()
        cursor.execute('select * from coupons_keys')

        # 获取剩余结果的第一行数据
        # row_1 = cursor.fetchone()
        # 获取剩余结果前n行数据
        # row_2 = cursor.fetchmany(3)
        # 获取剩余结果所有数据
        # row_3 = cursor.fetchall()

        values = cursor.fetchall()
        print(values)
        cursor.close()
        conn.close()

test = save_coupons_to_mysql('coupons.txt')
test.save_to_mysql()
test.see_all()
