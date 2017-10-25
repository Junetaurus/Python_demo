# 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

class Input(object):
    def __init__(self):
        self.filtered_words = list()
        self.in_string = ''
        self.out_string = ''
        self.load_filtered_words()

    def load_filtered_words(self, filename='filtered_words.txt'):
        with open(filename, 'r') as file:
            for line in file.readlines():
                self.filtered_words.append(line.strip())

    def filter_words(self):
        self.out_string = self.in_string
        for word in self.filtered_words:
            if word in self.out_string:
                self.out_string = self.out_string.replace(word, len(word)*'*')

    def user_input(self, filename):
        if not filename:
            self.in_string = input('>')
        else:
            with open(filename, 'r') as f:
                self.in_string = f.read()

    def std_output(self):
        self.filter_words()
        print(self.out_string)

if __name__ == '__main__':
    i = Input()
    i.user_input('')
    i.std_output()
