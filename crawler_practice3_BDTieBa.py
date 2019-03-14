import urllib
from urllib import request
import re


class BDTB:
#初始化，传入基地址，和是否只看楼主等参数
    def __init__(self,baseurl,lz_only):
        self.BaseUrl = baseurl
        self.LZ_only = '?see_lz='+ str(lz_only)
        self.tool = Tool()
#爬虫代码
    def crawl_page(self,PageNum=1):
        try:
            url = self.BaseUrl + self.LZ_only + '&pg='+ str(PageNum)
            req = request.Request(url)
            resp = request.urlopen(req)
        except request.URLError as e:
            if hasattr(e,'reason'):
                print("百度贴吧打开失败原因：",e.reason)
                return None
        return resp.read()
#获取帖子标题
    def get_title(self):
        page = self.crawl_page(1)
        title_pattern = re.compile('<h3 class=\"core_title_txt.*?title=\"(.*?)\".*?</h3>',re.S)
        result = re.search(title_pattern,page.decode('utf-8'))
        if result:
            print(result.group(1).strip())
        else:
            pass
        return None
#获取帖子页数
    def get_pagecount(self):
        page = self.crawl_page(1)
        count_pattern = re.compile('<span class=\"red\">(.*?)</span>')
        result = re.search(count_pattern,page.decode('utf-8'))
        if result:
            print(result.group(1).strip())

    def get_content(self):
        page = self.crawl_page(1)
        content_pattern = re.compile('<div id=\"post_content.*?style=\"display\:;">(.*?)</div>')
        result = re.findall(content_pattern,page.decode('utf-8'))
        for item in result:
            #print(self.tool.replace(item))
            print(item)
            print("img标签:",re.search(re.compile('<img.*?>| {7}|'),item))
            print("超链接标签:",re.search(re.compile('<a.*?>|</a>'),item))
            print("其余标签:",re.search(re.compile('<.*?>'),item))

class Tool:
    #去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    #删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    #把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    #将表格制表<td>替换为\t
    replaceTD= re.compile('<td>')
    #把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    #将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    #将其余标签剔除
    removeExtraTag = re.compile('<.*?>')
    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        #strip()将前后多余内容删除
        return x.strip()

baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)

bdtb.get_content()
