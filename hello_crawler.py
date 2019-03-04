import urllib2
res = urllib2.urlopen('http://tieba.baidu.com/p/1753935195')
ret = res.read()
print(ret)
