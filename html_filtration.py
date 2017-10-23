# 一个HTML文件，找出里面的正文  链接

from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc

# class TeHTMLParser(HTMLParser):