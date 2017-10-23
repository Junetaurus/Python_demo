# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
# 保存到 Redis 非关系型数据库中

import redis

class save_coupons_to_redis:
    def __init__(self, path):
        self.path = path
        print(self.path)

    def __connect(self):
        try:
            r = redis.StrictRedis(
                host='127.0.0.1',
                port=6379,
                db=0
            )
            print(r)
            return r
        except IOError:
            print('link redis error')

    def save_to_redis(self):
        r = self.__connect()
        path = self.path
        with open('coupons.txt', 'r') as f:
            r.set('coupons', f.readlines())
            r.save()
    def see_all(self):
        r = self.__connect()
        value =  r.get('coupons')
        print(value)
test = save_coupons_to_redis('coupons.txt')
test.save_to_redis()
test.see_all()
