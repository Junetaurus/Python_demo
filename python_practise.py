#使用while循环输入 1 2 3 4 5 6     8 9 10
#-*-coding: utf-8-*-
a = 0
while a < 10:
    a += 1
    if a != 7:
        print(a, end=' ')

print('')

a = 0
while a < 10:
    a += 1
    if a == 7:
        continue
    print(a, end=' ')

print('')

#求1-100的所有数的和
a = 0
b = 1
while b <= 100:
    a = a + b
    b += 1
print(a)

a = 0
b = 1
for i in range(101):
    a += i
print(a)

# 输出 1-100 内的所有奇数
a = 1
while a <= 100:
    if a%2 != 0:
        print(a, end=' ')
    a += 1
print('')
# 输出 1-100 内的所有偶数
a = 1
while a <= 100:
    if a%2 == 0:
        print(a, end=' ')
    a += 1
print('')
# 求1-2+3-4+5 ... 99的所有数的和
a = 0
b = 0
while a < 99:
    a += 1
    if a%2 == 0:
        b += a
    else:
        b -= a
print(b)

a = 1
b = 0
c = 0
while a <= 100:
    if a%2 == 0:
        b += a
    else:
        c += a
    a += 1
print(c - b)

# 用户登陆（三次机会重试）
a = 0
while a < 3:
    name = input('请输入用户名: ')
    password = input('请输入用户密码: ')

    a += 1
    if name == '111' and password == '222':
        print('登入成功')
        exit()
    else:
        print('输入错误')
print('次数超过三次')
