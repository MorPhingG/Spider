import re
import urllib.request
import time
from selenium import webdriver
from bs4 import BeautifulSoup

class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        self.headers = { 'User-Agent' : self.user_agent }
        self.jokeList = []
        self.enable = False

    # get html source code
    def getHtml(self):
        url = "http://www.qiushibaike.com/hot/"
        req = urllib.request.Request(url, headers = self.headers)
        page = urllib.request.urlopen(req)
        html = page.read()
        return html

    def getJoke(self):
        html = self.getHtml()
        soup = BeautifulSoup(html)
        jokeTag = soup.find_all('div',{'class':'content'})
        for subJokeTag in jokeTag:
            self.jokeList.append(subJokeTag.string)

    def getOneJoke(self):
        for oneJoke in self.jokeList:
            inputKey = input()
            if inputKey == "Q":
                self.enable = False
                return
            print(oneJoke)

    def start(self):
        self.enable = True
        self.getJoke()
        self.getOneJoke()

spider = QSBK()
spider.start()




