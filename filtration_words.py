# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。

class Input(object):
    def __init__(self):
        self.filtered_words = list()
        self.in_string = ''
        self.out_string = 'Human Rights'
        self.load_filtered_words()

    def load_filtered_words(self, filename='filtered_words.txt'):
        with open(filename, 'r') as file:
            for line in file.readlines():
                self.filtered_words.append(line.strip())

    def filter_words(self):
        for word in self.filtered_words:
            if self.in_string.find(word) != -1:
                self.out_string = 'Freedom'
                return

    def user_input(self):
        self.in_string = input('>')

    def std_output(self):
        self.filter_words()
        print(self.out_string)

if __name__ == '__main__':
    i = Input()
    i.user_input()
    i.std_output()
