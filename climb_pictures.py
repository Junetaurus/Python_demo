# 爬图片的程序

#-*-coding: utf-8-*-

import requests
from pyquery import PyQuery
from urllib.request import urlopen

class DownLoadImage(object):
    def __init__(self):
        self.urls = list()
        self.url = ''
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Safari/604.1.38'
        }
        self.s = requests.session()
        self.s.headers.update(self.headers)

    def get_image_url(self, url):
        self.url = url
        resp = self.s.get(self.url)
        doc = PyQuery(resp.content.decode())
        imgs = doc.find('img.BDE_Image')
        for img in imgs.items():
            self.urls.append(img.attr('src'))

    def save(self):
        for i in range(len(self.urls)):
            url = self.urls[i]
            print(url)
            resp = self.s.get(url)
            filename = 'img' + str(i) + '.jpg'
            with open(filename, 'wb') as file:
                file.write(resp.content)

    def download(self, url):
        if not url.strip():
            print('url is null')
            return
        self.get_image_url(url)
        self.save()

if __name__ == '__main__':
    d = DownLoadImage()
    d.download('https://tieba.baidu.com/p/5164619733')