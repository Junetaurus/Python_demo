# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

#-*-coding: utf-8-*-

import uuid

class coupons_N_keys:
    def __init__(self):
        self.num = 0;
        self.list = []

    def coupons(self, num):
        for i in range(num):
            self.list.append(uuid.uuid1())

    def return_list(self):
            return self.list;

test = coupons_N_keys()
test.coupons(200)
keys = test.return_list()
print(keys)
print(len(keys))

def writeToText(list_name, file_path):
    try:
        f = open(file_path, 'w')
        for item in list_name:
            f.write(str(item) + '\n\n')
        f.close()
    except IOError:
        print('write file fail')

writeToText(keys, 'coupons.txt')
