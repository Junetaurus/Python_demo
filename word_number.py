# 任一个英文的纯文本文件，统计其中的单词出现的个数。
from collections import Counter

f = open('subtitle.txt', 'r')

c = Counter()

for line in f:
    words = line.split()
    # print(words)
    c += Counter(words)

print(c)

for words in c.most_common():
    print(words)