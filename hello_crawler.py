import urllib2
resource = urllib2.urlopen('http://tieba.baidu.com/p/1753935195')
return = resource.read()
print(ret)
