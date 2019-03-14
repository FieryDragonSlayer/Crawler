import urllib
from urllib import request
import requests
import html
import re
import time

def craw_joke_list(page = 1):
    url = "https://www.qiushibaike.com/text/page/" + str(page)
    res = requests.get(url)
    #获取每个段子div的正则
    pattern = re.compile('<div class=\"article block untagged mb15.*?div class=\"content\".*?</div>',re.S )
    #把<br/>替换成换行
    body = html.unescape(res.text).replace("<br/>","\n")
    m = pattern.findall(body)
    #抽取用户名的正则
    user_pattern = re.compile('<div class=\"author clearfix\">.*?<h2>.*?</h2>',re.S)
    #抽取正文的正则
    joke_pattern = re.compile('<div class=\"content\">.*?</div>',re.S)
    for joke in m:
        user = user_pattern.findall(joke)
        output = []
        if len(user)>0:
            output.append(user[0])
        content = joke_pattern.findall(joke)
        if len(content)>0:
            output.append(content[0].replace("\n",""))
        print("\t".join(output))
    time.sleep(1)

if __name__ == '__main__':
    for i in range(1,11):
        craw_joke_list(i)
