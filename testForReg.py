import re
import urllib.request

def getHtml(url):
    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req)
    html = page.read()
    return html

def getImg(html):
    html = html.decode("gbk")
    reg = r'src="(http.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    print(imglist)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
html = getHtml("http://www.meizitu.com/")
getImg(html)