import re
import urllib.request
import time
from selenium import webdriver
from bs4 import BeautifulSoup

class ZH:

    def __init__(self):
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }
        self.urlList = []
        self.jokeList = []
        self.questionIndex = 1
        self.enable = False

    # get urls of questions
    def getUrlList(self):
        url = "http://www.zhihu.com/search?type=content&q=%E6%B1%A1%E7%AC%91%E8%AF%9D"
        html = self.getHtml(url)
        html = html.decode("utf-8")
        regTitle = r'target="_blank" href="/question(.+?)"'
        orderReTitle = re.compile(regTitle)
        self.urlList = re.findall(orderReTitle, html)
        for i in range(len(self.urlList)):
            self.urlList[i] = "http://www.zhihu.com/question" + self.urlList[i]

    # get html source code
    def getHtml(self, url):
        req = urllib.request.Request(url, headers = self.headers)
        page = urllib.request.urlopen(req)
        html = page.read()
        return html

    def getJoke(self):
        self.jokeList = []
        html = self.getHtml(self.urlList[self.questionIndex])
        soup = BeautifulSoup(html, "lxml")
        jokeTag = soup.find_all('div',{'class':'zm-editable-content clearfix'})
        for subJokeTag in jokeTag:
            self.jokeList.append(subJokeTag.text)

    def getOneJoke(self):
        for oneJoke in self.jokeList:
            inputKey = input()
            if inputKey == "Q":
                self.enable = False
                return
            print(oneJoke)

    def start(self):
        self.enable = True
        self.getUrlList()
        print("按回车获得笑话,'Q'退出(q无效,抱歉)")
        while self.questionIndex < self.urlList.__len__():
            self.getJoke()
            self.getOneJoke()
            if self.enable == False:
                return
            self.questionIndex = self.questionIndex+1
            print("下面进入另一个问题")
        print("我已经没有问题啦")

spider = ZH()
spider.start()