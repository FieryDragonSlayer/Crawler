
import urllib
from urllib import request
from  http import cookiejar
#最简单的爬虫代码，始 19.3.4
'''
page = request.urlopen('http://tieba.baidu.com/p/1753935195')#打开网页
htmlcode = page.read()#读取页面源码
htmlcode = htmlcode.decode("utf-8")
with open(r'D:\Desktop\19.03.04.txt','r+') as f:
    f.write(htmlcode)
 '''
#最简单的爬虫代码，终19.3.4

# 1Post格式的请求访问，始 19.3.4
'''
LoginValue ={}
LoginValue['username'] = 'nishishei545@163.com'
LoginValue['password'] = 'piannide'
data = urllib.parse.urlencode(LoginValue).encode('utf-8')
request = urllib.request.Request('http://www.163.com/?')
resource = urllib.request.urlopen(request,data)
ret = resource.read()
print(ret)
'''
# 1Post格式的请求访问，终 19.3.4

'''
#添加header模仿浏览器进行爬虫,始 19.3.6
hearder = {"user-agent":"Mozilla/5.0"}
url = 'https://baike.baidu.com/item/android/60243'
req = request.Request(url, headers=hearder)
response = urllib.request.urlopen(req)
htmlcode = response.read()#读取页面源码
print(response.getcode())
print(len(htmlcode))

htmlcode = htmlcode.decode("utf-8")
print(htmlcode)
#添加header模仿浏览器进行爬虫,终 19.3.6
'''
'''
#通过debuglog查看收发包数据，始19.3.8
httpHandler = request.HTTPHandler(debuglevel=1)
httpsHandler = request.HTTPSHandler(debuglevel=1)
opener = request.build_opener(httpHandler, httpsHandler)
request.install_opener(opener)
response = request.urlopen('http://www.baidu.com')
#通过debuglog查看收发包数据，终19.3.8
'''
'''
#cookie的相关用法
#声明一个cookie对象的实例用来保存cookie
cookie = cookiejar.CookieJar()
#利用request.HTTPCookieProcessor对象来创建cookie处理器,也就是CookieHandler
handler = request.HTTPCookieProcessor(cookie)
#通过CookieHandler创建opener
opener = request.build_opener(handler)
#这里用opener的方法去打开网页
response = opener.open('http://www.baidu.com')
#打印cookie信息
for item in cookie:
    print('Name = %s'%item.name)
    print('Value = %s'%item.value)
    
