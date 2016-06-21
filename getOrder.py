import re
import urllib.request
import time
from selenium import webdriver
from bs4 import BeautifulSoup

# get html source code
def getHtml(url):
    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req)
    html = page.read()
    return html

# get order
def getOrder(html):
    # html = html.decode("utf-8")
    regTitle = r'target="_blank" title="(.+?)"'
    orderReTitle = re.compile(regTitle)
    orderListTitle = re.findall(orderReTitle,html)
    return orderListTitle

if __name__ == '__main__':
    url = "https://passport.jd.com/new/login.aspx?ReturnUrl=http%3A%2F%2Fsearch.jd.com%2FSearch%3Fkeyword%3D%25E8%258B%25B9%25E6%259E%259C%25E6%2589%258B%25E6%259C%25BA%26enc%3Dutf-8%26qr%3D%26qrst%3DUNEXPAND%26as_key%3Dtitle_key%252C%252C%25E6%2589%258B%25E6%259C%25BA%26rt%3D1%26stop%3D1%26click%3D%26psort%3D1%26page%3D1"
    browser = webdriver.Firefox()                               # open firebox
    browser.get(url)
    browser.find_element_by_id("loginname").send_keys("18479285163")
    browser.find_element_by_id("nloginpwd").send_keys("9391012345bgtlTL")
    browser.find_element_by_id("loginsubmit").click()           # login in
    time.sleep(3)
    browser.find_element_by_class_name("fore2").find_element_by_class_name("dt").click()
    browser.switch_to_window(browser.window_handles[1])
    orderListTitle = getOrder(browser.page_source)
    time.sleep(3)
    print(orderListTitle)
    browser.quit()

