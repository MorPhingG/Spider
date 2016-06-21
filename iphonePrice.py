import re
import urllib.request
import time
from selenium import webdriver

# get html source code
def getHtml(url):
    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req)
    html = page.read()
    return html

# get price
def getImg(html):
    html = html.decode("utf-8")
    reg = r'data-price="(.+?)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    regTitle = r'target="_blank" title="(.+?)"'
    imgreTitle = re.compile(regTitle)
    imglistTitle = re.findall(imgreTitle,html)
    return imglist, imglistTitle

# html = getHtml("http://search.jd.com/Search?keyword=%E8%8B%B9%E6%9E%9C%E6%89%8B%E6%9C%BA&enc=utf-8&qr=&qrst=UNEXPAND&as_key=title_key%2C%2C%E6%89%8B%E6%9C%BA&rt=1&stop=1&click=&psort=1&page=1")
# imglist, imglistTitle = getImg(html)
# result = dict(zip(imglistTitle, imglist))
# result = sorted(result.items(), key=lambda x:x[1],reverse=True)
# for key,value in result:
#     print(key,':',value)

url = "http://search.jd.com/Search?keyword=%E8%8B%B9%E6%9E%9C%E6%89%8B%E6%9C%BA&enc=utf-8&qr=&qrst=UNEXPAND&as_key=title_key%2C%2C%E6%89%8B%E6%9C%BA&rt=1&stop=1&click=&psort=1&page=1"
browser = webdriver.Firefox()
browser.get(url)
html = getHtml(url)
imglist, imglistTitle = getImg(html)
browser.find_element_by_class_name("pn-next").click()
time.sleep(0.3)
html = getHtml(browser.current_url)
imglistTemp,imglistTitleTemp = getImg(html)
imglist.extend(imglistTemp)
imglistTitle.extend(imglistTitleTemp)

browser.find_element_by_class_name("pn-next").click()
time.sleep(0.3)
html = getHtml(browser.current_url)
imglistTemp,imglistTitleTemp = getImg(html)
imglist.extend(imglistTemp)
imglistTitle.extend(imglistTitleTemp)

result = list(zip(imglistTitle, imglist))
result = sorted(result, key=lambda x:x[1],reverse=True)
for key,value in result:
    print(key,':',value)
browser.quit()