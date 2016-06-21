import urllib.request
import re

# search = "https://www.baidu.com/s?ie=UTF-8&wd=haha"
# response = urllib.request.urlopen(search)  #接受反馈的信息
# the_page = response.read()  #读取反馈的内容
#
# def geturl(url):
#     url = url.decode()
#     reg = r'(http://)?((www)?\.[^/]*)(/[^/]/htm)?'
#     urlre = re.compile(reg)
#     urllist = re.findall(urlre,url)
#     return urllist
# urllist = geturl(the_page)

def getImg(html):
    html = html.decode()
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1

url = "http://tieba.baidu.com/p/2460150866"


user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
values = {'name' : 'WHY',
          'location' : 'SDU',
          'language' : 'Python' }
data = urllib.parse.urlencode(values)
data = data.encode(encoding='UTF8')
headers = { 'User-Agent' : user_agent}

req = urllib.request.Request(url,data,headers)
response = urllib.request.urlopen(req)  #接受反馈的信息
the_page = response.read()  #读取反馈的内容

getImg(the_page)





# import urllib
#
# page = 4
# url = 'http://www.qiushibaike.com/hot/page/' + str(page)
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# headers = { 'User-Agent' : user_agent }
# try:
#     request = urllib.request.Request(url,headers = headers)
#     response = urllib.request.urlopen(request)
# except urllib.error.URLError as e:
#     if hasattr(e,"code"):
#         print(e.code)
#     if hasattr(e,"reason"):
#         print(e.reason)
#
# content = response.read().decode('utf-8')
# pattern = re.compile('<div.*?author">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
#                          'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
# items = re.findall(pattern,content)
# for item in items:
#     print(item[0],item[1],item[2],item[3],item[4])






#
#
#
# url='https://www.zhihu.com/question/22591304/followers'
# #感觉这个话题下面美女多
# headers={省略}
# i=1
# for x in xrange(20,3600,20):
#     data={'start':'0',
#         'offset':str(x),
#         '_xsrf':'a128464ef225a69348cef94c38f4e428'}
# #知乎用offset控制加载的个数，每次响应加载20
#     content=requests.post(url,headers=headers,data=data,timeout=10).text
# #用post提交form data
#     imgs=re.findall('<img src=\\\\\"(.*?)_m.jpg',content)
# #在爬下来的json上用正则提取图片地址，去掉_m为大图

